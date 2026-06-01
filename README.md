---
title: IDX Smart Rebalance
emoji: 📈
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# IDX Smart Rebalance — AI-Powered Sectoral Portfolio Optimizer

> **Datathon Ristek Fasilkom UI 2025** · Tim Gacor · Telkom University

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)](https://fastapi.tiangolo.com)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Hugging%20Face%20Spaces-yellow?logo=huggingface)](https://huggingface.co/spaces/KevinJonathanR/idx-smart-rebalance)

---

## 🚀 Live Demo

**[→ Try it on Hugging Face Spaces](https://huggingface.co/spaces/KevinJonathanR/idx-smart-rebalance)**

> Input your portfolio amount (IDR) → get sector allocation recommendations optimized for the **next 7 days**, factoring in live IDX market data and **current geopolitical risk conditions** (GPR Index).
>
> *First run fetches live data and runs inference — allow ~2–3 minutes.*

---

## What It Does

Given a portfolio amount in IDR, the system outputs how much to allocate across **11 IDX sectors** for the next 7 days — minimizing volatility exposure based on current market conditions and geopolitical risk.

**Under the hood:**
1. **Volatility Forecasting** — 11 sector-specific deep learning models (TFT, LSTM, N-HiTS, N-BEATS-X) predict 7-day-ahead volatility for each IDX sector using live market data + GPR Index (Geopolitical Risk) as exogenous features
2. **Portfolio Optimization** — A pre-trained **Soft Actor-Critic (SAC)** reinforcement learning agent takes predicted volatilities as input and outputs optimal capital allocation weights across all 11 sectors
3. **Interactive Dashboard** — Plotly.js charts show per-sector volatility forecasts, a portfolio pie chart, and IDR breakdown per sector

**Tech Stack:** FastAPI · NeuralForecast (TFT/LSTM/N-HiTS/N-BEATS-X) · Stable-Baselines3 (SAC) · yfinance · Plotly.js

---

## Architecture

```
User Input (IDR amount)
        │
        ▼
┌──────────────────────────────────┐
│  Live Data Fetch                  │  yfinance (11 IDX sectors) + GPR Index
├──────────────────────────────────┤
│  7-Day Volatility Forecast        │  11 sector-specific DL models
├──────────────────────────────────┤
│  Portfolio Allocation (SAC DRL)   │  predicted volatility → sector weights
└──────────────────────────────────┘
        │
        ▼
  Allocation recommendation (% per sector + IDR amount)
```

| Sector | Model |
|---|---|
| Basic Materials, Properties, Transportation | N-HiTS |
| Consumer Cyclicals, Industrials | N-BEATS-X |
| Consumer Non-Cyclicals, Financials, Infra, Technology, Healthcare | TFT |
| Energy | LSTM |

---

## Run Locally

```bash
git clone https://github.com/KevinJonathanR/idx-rebalance-agent.git
cd idx-rebalance-agent
pip install -r requirements.txt
uvicorn api_backend:app --reload --host 0.0.0.0 --port 8000
# Open http://localhost:8000
```

---

*Built for Datathon Ristek Fasilkom UI 2025 by Tim Gacor — Telkom University*