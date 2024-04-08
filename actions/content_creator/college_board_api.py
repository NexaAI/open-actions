import logging
from fastapi import FastAPI, HTTPException, Query, APIRouter
from fastapi.responses import JSONResponse
import httpx
import os
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import json

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Suppress warnings
import warnings

warnings.filterwarnings("ignore")


# Base URL of the Football News API
BASE_URL = "http://api.data.gov/ed/collegescorecard/v1/schools"
COLLEGE_API_KEY = "UaCGXU28T1tPDng2fjBcj1yaCQTaJtRZbv2sUtDC"


router = APIRouter(prefix="/api/v1", tags=["content creator"])


def fetch_school_data(data: dict) -> List[Dict]:
    results = data.get("results", [])
    school_data_list = []

    for item in results:
        school_data = item.get("school")
        if school_data:
            school_data_list.append(school_data)

    return school_data_list

@router.get("/retrieve_answer_from_college_board", response_model=List[Dict])
async def get_institution(
    state: Optional[str] = Query(None, description="State of the school"),
    city: Optional[str] = Query(None, description="City of the school"),
    zip: Optional[str] = Query(None, description="Postal code of the school"),
    name: Optional[str] = Query(None, description="Name of the school")
):
    """Retrive all information about all high educational institions from the College Scorecard API.

    Args:
        `name`: "The name of the school to search for".
    """

    # Construct the query parameters
    params = {"api_key": COLLEGE_API_KEY}
    if state:
        params["school.state"] = state
    if city:
        params["school.city"] = city
    if zip:
        params["school.zip"] = zip
    if name:
        params["school.name"] = name

    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(BASE_URL, params=params)

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Failed to fetch data: {response.status_code} - {response.text}",
            )

        data = response.json()
        schools = fetch_school_data(data)

        if not schools:
            raise HTTPException(status_code=404, detail="School not found")
        
        return schools

