import logging
from dataclasses import dataclass
import random
from src.task import Task

logger = logging.getLogger("task")


@dataclass
class GeneratorConfig:
    """
    Конфигурация для GeneratorSource
    
    Атрибуты:
        count: Количество задач для генерации (по умолчанию 5)
        prefix: Префикс для идентификаторов задач (по умолчанию "task_")
        seed: Seed для генератора случайных чисел (None = без фиксации)
        random_priority: Если True, приоритет генерируется случайно (1-10)
    """
    count: int = 5
    prefix: str = "task_"
    seed: int | None = None
    random_priority: bool = True

    def __post_init__(self) -> None:
        """
        Валидация атрибутов после инициализации
        """
        if not isinstance(self.count, int):
            logger.error(
                f"Некорректный тип count: {type(self.count).__name__}")
            raise ValueError("Количество задач должно быть целым числом")
        if self.count < 0:
            logger.error(f"Отрицательное значение count: {self.count}")
            raise ValueError("Количество задач не может быть отрицательным")
        logger.debug(
            f"GeneratorConfig создан: count={self.count}, prefix={self.prefix}")


class GeneratorSource:
    """
    Источник задач, генерирующий задачи программно
    """

    def __init__(self, config: GeneratorConfig | None = None) -> None:
        self.config = config if config is not None else GeneratorConfig()
        logger.debug(
            f"GeneratorSource инициализирован с конфигом: count={self.config.count}")

    @classmethod
    def for_test(cls, count: int = 3) -> 'GeneratorSource':
        """
        Args:
            count: Количество задач для генерации
            
        Returns:
            GeneratorSource: Настроенный генератор для тестов
        """
        logger.debug(f"Создание генератора для тестов: count={count}")
        config = GeneratorConfig(count=count, seed=52, random_priority=False)
        return cls(config)

    def get_task(self) -> list[Task]:
        """
        Сгенерировать задачи 
        
        Returns:
            list[Task]: Список объектов Task
        """
        logger.info(
            f"Генерация {self.config.count} задач с префиксом '{self.config.prefix}'")
        if self.config.seed is not None:
            random.seed(self.config.seed)
            logger.debug(f"Seed установлен: {self.config.seed}")

        tasks = []

        for i in range(1, self.config.count + 1):
            if self.config.random_priority:
                priority = random.randint(1, 10)
            else:
                priority = 5

            logger.debug(f"Генерация задачи {i}: id={i}, priority={priority}")

            task = Task(
                id=i,
                payload={
                    "generated": True,
                    "index": i,
                    "source": "GeneratorSource",
                    "priority": priority,
                    "description": f"{self.config.prefix}Сгенерированная задача #{i}",
                    "status": "new" 
                }
            )
            tasks.append(task)

        logger.info(f"Сгенерировано {len(tasks)} задач")
        return tasks
