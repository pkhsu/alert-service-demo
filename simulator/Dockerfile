# 使用官方 Python 執行環境作為基礎映像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /usr/src/app

# 複製 Python 腳本到容器
COPY simulator.py ./

# 安裝 requests 庫
RUN pip install --no-cache-dir requests

# 當容器啟動時執行 Python 腳本
CMD [ "python", "./simulator.py" ]
