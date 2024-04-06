from fastapi import FastAPI
from content_creator import ai_tool_search_api, new_york_times_top_stories_api
from researcher import arxiv_api
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse
import socket
import uvicorn

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Open Actions APIs",
        version="0.0.1",
        description="APIs for LLM Actions",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
app.include_router(ai_tool_search_api.router)
app.include_router(arxiv_api.router)
app.include_router(new_york_times_top_stories_api.router)

hostname = socket.gethostname()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return f"API is hosted on {hostname}"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)