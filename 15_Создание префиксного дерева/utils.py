import functools
from typing import Any
from argparse import ArgumentTypeError


def arg_one_is_char(func: Any) -> Any:
    @functools.wraps(func)
    def wrapper(*args: list, **kwargs: list) -> None:
        if type(args[1]) is str and len(args[1]) > 1:
            raise ArgumentTypeError('Not a char!')
        result = func(*args, **kwargs)

        return result

    return wrapper
