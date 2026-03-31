from dataclasses import dataclass
from typing import Any
from datetime import datetime
from src.descriptors import (
    IdDescriptor,
    DescriptionDescriptor,
    PriorityDescriptor,
    StatusDescriptor,
    ReadOnlyDescriptor,
    TaskTypeDescriptor,
    ValidationError)


@dataclass
class Task:
    id = IdDescriptor()
    description = DescriptionDescriptor()
    priority = PriorityDescriptor()
    status = StatusDescriptor()
    created_at = ReadOnlyDescriptor()

    task_type = TaskTypeDescriptor()

    def __init__(self, id: int, payload: dict[str, Any]) -> None:
        """
        Данные из payload распределяются по атрибутам с валидацией
        через дескрипторы.

        Args:
            task_id: Идентификатор задачи
            payload: Словарь с данными задачи (description, priority, status)

        Raises:
            ValidationError: Если данные в payload не проходят валидацию
        """
        if not payload:
            raise ValidationError("Payload не может быть пустым")
        
        self.id = id
        self.payload = payload
        self.description = payload.get("description", "task")
        self.priority = payload.get("priority", 10)
        self.status = payload.get("status", "new")
        self.created_at = datetime.now()

    @property
    def is_ready(self) -> bool:
        """
        Проверяет готовность задачи к выполнению
        Returns:
            bool: True если задача готова, False иначе
        """
        return bool(self.description and self.priority > 0)

    def __repr__(self) -> str:
        """
        Returns:
            str: Строковое представление для отладки
        """
        return (
            f"Task(id={self.id}, priority={self.priority}, "
            f"status='{self.status}', is_ready={self.is_ready})"
        )
