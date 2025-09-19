# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from parsers import get_parser

app = FastAPI()

# Allow frontend JS to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your domain once deployed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/decode")
def decode(manufacturer: str, serial: str):
    parser = get_parser(manufacturer)
    if not parser:
        raise HTTPException(status_code=400, detail="No parser available for this manufacturer")
    try:
        result = parser(serial)
        return {"manufacturer": manufacturer, "serial": serial, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error decoding serial: {str(e)}")

@app.get("/")
def home():
    return {"message": "HVAC Serial Decoder API"}
