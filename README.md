# EduNova Payment Diagnostics

FastAPI + CLI tool for payment authorization root-cause analysis.

## Run

```bash
pip install -r requirements.txt
python generate_data.py
python cli.py data/transactions.csv
uvicorn app.main:app --reload
```

## API

- POST /analyze
- GET /health
