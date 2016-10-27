class SingletonMetaClass(type):
    def __init__(cls, name, bases, dict):
        super(SingletonMetaClass, cls).__init__(name, bases, dict)
        original_new = cls.__new__

        def my_new(_cls, *args, **kwargs):
            if _cls.instance is None:
                _cls.instance = original_new(_cls, *args, **kwargs)
            return _cls.instance

        cls.instance = None
        cls.__new__ = staticmethod(my_new)
