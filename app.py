from fastapi import FastAPI, Query
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
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
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.post("/predict")
async def predict_route(
    text: str = Query(..., description="The text you want to summarize"),
    use_pre_trained_model: bool = Query(False, description="Toggle between pre-trained or base model")
):
    try:
        # Now use_pre_trained_model is a boolean passed from the URL
        prediction_pipeline = PredictionPipeline()
        
        # Calling your custom logic
        summary = prediction_pipeline.predict(text, pred_trained_model=use_pre_trained_model)
        
        return Response(content=f"Summary: {summary}", media_type="text/plain")

    except Exception as e:
        print(f"Error occurred: {e}")
        return Response(content=f"Prediction failed: {str(e)}", media_type="text/plain", status_code=500)
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)