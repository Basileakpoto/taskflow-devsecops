from taskflow.manager import TaskManager


def test_add_task():
    manager = TaskManager()
    task = manager.add_task("Mémoire", "Rédiger le chapitre 5")

    assert task.id == 1
    assert task.title == "Mémoire"
    assert task.status == "À faire"


def test_mark_task_done():
    manager = TaskManager()
    task = manager.add_task("Soutenance", "Préparer les diapositives")

    result = manager.mark_done(task.id)

    assert result is True
    assert manager.list_tasks()[0].status == "Terminée"
