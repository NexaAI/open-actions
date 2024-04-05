import os
import logging
import httpx
from mistralai.client import MistralClient
from actions.content_creator import college_board_api

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
mistral_client = MistralClient(api_key=MISTRAL_API_KEY)
COLLEGE_API_KEY = "UaCGXU28T1tPDng2fjBcj1yaCQTaJtRZbv2sUtDC"

BASE_URL = "http://api.data.gov/ed/collegescorecard/v1/schools"

# Retrieve the answer from the College Board API
async def retrieve_answer_from_college_board(name: str ):
    params = {"api_key": COLLEGE_API_KEY, "school.name": name}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)

        if response.status_code == 200:
            school_data = response.json().get('results', [])
            return school_data
        else:
            logging.error(f"Failed to fetch school data: {response.status_code} - {response.text}")
            return None

  
  