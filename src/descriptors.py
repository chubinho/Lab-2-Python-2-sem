class IdDescriptor:
    """
    Data Descriptor для валидации идентификатора задачи
    """

    def __set_name__(self, owner: type, name: str) -> None:
        """
        Сохраняет имя атрибута.
        Вызывается автоматически при создании класса-владельца
        """
        self.id = '_' + id

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
        if not isinstance(id, int):
            raise TypeError("Id должен быть целый")
        if id < 1:
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

    def __set_name__(self, owner: type, name: str) -> None:
        """
        Вызывается автоматически при создании класса

        Args:
            owner: Класс-владелец дескриптора
            name: Имя атрибута в классе
        """
        self.priority = '_' + name

    def __set__(self, instance: object, value: int) -> None:
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
        setattr(instance, self.priority, value)

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
