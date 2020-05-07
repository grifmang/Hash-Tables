import math
import random
import time

def slowfun(x, y, cache = {}):
    # TODO: Modify to produce the same results, but much faster

    # Possibly make faster rewriting pow and factorial functions caching both

    ti = time.ctime()
    if ('pow', x, y) not in cache:
        cache[('pow', x, y)]= math.pow(x, y)
    v = cache[('pow', x, y)]
    if ('fact', v) not in cache:
        cache[('fact', v)] = math.factorial(v)
    v = cache[('fact', v)]
    v //= (x + y)
    v %= 982451653

    return v, ti


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
