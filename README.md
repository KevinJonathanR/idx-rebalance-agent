---
title: IDX Smart Rebalance
emoji: 📈
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# IDX Smart Rebalance — AI-Powered Sectoral Portfolio Optimization

> **Datathon Ristek Fasilkom UI 2025** · Tim Gacor · Telkom University

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)](https://fastapi.tiangolo.com)
[![HuggingFace](https://img.shields.io/badge/Live%20Demo-Hugging%20Face%20Spaces-yellow?logo=huggingface)](https://huggingface.co/spaces/YOUR_USERNAME/idx-smart-rebalance)

---

## What It Does

IDX Smart Rebalance is a real-time portfolio recommendation system for the **Indonesian Stock Exchange (IDX)**. It combines:

1. **Volatility Forecasting** — 11 sector-specific deep learning models (TFT, LSTM, N-HiTS, N-BEATS-X via NeuralForecast) predict 7-day-ahead sector volatility using live market data + geopolitical risk indicators (GPR Index)
2. **DRL Portfolio Optimization** — A pre-trained **Soft Actor-Critic (SAC)** reinforcement learning agent (Stable-Baselines3) allocates capital across 11 IDX sectors to minimize volatility exposure
3. **Interactive Dashboard** — Vanilla JS + Plotly.js frontend shows forecast charts, sector allocation pie chart, and IDR-denominated portfolio breakdown

**Tech Stack:** FastAPI · NeuralForecast (TFT/LSTM/N-HiTS) · Stable-Baselines3 (SAC) · yfinance · Plotly.js · Vanilla JS

---

## Architecture

```
User Input (IDR amount)
        │
        ▼
┌─────────────────────┐
│  FastAPI Backend     │  ← serves frontend + API
├─────────────────────┤
│  get_data.py         │  ← yfinance + GPR Index (live)
│  predict.py          │  ← 11x NeuralForecast models
│  predict.py (DRL)    │  ← SAC agent → sector weights
└─────────────────────┘
        │
        ▼
  Plotly.js Charts + Portfolio Table
```

**Models per sector:**
| Sector | Model |
|---|---|
| Basic Materials, Properties, Transportation | N-HiTS |
| Consumer Cyclicals, Industrials | N-BEATS-X |
| Consumer Non-Cyclicals, Financials, Infra, Technology, Healthcare | TFT |
| Energy | LSTM |

---

## Live Demo

🚀 **[Try it on Hugging Face Spaces →](https://huggingface.co/spaces/YOUR_USERNAME/idx-smart-rebalance)**

> First run downloads live IDX data and runs inference — expect ~2–3 minutes for the full pipeline.

---

## Run Locally

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/idx-smart-rebalance.git
cd idx-smart-rebalance

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start server (serves frontend + API at localhost:8000)
uvicorn api_backend:app --reload --host 0.0.0.0 --port 8000

# 4. Open http://localhost:8000
```

## Run with Docker

```bash
docker build -t idx-smart-rebalance .
docker run -p 8000:7860 idx-smart-rebalance
# Open http://localhost:8000
```

---

## Project Structure

```
idx-smart-rebalance/
├── api_backend.py          # FastAPI app (API + static file serving)
├── src/
│   ├── get_data.py         # Live data: yfinance + GPR Index
│   ├── predict.py          # NeuralForecast inference + SAC DRL agent
│   └── train.py            # Model training scripts
├── web/                    # Frontend (vanilla JS + Plotly.js)
├── saved_models/
│   ├── Forecast_Model/     # 11 sector-specific .ckpt checkpoints
│   └── DRL_Model/          # SAC_Portfolio.zip + standard_scaler.pkl
├── data/                   # Sector mapping + pre-processed CSVs
├── Dockerfile              # For Hugging Face Spaces deployment
└── requirements.txt
```

---

*Built for Datathon Ristek Fasilkom UI 2025 by Tim Gacor — Telkom University*
