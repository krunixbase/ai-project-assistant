from uuid import uuid4

from core.stage import Stage, StageStatus


def test_create_stage_defaults_to_draft():
    project_id = uuid4()
    stage = Stage.create(project_id=project_id, name="Etap 1", description="Start")

    assert stage.project_id == project_id
    assert stage.status == StageStatus.draft
    assert stage.id is not None


def test_stage_happy_path_transitions():
    stage = Stage.create(project_id=uuid4(), name="Etap 1", description="Start")

    stage.start()
    assert stage.status == StageStatus.in_progress

    stage.mark_done()
    assert stage.status == StageStatus.done

    stage.confirm()
    assert stage.status == StageStatus.confirmed


def test_stage_invalid_transitions_raise():
    stage = Stage.create(project_id=uuid4(), name="Etap 1", description="Start")

    try:
        stage.confirm()
        assert False, "Expected ValueError"
    except ValueError:
        assert True
