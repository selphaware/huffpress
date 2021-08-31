from huffpress.compress import compress_string
from huffpress.decompress import decompress_bytes


def comp(fun):
    def decorator(*args, **kwargs):
        ret = fun(*args, **kwargs)
        com_ret = compress_string(ret)
        return com_ret
    return decorator


def decomp(*str_vars):
    def inner(fun):
        def decorator(*args, **kwargs):
            new_kwargs = {}
            for k, v in kwargs.items():
                decomp_bytes = decompress_bytes(v) if k in str_vars else v
                new_kwargs[k] = "".join(map(chr, list(decomp_bytes)))
            return fun(*args, **new_kwargs)
        return decorator
    return inner
