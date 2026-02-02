from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class Project:
    id: UUID
    name: str
    description: str
    created_at: datetime
    is_active: bool = True

    @staticmethod
    def create(name: str, description: str) -> "Project":
        return Project(
            id=uuid4(),
            name=name,
            description=description,
            created_at=datetime.utcnow(),
            is_active=True,
        )
