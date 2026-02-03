from typing import Dict
from uuid import UUID

from backend.src.core.project import Project


PROJECTS: Dict[UUID, Project] = {}


def create_project(name: str, description: str) -> Project:
    project = Project.create(name=name, description=description)
    PROJECTS[project.id] = project
    return project


def list_projects() -> list[Project]:
    return list(PROJECTS.values())
