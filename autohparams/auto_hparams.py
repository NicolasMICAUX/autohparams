from inspect import isclass, isfunction, ismethod, ismodule
from typing import Dict


def _get_repr(x):
    if isinstance(x, (int, float, complex, bool, str)):  # any basic type
        return x
    _repr = str(x)
    if _repr.startswith("<"):
        return str(x.__class__).split(".")[-1].split("'")[0]
    else:
        return _repr


def get_auto_hparams(var_dict: Dict) -> Dict:
    """Returns a default config dictionnary from available variables at run time.

    Args:
        var_dict (dict): most often globals(). Use it as follows: `get_auto_config(globals())`

    Returns:
        dict: default config dict
    """
    return {
        name: _get_repr(val)
        for name, val in var_dict.items()
        if not (
            name.startswith("_")
            or isclass(val)
            or ismodule(val)
            or ismethod(val)
            or isfunction(val)
            or name in {"In", "Out", "exit", "quit"}
        )
    }
