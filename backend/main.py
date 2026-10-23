
from fastapi import FastAPI

app = FastAPI(title="LinkRide Backend")

@app.get("/")
def home():
    return {"message": "LinkRide backend is running!"}

    @app.get("/health")
    def health():
        return {"status": "ok"}
    