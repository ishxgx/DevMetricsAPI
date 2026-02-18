from pydantic import BaseModel, Field

class RepoMetrics(BaseModel):
    repo: str = Field(..., examples=["owner/repo"])
    stars: int = Field(..., ge=0)
    forks: int = Field(..., ge=0)
    open_issues: int = Field(..., ge=0)
    score: float = Field(..., ge=0, le=100)
