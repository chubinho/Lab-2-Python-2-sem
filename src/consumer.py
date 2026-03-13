import logging
from typing import Any
from src.protocol import TaskSource
from src.task import Task

logger = logging.getLogger("task")


class TaskConsumer:
    """
    Приёмник задач, который работает с любыми источниками,
    соблюдающими контракт TaskSource
    """

    def accept_tasks(self, source: Any) -> list[Task]:
        """
        Принятие задачи из источника с обязательной проверкой контракта
        Args:
            source: Любой объект, который должен быть источником задач
        Returns:
            list[Task]: Список объектов Task, полученных из источника

        Raises:
            TypeError: Если объект не соответствует контракту TaskSource.
        """
        logger.debug(f"Попытка получения задач из {type(source).__name__}")
        if not isinstance(source, TaskSource):
            logger.error(
                f"Объект типа '{type(source).__name__}' не соответствует контракту TaskSource ")
            raise TypeError(
                f"Объект типа '{type(source).__name__}' не соответствует контракту TaskSource ")

        logger.info(f"Получение задач из источника: {type(source).__name__}")
        tasks = source.get_task()

        return tasks

    def accept_tasks_from_multiple_sources(self, sources: list[Any]) -> list[Task]:
        """
        Принятие задач из нескольких источников одновременно
        Args:
            sources: Список объектов, которые должны быть источниками задач

        Returns:
            list[Task]: Объединённый список задач из всех источников

        Raises:
            TypeError: Если хотя бы один объект не соответствует контракту
        """
        all_tasks = []
        logger.info(f"Получение задач из {len(sources)} источников")
        for source in sources:
            tasks = self.accept_tasks(source)
            all_tasks.extend(tasks)
            logger.debug(
                f"Добавлено {len(tasks)} задач из {type(source).__name__}")

        logger.info(
            f"Завершено: всего {len(all_tasks)} задач из {len(sources)} источников")
        return all_tasks
