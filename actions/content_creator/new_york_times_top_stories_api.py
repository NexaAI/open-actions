import httpx
from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi.responses import JSONResponse
import logging
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

load_dotenv()
NYT_API_KEY = os.getenv("NYT_API_KEY")

router = APIRouter(
    prefix='/api/v1',
    tags=['content creator']
)

# https://developer.nytimes.com/docs/top-stories-product/1/routes/%7Bsection%7D.json/get
@router.get("/new-york-times-top-stories")
async def new_york_times_top_stories(
    section: str = Query(..., title="Section", description="The section the story appears in. The following values are allowed:arts, automobiles, books/review, business, fashion, food, health, home, insider, magazine, movies, nyregion, obituaries, opinion, politics, realestate, science, sports, sundayreview, technology, theater, t-magazine, travel, upshot, us, world"),
):
    """
    Get the top stories from The New York Times.
    
    Args:
    - `section`: The section the story appears in. The following values are allowed: arts, automobiles, books/review, business, fashion, food, health, home, insider, magazine, movies, nyregion, obituaries, opinion, politics, realestate, science, sports, sundayreview, technology, theater, t-magazine, travel, upshot, us, world.
    """

    url = f"https://api.nytimes.com/svc/topstories/v2/{section}.json?api-key={NYT_API_KEY}"

    async with httpx.AsyncClient() as client:  
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching news from the New York Times")
        
        news_items = response.json().get("results", [])[:10]
        
        return news_items

    

