import requests
import random
import logging
from time import sleep

# 設定日誌級別和格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 設定 API 端點 URL (使用 Docker Compose 服務名稱)
api_url = 'http://alertmanager:9093/api/v2/alerts'

# 無窮迴圈來模擬定期發送數據
while True:
    # 隨機生成溫度和濕度數據
    temperature = random.uniform(20, 30)
    humidity = random.uniform(30, 70)
    
    # 創建一個告警的 payload
    alert_data = [
        {
            "labels": {
                "alertname": "TemperatureHumidityAlert",
                "sensor": "Sensor1",
            },
            "annotations": {
                "info": f"Temperature: {temperature}, Humidity: {humidity}",
            }
        }
    ]
    
    try:
        # 發送告警到 AlertManager
        response = requests.post(api_url, json=alert_data)
        response.raise_for_status()  # 將引發 HTTPError，如果HTTP請求返回了不成功的狀態碼
        
        # 如果發送成功，記錄信息
        logging.info(f"Data sent successfully: Temperature: {temperature}, Humidity: {humidity}")
    except requests.exceptions.HTTPError as http_err:
        # 記錄 HTTP 錯誤信息
        logging.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        # 記錄其他錯誤信息
        logging.error(f'An error occurred: {err}')

    # 暫停一段時間，比如每 30 秒發送一次數據
    sleep(30)
