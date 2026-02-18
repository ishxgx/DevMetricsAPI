from fastapi import APIRouter, HTTPException
from app.schemas.metrics import RepoMetrics
from app.services.github import fetch_repo

router = APIRouter(prefix="/metrics", tags=["metrics"])

@router.get("/{owner}/{repo}", response_model=RepoMetrics)
def get_repo_metrics(owner: str, repo: str):
    data = fetch_repo(owner, repo)
    if data.get("_error") == "not_found":
        raise HTTPException(status_code=404, detail="Repository not found")

    stars = int(data.get("stargazers_count", 0))
    forks = int(data.get("forks_count", 0))
    open_issues = int(data.get("open_issues_count", 0))

    score = min(100.0, stars * 0.12 + forks * 0.6 - open_issues * 0.3)
    score = max(0.0, score)

    return RepoMetrics(
        repo=f"{owner}/{repo}",
        stars=stars,
        forks=forks,
        open_issues=open_issues,
        score=round(score, 2),
    )
