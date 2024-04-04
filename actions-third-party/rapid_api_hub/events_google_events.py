import httpx
from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi.responses import JSONResponse
from .rapid_config import RAPID_API_KEY
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

router = APIRouter(
    prefix='/api/v1',
    tags=['content creator']
)

# https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-events-search, [Search Events]
@router.get("/google-events")
async def google_events_search(
    query: str = Query(..., title="Search query", description="Search query / keyword including location and time.")
):
    """
    Search for local public events in a specific location and time.

    Args:
    - `query`: The search query for events, including location and time.
    """
    if not RAPID_API_KEY:
        raise HTTPException(status_code=500, detail={"error": "Rapid API key is missing."})
    url = "https://real-time-events-search.p.rapidapi.com/search-events"
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "real-time-events-search.p.rapidapi.com"
    }
    querystring = {
        "query": query
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail={"error": "Failed to fetch Google events information."})