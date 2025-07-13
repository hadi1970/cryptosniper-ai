from fastapi import FastAPI
from predictor import get_prediction

app = FastAPI()

@app.get("/predict")
def predict(symbol: str = "BTCUSDT"):
    return get_prediction(symbol)
