# coding=utf-8


class Flex:
    def __getattr__(self, item):
        if item in dir(self):
            return getattr(self, item)
        return Flex()

    def __call__(self, *args, **kwargs):
        return Flex()


class Task:
    """Descriptor for keeping a potential logger object.

    If it is asigned to an attribiute of a class (let say `logger`),
    then we can call any method on this atribute wihout cousing any operation.
    But if we assigne an object to the `logger` attribute,
    then geting the `logger` will reutrn the asigned reference.

    Examples:
    >>> class Logger:
    ...     def log(self, msg): print(msg)
    >>> class MyClass:
    ...     logger = Task()
    >>> obj = MyClass()
    >>> obj.logger.any_method()     # logger isn't assigned yet
    >>> obj.logger = Logger()
    >>> obj.logger.log("msg")
    msg
    >>> obj.logger.any_method()
    Traceback (most recent call last):
     ...
    AttributeError: 'Logger' object has no attribute 'any_method'
    """
    def __get__(self, obj, objtype=None):
        value = getattr(obj, '_logger', None)
        if value is None:
            return Flex()
        return value

    def __set__(self, obj, value):
        obj._logger = value
