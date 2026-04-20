from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "Agent rodando 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/next-ll")
def next_ll():
    return {
        "recommendation": "Slinky Dog Dash",
        "plan_b": "Tower of Terror"
    }
