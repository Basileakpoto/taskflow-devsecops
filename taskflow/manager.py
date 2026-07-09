from taskflow.task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        if not title:
            raise ValueError("Le titre ne peut pas être vide.")

        task = Task(
            id=len(self.tasks) + 1,
            title=title,
            description=description
        )
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def mark_done(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_done()
                return True
        return False
