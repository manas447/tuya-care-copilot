from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai_agent import analyze_issue
from tuya_mock import get_device_logs

app = FastAPI()

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "TuyaCare Copilot running"}

@app.post("/analyze")
def analyze(data: dict):
    device_id = data.get("device_id")
    logs = get_device_logs(device_id)
    response = analyze_issue(logs)
    return {
        "device_id": device_id,
        "logs": logs,
        "analysis": response
    }
