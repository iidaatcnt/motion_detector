# ベースとなるPythonイメージを指定
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なシステムライブラリをインストール (OpenCVのGUI機能に必要)
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# requirements.txtをコンテナにコピー
COPY requirements.txt .

# Pythonライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコンテナにコピー
COPY motion_detector.py .

# コンテナ実行時に起動するコマンド
CMD ["python3", "motion_detector.py"]
