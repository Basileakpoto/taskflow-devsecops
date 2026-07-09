from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    description: str
    status: str = "À faire"

    def mark_done(self):
        self.status = "Terminée"
