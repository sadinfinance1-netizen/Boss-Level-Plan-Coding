from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize the backend application
app = FastAPI()

# CORS (Cross-Origin Resource Sharing)
# This acts as a bouncer. It tells the backend that it is safe to accept 
# requests from your HTML Dashboard hosted on a different URL.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any website to connect (good for beginners)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint 1: A simple health check (like checking a pulse)
@app.get("/")
def check_status():
    return {
        "status": "Boss Level Active",
        "message": "Backend is online and ready for commands."
    }

# Endpoint 2: Sending data to your dashboard
@app.get("/api/stats")
def get_stats():
    return {
        "current_layer": 1,
        "focus": "High-Performance Engine",
        "days_active": 1
    }
