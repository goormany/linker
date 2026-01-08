import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from src.api.links import router as router_links

app = FastAPI()
app.include_router(router_links)


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", reload=True)