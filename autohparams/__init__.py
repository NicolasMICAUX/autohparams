"""Returns a default config dictionnary from available variables at run time.

Args:
    var_dict (dict): most often globals(). Use it as follows: `get_auto_config(globals())`

Returns:
    dict: default config dict
"""
from sys import modules
from types import ModuleType

from .auto_hparams import get_auto_hparams

__all__ = ["get_auto_hparams"]


class CallableModule(ModuleType):
    """Inspired from https://stackoverflow.com/a/74604283"""

    def __init__(self):
        ModuleType.__init__(self, __name__)
        self.__dict__.update(modules[__name__].__dict__)

    def __call__(self, *args, **kwargs):
        get_auto_hparams(*args, **kwargs)

    mod_call = __call__
    __all__ = list(set(vars().keys()) - {"__qualname__"})


modules[__name__] = CallableModule()
