from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None

@app.get('/')
async def hello_world():
    return {"hello": "world"}

@app.get('/test')
async def hello_world():
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)


@app.get('/component/{component_id}') #path parameter
async def get_component(component_id: int):
    return{"component_id": component_id}

@app.get('/component/') #query parameter
async def read_component(number: int, text: str):
    return {"number": number, "text": text}

@app.post("/package/") # body
async def make_package(package: Package):
    return package

@app.post("/package/{priority}") # body with path parameter
async def make_package(priority: int, package: Package):
    return {"priority": priority, **package.dict()}

@app.post("/package/qp/{priority}") # body with path parameter and query parameter
async def make_package(priority: int, package: Package, value: int):
    return {"priority": priority, **package.dict(), "value": value}


