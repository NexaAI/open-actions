from fastapi import FastAPI
from rapid_api_hub import events_google_events
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse
import socket
import uvicorn

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Open Actions APIs from third-party services",
        version="0.0.1",
        description="APIs for LLM Actions from third-party services",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
app.include_router(events_google_events.router)
hostname = socket.gethostname()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return f"API is hosted on {hostname}"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8079, reload=True)