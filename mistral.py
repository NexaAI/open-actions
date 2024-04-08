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
import asyncio
from mistral_functions_list import TOOL_LIST, FUNCTION_LIST

import json


os.environ["TZ"] = "America/Los_Angeles"
time.tzset()
today_date = time.strftime("%Y_%m_%d", time.localtime())

load_dotenv()

# Mistral API key and configuration
MISTRAL_API_KEY = os.environ["MISTRAL_API_KEY"]
MODEL_NAME = "mistral-small-latest"
monthly_token_limit = 10000000000

current_monthly_usage = 0
client = MistralClient(api_key=MISTRAL_API_KEY)


def check_usage(usage, limit):
    percentage = usage / limit * 100
    if percentage > 95:
        logging.warning("API usage is above 95%, stopping function calls.")
        return False
    elif percentage > 80:
        logging.info("API usage is above 80%.")
    return True


INSTRUCTION_1 = "Retrive all information about High institutions."

INSTRUCTION_2 = "University of California-Berkeley"
INSTRUCTION_3 = "Retrive all the institutions in CA."


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
async def query_mistral_api():
    # Load the current monthly usage
    global current_monthly_usage

    # Check if the usage is above 95%
    if not check_usage(current_monthly_usage, monthly_token_limit):
        return None

    messages = [
        ChatMessage(
            role="user",
            content=INSTRUCTION_1,
        )
    ]

    try:
        response = client.chat(
            model=MODEL_NAME,
            messages=messages,
            tools=TOOL_LIST,
            tool_choice="auto",
        )
        if not response or not response.choices:
            logging.error("No response or no choices in the response from Mistral API")
            return None

        messages.append(
            ChatMessage(role="assistant", content=response.choices[0].message.content)
        )
        messages.append(
            ChatMessage(
                role="user",
                content=INSTRUCTION_2,
                tools=TOOL_LIST,
                tool_choice="auto",
            )
        )
        response = client.chat(
            model=MODEL_NAME, messages=messages, tools=TOOL_LIST, tool_choice="auto"
        )

        messages.append(response.choices[0].message)
        if (
            not response
            or not response.choices
            or not response.choices[0].message.tool_calls
        ):
            logging.error(
                "No response or no tool calls in the response from Mistral API"
            )
            return None
        print("messages: ", messages)

        tool_call = response.choices[0].message.tool_calls[0]

        function_name = tool_call.function.name
        function_params = json.loads(tool_call.function.arguments)
        print(
            "\nfunction_name: ", function_name, "\nfunction_params: ", function_params
        )

        function_result = await FUNCTION_LIST["get_institution"](**function_params)

        if isinstance(function_result, (list, dict)):
            function_result = json.dumps(function_result)
        print
        messages.append(
            ChatMessage(role="tool", name=function_name, content=function_result)
        )

        response = client.chat(model=MODEL_NAME, messages=messages)

    except Exception as e:
        logging.error(f"Error querying Mistral API: {e}")
        return None

    return response.choices[0].message.content


async def main():
    logging.basicConfig(level=logging.INFO)
    response = await query_mistral_api()
    if response:
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
