# server.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins (can be locked down later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample route
@app.get("/")
def root():
    return {"status": "Abyss API is online"}

# Placeholder for token feed
@app.get("/tokens")
def get_tokens():
    return [
        {"name": "TokenX", "score": 91},
        {"name": "DeepGem", "score": 87},
        {"name": "SubAqua", "score": 90}
    ]
