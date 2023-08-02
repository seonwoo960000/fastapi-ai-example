from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
classifier = pipeline("sentiment-analysis")
translator = pipeline("translation_en_to_fr")

@app.post("/predict")
async def predict(text: str):
    result = classifier(text)[0]  # only get the first (and only) prediction
    return {"result": result}

@app.post("/translate")
async def translate(text: str):
    result = translator(text)[0]['translation_text']
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
