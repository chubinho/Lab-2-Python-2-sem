from typing import Any
from protocol import TaskSource
from task import Task


class TaskConsumer:
    def accept_tasks(self, source: Any) -> list[Task]:
        if not isinstance(source, TaskSource):
            raise TypeError(
                f"Объект типа '{type(source).__name__}' не соответствует контракту TaskSource ")
        tasks = source.get_task()
        return tasks

    def accept_tasks_from_multiple_sources(self, sources: list[Any]) -> list[Task]:
        all_tasks = []

        for source in sources:
            tasks = self.accept_tasks(source)
            all_tasks.extend(tasks)

        return all_tasks
