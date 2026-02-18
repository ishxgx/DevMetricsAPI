import httpx

GITHUB_API = "https://api.github.com"

def fetch_repo(owner: str, repo: str) -> dict:
    url = f"{GITHUB_API}/repos/{owner}/{repo}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "devmetrics-api",
    }

    with httpx.Client(timeout=10.0, follow_redirects=True) as client:
        r = client.get(url, headers=headers)
        if r.status_code == 404:
            return {"_error": "not_found"}
        r.raise_for_status()
        return r.json()
