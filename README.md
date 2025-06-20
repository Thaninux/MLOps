# ⚡ MLOps Power Consumption Project

## 📁 Structure du projet

```
.
├── docker-compose.yml
├── mlflow.Dockerfile
├── mlruns/
│   └── mlflow.db
├── ml/
│   ├── train.py
│   ├── preprocessing.py
│   └── requirements.txt
├── data/
│   ├── household_power_consumption.txt
│   └── processed/
│       └── power_2008.csv (généré après preprocessing)
```

---

## 🚀 Étapes pour exécuter le projet

### 1. Installer les dépendances Python
```bash
pip install -r ml/requirements.txt
```

### 2. Prétraiter les données
```bash
mkdir -p data/processed
python ml/preprocessing.py
```

### 3. Lancer MLflow et l’API FastAPI
```bash
docker-compose up --build
```

- MLflow accessible sur : http://localhost:5000

### 4. Entraîner le modèle (dans un autre terminal)
```bash
python ml/train.py
```

- Le modèle est enregistré dans MLflow avec le nom **PowerConsumptionModel**


## ✅ Fonctionnalités

- Tracking d’expériences avec MLflow
- Registry de modèles
- Infrastructure containerisée avec Docker
- Données prétraitées et sauvegardées

---