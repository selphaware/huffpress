"""
    (c) 2021 Usman Ahmad https://github.com/selphaware

    decorators.py

    Contains decorators for compressing and decompressing variable objects

    e.g.

    # Function below with @comp decorator returns the compressed
    # byterray of "Hello world"
    @comp
    def some_fn():
        return "Hello world"


    # Function below decompresses contents of var2 first before proceeding
    # with the rest of the function
    @decomp("var2")
    def some_fn2(var1, var2):
        ...
"""

from huffpress.press.compress import compress_string
from huffpress.press.decompress import decompress_bytes


def comp(fun):
    """
    Compression decorator, which compresses final string result

    :param fun: Function to be decorated
    :return: decorator function
    """
    def decorator(*args, **kwargs) -> bytearray:
        """
        Compresses final result before returning

        :param args: Original list args
        :param kwargs: Original dict args
        :return: Compressed string in bytearray format
        """
        ret = fun(*args, **kwargs)
        com_ret: bytearray = compress_string(ret)
        return com_ret
    return decorator


def decomp(*bytearray_vars):
    """
    Decompression decorator, which first decompresses given bytearray variable
    objects before proceeding with the rest of the function

    :param bytearray_vars: Bytearray variables to decompress first
    :return: decorator function
    """
    def inner(fun):
        """
        Inner decorator for decompression
        :param fun: Function to decorate
        :return: inner decorator function
        """
        def decorator(*args, **kwargs):
            """
            Decompress bytearray input variables first before proceeding

            :param args: Original list args
            :param kwargs: Original dict args
            :return: usual returning from fun
            """
            new_kwargs = {}
            for k, v in kwargs.items():
                decomp_bytes = decompress_bytes(v) if k in bytearray_vars else v
                new_kwargs[k] = "".join(map(chr, list(decomp_bytes)))
            return fun(*args, **new_kwargs)
        return decorator
    return inner
