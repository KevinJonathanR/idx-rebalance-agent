"""Download model files directly from HF HTTP API, bypassing LFS pointer issues. v2"""
import os
import requests

REPO_ID = "KevinJonathanR/idx-smart-rebalance-models"
LOCAL_DIR = "saved_models"

def download_models():
    api_url = f"https://huggingface.co/api/models/{REPO_ID}"
    siblings = requests.get(api_url).json().get("siblings", [])

    for s in siblings:
        fname = s["rfilename"]
        if fname.startswith("."):
            continue

        dest = os.path.join(LOCAL_DIR, fname)
        os.makedirs(os.path.dirname(dest), exist_ok=True)

        url = f"https://huggingface.co/{REPO_ID}/resolve/main/{fname}"
        print(f"Downloading {fname}...")
        with requests.get(url, stream=True, allow_redirects=True) as r:
            r.raise_for_status()
            with open(dest, "wb") as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)
        print(f"  → {os.path.getsize(dest)} bytes")

if __name__ == "__main__":
    download_models()