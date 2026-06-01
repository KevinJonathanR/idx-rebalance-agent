FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    git-lfs \
    && rm -rf /var/lib/apt/lists/*

# Install CPU-only PyTorch first to keep image size minimal
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Download all model files from HF Model repo at build time
RUN pip install --no-cache-dir huggingface_hub && \
    python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='KevinJonathanR/idx-smart-rebalance-models', repo_type='model', local_dir='saved_models')"

EXPOSE 7860

CMD ["uvicorn", "api_backend:app", "--host", "0.0.0.0", "--port", "7860"]
