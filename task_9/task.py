# coding=utf-8


class Task(Exception):
    """Exception class with the messages: "whars ma mone dude?"""
    def __init__(self, *args, **kwargs):
        super().__init__('whars ma mone dude?')
