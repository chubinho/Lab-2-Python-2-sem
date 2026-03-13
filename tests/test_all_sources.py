import json
import pytest
from src.sources.file_source import FileSource


class TestFileSource:

    def test_load_tasks_from_json(self, tmp_path):
        """Загружаем задачи из нормального JSON-файла"""
        test_file = tmp_path / "tasks.json"
        data = [
            {"id": "task_1", "payload": {"action": "test1"}},
            {"id": "task_2", "payload": {"action": "test2"}},
        ]
        test_file.write_text(json.dumps(data))

        source = FileSource(str(test_file))
        tasks = source.get_task()

        assert len(tasks) == 2
        assert tasks[0].id == "task_1"

    def test_invalid_json_content(self, tmp_path):
        """Тест на неправильный файл JSON"""
        test_file = tmp_path / "broken.json"
        test_file.write_text('{ this is not valid json }')

        source = FileSource(str(test_file))

        with pytest.raises(ValueError):
            source.get_task()

    def test_missing_payload_field(self, tmp_path):
        """Передача задачи без payload"""
        test_file = tmp_path / "missing.json"
        data = [{"id": "1"}]
        test_file.write_text(json.dumps(data))

        source = FileSource(str(test_file))

        with pytest.raises(KeyError):
            source.get_task()

    def test_file_not_exists(self):
        """Несуществующий файл"""
        source = FileSource("/nonexistent/path/file.json")

        with pytest.raises(ValueError):
            source.get_task()
