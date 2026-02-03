from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4


class StageStatus(str, Enum):
    draft = "draft"
    in_progress = "in_progress"
    done = "done"
    confirmed = "confirmed"


@dataclass
class Stage:
    id: UUID
    project_id: UUID
    name: str
    description: str
    created_at: datetime
    status: StageStatus = StageStatus.draft

    @staticmethod
    def create(project_id: UUID, name: str, description: str) -> "Stage":
        return Stage(
            id=uuid4(),
            project_id=project_id,
            name=name,
            description=description,
            created_at=datetime.utcnow(),
            status=StageStatus.draft,
        )

    def start(self) -> None:
        if self.status != StageStatus.draft:
            raise ValueError("Stage can only be started from draft.")
        self.status = StageStatus.in_progress

    def mark_done(self) -> None:
        if self.status != StageStatus.in_progress:
            raise ValueError("Stage can only be marked done from in_progress.")
        self.status = StageStatus.done

    def confirm(self) -> None:
        if self.status != StageStatus.done:
            raise ValueError("Stage can only be confirmed from done.")
        self.status = StageStatus.confirmed
