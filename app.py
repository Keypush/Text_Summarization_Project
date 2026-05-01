from fastapi import FastAPI
import uvicorn
import os
import sys
from fastapi.templating import Jinja2Templates
from starlette.requests import RedirectResponse
from fastapi.responses import Response
from textSummarization.pipeline.prediction import PredictionPipeline

text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response(content="Training Successful", media_type="text/plain")
    except Exception as e:
        print(f"Error occurred: {e}")
        return Response(content=f"Training failed {e}", media_type="text/plain")
    

@app.get("/predict")
async def predict():
    try:
        prediction_pipeline = PredictionPipeline()
        summary = prediction_pipeline.predict(text)
        return Response(content=f"Summary: {summary}", media_type="text/plain")
    except Exception as e:
        print(f"Error occurred: {e}")
        return Response(content=f"Prediction failed {e}", media_type="text/plain")
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)