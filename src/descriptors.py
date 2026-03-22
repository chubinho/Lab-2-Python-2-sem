class IdDescriptor:
    def __set_name__(self, owner, name):
        self.id = '_' + id

    def __set__(self, obj, value):
        if not isinstance(id, int):
            raise TypeError("Id должен быть целый")
        if id < 1:
            raise ValueError("Id это целое число > 0")
        setattr(obj, self.id, value)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.id, None)
