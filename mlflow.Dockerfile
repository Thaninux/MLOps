FROM python:3.9-slim

RUN pip install mlflow psycopg2-binary

EXPOSE 5000

CMD mlflow server     --backend-store-uri sqlite:///mlruns/mlflow.db     --default-artifact-root /mlruns     --host 0.0.0.0     --port 5000