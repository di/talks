import sys

import afl

afl.init()

try:
    x, a, b, c = eval(sys.stdin.read())
    assert max(x) >= max(x[a:b:c])
except Exception as e:
    if isinstance(e, AssertionError):
        raise e
