def regular(function):
    def closure(*args):
        if len(args)>= function.__code__.co_argcount:
            return function(*args)
        return lambda x: closure(*args, x)

    return closure
def add(x,y,z):
    return x + y + z
iadd = regular(add)
res1 = iadd(1,2,3)
res2 = iadd(1)(2)(3)
res3 = iadd(1,2)(3)
print(res1,res2,res3)
