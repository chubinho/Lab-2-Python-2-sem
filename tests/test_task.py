from src.task import Task


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
        
