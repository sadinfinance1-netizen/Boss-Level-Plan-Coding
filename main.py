from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "Boss Level Active", "message": "System Online."}

@app.get("/api/stats")
def get_stats():
    return {"current_layer": 1, "focus": "High-Performance Engine", "days_active": 1}
