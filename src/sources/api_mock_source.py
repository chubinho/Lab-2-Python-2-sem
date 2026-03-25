import logging
from typing import Any
from src.task import Task

logger = logging.getLogger("task")


class APIMockSource:
    """
    Источник задач, имитирующий внешний API.
    
    Возвращает заранее определённый набор задач для тестирования.
    Все задачи создаются с валидацией через дескрипторы.
    """

    def __init__(self, tasks_data: list[dict[str, Any]] | None = None) -> None:
        """
        Инициализация API-заглушки.
        
        Args:
            tasks_data: Список словарей с данными задач (по умолчанию 3 задачи)
        """
        if tasks_data is None:
            self.tasks_data = [
                {
                    "id": 1,
                    "payload": {
                        "action": "send_email",
                        "user": "test@example.com",
                        "description": "Отправить email пользователю",
                        "status": "new",
                        "priority": 5
                    }
                },
                {
                    "id": 2,
                    "payload": {
                        "action": "calc_stats",
                        "date": "2025-03-08",
                        "description": "Рассчитать статистику за дату",
                        "status": "new",
                        "priority": 7
                    }
                },
                {
                    "id": 3,
                    "payload": {
                        "action": "log_message",
                        "text": "System started",
                        "description": "Записать сообщение в лог",
                        "status": "new",
                        "priority": 3
                    }
                },
            ]
            logger.debug(
                "APIMockSource инициализирован с данными по умолчанию")
        else:
            self.tasks_data = tasks_data
            logger.debug(
                f"APIMockSource инициализирован с {len(tasks_data)} кастомными задачами")

    def get_task(self) -> list[Task]:
        """
        Получение задач из API-заглушки.
        
        Returns:
            list[Task]: Список объектов Task
        
        Raises:
            KeyError: Если в данных отсутствуют обязательные поля
            ValueError: Если данные не проходят валидацию дескрипторов
        """
        tasks = []
        logger.info(f"Получение задач из API: {len(self.tasks_data)} записей")

        for task_data in self.tasks_data:
            task_id = task_data['id']
            payload = task_data['payload']
                

            task = Task(
                id=task_id,
                payload=payload
            )
            tasks.append(task)
            logger.debug(f"Создана задача: {task.id}")


        logger.info(f"Создано {len(tasks)} объектов Task из API")
        return tasks
