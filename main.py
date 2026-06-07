from fastapi import FastAPI, UploadFile
from tempfile import NamedTemporaryFile
from app.analyzer import analyze_csv

app=FastAPI()

@app.get('/health')
def health():
    return {'status':'ok'}

@app.post('/analyze')
async def analyze(file: UploadFile):
    with NamedTemporaryFile(delete=False,suffix='.csv') as tmp:
        tmp.write(await file.read())
        path=tmp.name
    return analyze_csv(path)
