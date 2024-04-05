import logging
from fastapi import FastAPI, HTTPException, Query, APIRouter
from fastapi.responses import JSONResponse
import httpx
import os
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Suppress warnings
import warnings

warnings.filterwarnings("ignore")

class SchoolModel(BaseModel):
    name: str = Field(..., title="The name of the school.")
    address: str = Field(..., title="The location about the school.")
    zip: str = Field(..., title="The postal code where the school is located.")
    tuition_revenue_per_fte: int = Field(..., title="Expenditure of full-time about the school.")
    accreditor: str = Field(..., title="The accrediting agency of the school.")
    school_url: str = Field(..., title="The URL of the school.")


# Base URL of the Football News API
BASE_URL = "http://api.data.gov/ed/collegescorecard/v1/schools"
COLLEGE_API_KEY = "UaCGXU28T1tPDng2fjBcj1yaCQTaJtRZbv2sUtDC"


# router = APIRouter(prefix="/api/v1", tags=["content creator"])


def fetch_school_data(data: dict) -> List[SchoolModel]:
    schools_data = []
    for item in data.get("results", []):
        school_data = item.get("school", {})
        if school_data:
            schools_data.append(SchoolModel(**school_data))
    return schools_data

app = FastAPI()

@app.get("/", response_model=List[SchoolModel])
async def get_institution(
    name: str = Query(None, description="The name of the school to search for"),
):
    """Retrive all information about all high educational institions from the College Scorecard API.

    Args:
        `name`: "The name of the school to search for".
    """
    # Construct the query parameters
    params = {"api_key": COLLEGE_API_KEY}
    if name:
        params["school.name"] = name

    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(BASE_URL, params=params)
        logger.debug(f"Response URL: {response.url}")  # 输出实际请求的URL
        logger.debug(f"Response status code: {response.status_code}")
        
        if response.status_code != 200:
            logging.error(f"Failed to fetch data: {response.status_code} - {response.text}")
            raise HTTPException(
                status_code=response.status_code,
                detail="Error fetching institution information",
            )
        
        data = response.json()
        schools = fetch_school_data(data)

        if not schools:
            raise HTTPException(status_code=404, detail="School not found")

        return schools

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("college_board_api:app", host="0.0.0.0", port=8082, reload=True)