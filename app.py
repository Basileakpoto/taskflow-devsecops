from taskflow.manager import TaskManager


def main():
    manager = TaskManager()
    manager.add_task("Finaliser le mémoire", "Ajouter les résultats expérimentaux")
    manager.add_task("Préparer la soutenance", "Préparer les diapositives")

    for task in manager.list_tasks():
        print(f"{task.id} - {task.title} [{task.status}]")


if __name__ == "__main__":
    main()
