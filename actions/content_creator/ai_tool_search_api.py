import httpx
from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi.responses import JSONResponse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

router = APIRouter(
    prefix='/api/v1',
    tags=['content creator']
)

@router.get("/ai-tools")
async def search_ai_tools():
    pass