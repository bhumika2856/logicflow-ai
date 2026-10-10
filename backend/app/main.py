from fastapi import FastAPI

app = FastAPI(
    title="LogicFlow API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "LogicFlow Backend Running"
    }