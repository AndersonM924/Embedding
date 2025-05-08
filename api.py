from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SimpleInput(BaseModel):
    text: str

@app.post("/test")
def test_endpoint(data: SimpleInput):
    return {"length": len(data.text)}
