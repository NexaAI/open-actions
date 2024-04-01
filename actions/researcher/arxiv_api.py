from typing import List, Dict
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
import logging
import requests
from xml.etree import ElementTree as ET

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

router = APIRouter(
    prefix='/api/v1',
    tags=['researcher']
)

# 
@router.get("/arxiv", response_model=List[Dict])
async def arxiv(
    query: str = Query(..., title="Query", description="Search query for papers."),
    max_results: int = Query(default=10, ge=1, le=100, title="Max results", description="Maximum number of results to return.")
) -> JSONResponse:
    """
    From arXiv, Fetch the latest research papers based on the query.
    """
    formatted_query = "+".join(query.split(" "))
    url = f'http://export.arxiv.org/api/query?search_query=all:{formatted_query}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
        raise HTTPException(status_code=400, detail=str(http_err))
    except Exception as err:
        logging.error(f'An error occurred: {err}')
        raise HTTPException(status_code=500, detail=str(err))
    
    xml_data = response.content
    root = ET.fromstring(xml_data)
    ns = {'ns': 'http://www.w3.org/2005/Atom'}
    results = []

    for entry in root.findall('ns:entry', ns):
        result = {
            "title": entry.find('ns:title', ns).text.strip(),
            "authors": [author.text for author in entry.findall('ns:author/ns:name', ns)],
            "summary": entry.find('ns:summary', ns).text.strip(),
            "link": entry.find('ns:id', ns).text.strip(),
            "published_date": entry.find('ns:published', ns).text.strip()
        }
        results.append(result)
    
    return JSONResponse(content=results)