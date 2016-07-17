import sys

import afl

afl.init()

try:
    x, y = eval(sys.stdin.read())
    assert min(x, y) == min(y, x)
except Exception as e:
    if isinstance(e, AssertionError):
        raise e
