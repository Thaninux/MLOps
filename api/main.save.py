from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import mlflow.pyfunc
from datetime import datetime

app = FastAPI(title="API Prévision Élec", version="0.1")

model = None

class Req(BaseModel):
    timestamp: datetime

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/predict")
def predict(req: Req):
    global model
    if model is None:
        try:
            mlflow.set_tracking_uri("http://localhost:5001")
            model = mlflow.pyfunc.load_model("runs://model")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"off {err}")

    df = pd.DataFrame([{"timestamp": req.timestamp}])
    try:
        pred = model.predict(df)[0]
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"erreur {err}")

    return {"timestamp": req.timestamp, "consommation": float(pred)}

