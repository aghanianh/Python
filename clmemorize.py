def memorize(function):
    cache = {}  #(3,4) -> 7
    def foo(*args):
        if args in cache:
            return cache[args]
        result = function(*args)
        cache[args] = result
        return result
    return foo


def add(a,b):
    return a + b
mem = memorize(add)
mem(3,4)
mem(5,6)
mem(6,7)
mem(7,8)
mem(8,9)
print(mem.__closure__[0].cell_contents)
