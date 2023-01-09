class MetaSingleton(type):
    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)

        return cls.instance


class CheckSingletonMeta(metaclass=MetaSingleton):
    pass


t_obj = CheckSingletonMeta()
t_obj_1 = CheckSingletonMeta()
print(t_obj is t_obj_1)
