import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from mlflow.models.signature import infer_signature

def train(data_path: str):
    df = pd.read_csv(data_path)
    X = df[["hour", "Global_active_power"]]
    y = df["Global_intensity"]

    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("PowerConsumption")

    with mlflow.start_run():
        model = RandomForestRegressor()
        model.fit(X, y)
        mse = mean_squared_error(y, model.predict(X))
        mlflow.log_metric("mse", mse)
        signature = infer_signature(X, model.predict(X))
        mlflow.sklearn.log_model(
    model,
    artifact_path="model",
    signature=signature,
    registered_model_name="PowerConsumptionModel"
)


if __name__ == "__main__":
    train("data/processed/power_2008.csv")