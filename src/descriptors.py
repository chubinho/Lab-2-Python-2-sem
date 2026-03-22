class IdDescriptor:
    """
    Data Descriptor для валидации идентификатора задачи
    """

    def __set_name__(self, owner: type, name: str) -> None:
        """
        Сохраняет имя атрибута.
        Вызывается автоматически при создании класса-владельца
        """
        self.id = '_' + name

    def __set__(self, obj: object, value: int) -> None:
        """
        Устанавливает значение ID с валидацией
        Args:
            obj: Экземпляр объекта
            value: Значение ID
        Raises:
            TypeError: Если значение не целое число
            ValueError: Если значение <= 0
        """
        if not isinstance(value, int):
            raise TypeError("Id должен быть целый")
        if value < 1:
            raise ValueError("Id это целое число > 0")
        setattr(obj, self.id, value)

    def __get__(self, obj: object, owner: type = None) -> int | None:
        """
        Возвращает значение ID
        Args:
            obj: Экземпляр объекта 
            objtype: Класс-владелец
        Returns:
            Значение ID или сам дескриптор
        """
        if obj is None:
            return self
        return getattr(obj, self.id, None)


class PriorityDescriptor:
    """
    Data Descriptor для валидации приоритета задачи.
    """

    def __set_name__(self, name: str, owner: type, ) -> None:
        """
        Сохраняет имя атрибута.
        Вызывается автоматически при создании класса

        Args:
            owner: Класс-владелец дескриптора
            name: Имя атрибута в классе
        """
        self.priority = '_' + name

    def __set__(self, obj: object, value: int) -> None:
        """
        Устанавливает значение приоритета с валидацией

        Args:
            instance: Экземпляр объекта
            value: Значение приоритета

        Raises:
            TypeError: Если значение не целое число
            ValueError: Если значение вне диапазона 1-10
        """
        if not isinstance(value, int):
            raise TypeError("Priority должен быть целым числом(от 1 до 10)")
        if not (1 <= value <= 10):
            raise ValueError("Priority должен быть в диапазоне от 1 до 10")
        setattr(obj, self.priority, value)

    def __get__(self, obj: object, owner: type = None) -> int | None:
        """
        Возвращает значение приоритета
        Args:
            obj: Экземпляр объекта 
            owner: Класс-владелец
        Returns:
            Значение приоритета или сам дескриптор (при обращении через класс)
        """
        if obj is None:
            return self
        return getattr(obj, self.priority, None)


class StatusDescriptor:
    def __set_name__(self, name: str, owner: type) -> None:
        """
        Сохраняет имя атрибута.
        Вызывается автоматически при создании класса-владельца.
        Args:
            owner: Класс-владелец дескриптора
            name: Имя атрибута в классе
        """
        self.status = '_' + name

    def __set__(self, obj: object, value: str) -> None:
        """
        Устанавливает значение статуса с валидацией
        Args:
            obj: Экземпляр объекта
            value: Значение статуса
        Raises:
            TypeError: Если значение не строка
            ValueError: Если статус не входит в список допустимых
        """
        if not isinstance(value, str):
            raise TypeError("Status должен быть строкой")
        if value not in ["in_progress", "done", "cancelled", "paused", "new"]:
            raise ValueError(f"Статус {value} недопустим")
        setattr(obj, self.status, value)

    def __get__(self, obj: object, owner: type = None) -> str | None:
        """
        Возвращает значение статуса
        Args:
            obj: Экземпляр объекта 
            objtype: Класс-владелец
        Returns:
            Значение статуса или сам дескриптор
        """
        if obj is None:
            return self
        return getattr(obj, self.status, None)