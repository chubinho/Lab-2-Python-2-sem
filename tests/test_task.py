from src.task import Task
from src.exceptions import ValidationError
import pytest


class TestTask:

    def test_task_attributes(self):
        """Проверка создания задачи"""
        task = Task(id=12345, payload={
                    "test": "the best", "description": "Тест", "priority": 5})
        assert task.id == 12345
        assert task.payload == {"test": "the best",
                                "description": "Тест", "priority": 5}

    def test_task_with_complex_payload(self):
        """Проверка задачи со сложным payload"""
        payload = {
            "dict": {"key": "value"},
            "list": [1, 2, 3, 5, 151, 51],
            "bool": True,
            "priority": 5,
            "description": "Тест"
        }
        task = Task(id=999, payload=payload)

        assert len(task.payload["list"]) == 6
        assert task.payload['list'][0] == 1
        assert task.id == 999
        assert task.payload["dict"]["key"] == "value"
        
    def test_task_invalid_id_type(self):
        """ID должен быть только целым числом"""
        with pytest.raises(ValidationError, match="Id должен быть целый"):
            Task(id="abc", payload={"description": "Test", "priority": 5})

    def test_task_priority_boundaries(self):
        """Проверка допустимых границ приоритета"""
        t1 = Task(id=1, payload={"description": "Low", "priority": 1})
        t2 = Task(id=2, payload={"description": "High", "priority": 10})
        assert t1.priority == 1
        assert t2.priority == 10


    def test_task_priority_out_of_range(self):
        """Приоритет вне диапазона 1-10 должен вызывать ошибку"""
        with pytest.raises(ValidationError):
            Task(id=1, payload={"description": "Error", "priority": 11})
        with pytest.raises(ValidationError):
            Task(id=1, payload={"description": "Error", "priority": 0})

    def test_data_vs_nondata_priority(self):
        """
        Демонстрация разницы в приоритетах:
        Data Descriptor > __dict__ > Non-Data Descriptor
        """
        payload = {"description": "Учить дескрипторы", "priority": 5}
        task = Task(id=1, payload=payload)
        task.__dict__['priority'] = 999

        assert task.priority == 5
        assert task.priority != 999
    
        assert task.task_type == "GeneralTask"

        task.__dict__['task_type'] = "SuperUrgentTask"

        assert task.task_type == "SuperUrgentTask"
        assert task.task_type != "GeneralTask"
