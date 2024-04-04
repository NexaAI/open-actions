import httpx
from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi.responses import JSONResponse
import logging