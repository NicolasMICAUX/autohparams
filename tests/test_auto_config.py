from unittest import TestCase

from autohparams.auto_hparams import get_auto_hparams


class MyClass:
    pass


x = 0
_y = 1


class Test(TestCase):
    def test_auto_hparams(self):
        assert get_auto_hparams(globals()) == {"x": 0}
