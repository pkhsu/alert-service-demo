from fastapi import FastAPI, Request
import logging
from typing import List

# 設定日誌配置
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# 假設存儲告警數據的結構
alerts = []

@app.post("/webhook")
async def receive_alert(request: Request):
    alert = await request.json()
    alerts.append(alert)
    # 日誌記錄收到的告警
    logging.info(f"Received alert: {alert}")
    return {"message": "Alert received"}

@app.get("/alerts")
def get_alerts():
    return alerts
