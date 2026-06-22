"""Download model files directly from HF HTTP API, bypassing LFS pointer issues."""
import os
import requests
from requests.adapters import HTTPAdapter, Retry

REPO_ID = "KevinJonathanR/idx-smart-rebalance-models"
LOCAL_DIR = "saved_models"
TIMEOUT = 30  # seconds per request

def _session():
    s = requests.Session()
    retries = Retry(total=5, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504])
    s.mount("https://", HTTPAdapter(max_retries=retries))
    return s

def download_models():
    session = _session()
    api_url = f"https://huggingface.co/api/models/{REPO_ID}"
    siblings = session.get(api_url, timeout=TIMEOUT).json().get("siblings", [])

    for s in siblings:
        fname = s["rfilename"]
        if fname.startswith("."):
            continue

        dest = os.path.join(LOCAL_DIR, fname)
        os.makedirs(os.path.dirname(dest), exist_ok=True)

        url = f"https://huggingface.co/{REPO_ID}/resolve/main/{fname}"
        print(f"Downloading {fname}...")
        with session.get(url, stream=True, allow_redirects=True, timeout=TIMEOUT) as r:
            r.raise_for_status()
            with open(dest, "wb") as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)
        print(f"  → {os.path.getsize(dest)} bytes")

if __name__ == "__main__":
    download_models()
