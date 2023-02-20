import json
from typing import Union
import pandas as pd
import datetime as dt
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

origins = [
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/") 
async def main_route():     
    return {"message": "true"}


@app.get("/price/{contractAddress}")
async def get_price(contractAddress: str):
    data = 16824.22
    return {'price': data}


@app.get("/candles/{contractAddress, startTime, endTime, candleDuration}")
async def get_candles(contractAddress: str, startTime: int, endTime: int, candleDuration: int):
    path = f'storage/candles.csv'
    data = pd.read_csv(path)[['time', 'open', 'high', 'low', 'close']].values
    output = [{'time': value[0], 'open': value[1], 'high': value[2], 'low': value[3], 'close': value[4]} for value in data]
    return output
