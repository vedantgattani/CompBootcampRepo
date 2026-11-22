def buggyfunc(x):
    y = x
    for i in range(x):
        y = y-1
        if y == 0:
            breakpoint()
        z = x/y
    return z

buggyfunc(20)