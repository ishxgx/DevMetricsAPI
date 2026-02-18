from fastapi.testclient import TestClient
import app.routers.metrics as metrics_router
from app.main import app

client = TestClient(app)

def test_metrics_missing_repo_segment_returns_404():
    r = client.get("/metrics/onlyowner")
    assert r.status_code == 404

def test_metrics_not_found(monkeypatch):
    def fake_fetch_repo(owner: str, repo: str):
        return {"_error": "not_found"}

    monkeypatch.setattr(metrics_router, "fetch_repo", fake_fetch_repo)

    r = client.get("/metrics/x/y")
    assert r.status_code == 404

def test_metrics_ok_mocked(monkeypatch):
    def fake_fetch_repo(owner: str, repo: str):
        return {
            "stargazers_count": 100,
            "forks_count": 20,
            "open_issues_count": 5,
        }

    monkeypatch.setattr(metrics_router, "fetch_repo", fake_fetch_repo)

    r = client.get("/metrics/tiangolo/fastapi")
    assert r.status_code == 200
    data = r.json()
    assert data["repo"] == "tiangolo/fastapi"
    assert data["stars"] == 100
    assert data["forks"] == 20
    assert data["open_issues"] == 5
    assert 0 <= data["score"] <= 100
