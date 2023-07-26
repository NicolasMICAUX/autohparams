from unittest import TestCase

from autoconfig.auto_config import get_auto_config


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


x = 0
_y = 1


class Test(TestCase):
    def test_auto_config(self):
        assert get_auto_config(globals()) == {"x": 0}
