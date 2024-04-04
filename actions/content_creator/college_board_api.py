import logging
from fastapi import FastAPI, HTTPException, Query, APIRouter
from fastapi.responses import JSONResponse
import httpx
import os
from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Suppress warnings
import warnings

warnings.filterwarnings("ignore")
# Base URL of the Football News API
BASE_URL = "http://api.data.gov/ed/collegescorecard/"
COLLEGE_API_KEY = "UaCGXU28T1tPDng2fjBcj1yaCQTaJtRZbv2sUtDC"
COLLEGE_SCORECARD_API_URL = "http://api.data.gov/ed/collegescorecard/v1/schools"

router = APIRouter(
    prefix='/api/v1',
    tags=['content_creator']
)

class SchoolBoard(BaseModel):
    name: str = Query(..., title="Name", description="Name of the institution.")

@router.get("/institution")
async def get_institution(name: str):
    # Construct the query parameters
    params = {
        'school.name': name,
        'api_key': 'COLLEGE_API_KEY'  
    }

    # Forward the request to the College Scorecard API
    async with httpx.AsyncClient() as client:
        response = await client.get(COLLEGE_SCORECARD_API_URL, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching institution information")

    # Return the response from the College Scorecard API
    return response.json()
