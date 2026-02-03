from fastapi import FastAPI
from pydantic import BaseModel

from backend.src.api.projects import create_project, list_projects


app = FastAPI(title="AI Project Assistant")


class ProjectCreateRequest(BaseModel):
    name: str
    description: str


@app.post("/projects")
def create_project_endpoint(payload: ProjectCreateRequest):
    return create_project(
        name=payload.name,
        description=payload.description,
    )


@app.get("/projects")
def list_projects_endpoint():
    return list_projects()
