import logging
import os
import json
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv
import time
import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import functools
import mistral_functions_list
import mistral_function
import json


os.environ["TZ"] = "America/Los_Angeles"
time.tzset()
today_date = time.strftime("%Y_%m_%d", time.localtime())

load_dotenv()

# Mistral API key and configuration
MISTRAL_API_KEY = os.environ["MISTRAL_API_KEY"]
MODEL_NAME = "open-mistral-7b"
monthly_token_limit = 10000000000

current_monthly_usage = 0


def check_usage(usage, limit):
    percentage = usage / limit * 100
    if percentage > 95:
        logging.warning("API usage is above 95%, stopping function calls.")
        return False
    elif percentage > 80:
        logging.info("API usage is above 80%.")
    elif percentage > 50:
        logging.info("API usage is above 50%.")
    elif percentage > 30:
        logging.info("API usage is above 30%.")
    return True


names_to_functions = {
    "retrieve_answer_from_college_board": functools.partial(
        mistral_function.retrieve_answer_from_college_board,
    )
}

INSTRUCTION = """
Retrive all information about the University of California, Berkeley from the College Scorecard API.
"""
def prompt_function_call(function_name, parameters):
    if function_name in names_to_functions:
        return names_to_functions[function_name](**parameters)
    else:
        return json.dumps({"status": "Function not found"})


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def query_mistral_api(prompt):
    # Load the current monthly usage
    global current_monthly_usage

    # Check if the usage is above 95%
    if not check_usage(current_monthly_usage, monthly_token_limit):
        return None

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + MISTRAL_API_KEY,
    }
    body = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "message": prompt,
            }
        ],
    }
    try:
        response = requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers=headers,
            json=body,
            tools=mistral_functions_list.tools,
            tool_choice=names_to_functions,
        )
        if response.status_code == 200:
            response_data = response.json()
            # Update the current monthly usage
            usage_data = response_data.get("usage", {})
            prompt_tokens = usage_data.get("prompt_tokens", 0)
            completion_tokens = usage_data.get("completion_tokens", 0)

            # Update the current monthly usage
            current_monthly_usage += prompt_tokens + completion_tokens
            return response_data
        else:
            logging.error(f"Error querying Mistral API: HTTP {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Error querying Mistral API: {e}")
        return None
