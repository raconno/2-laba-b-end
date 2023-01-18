def outer():
    # global x
    x = 1

    def inner():
        nonlocal x   # <- should be highlighted as Unbound
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)


outer()
