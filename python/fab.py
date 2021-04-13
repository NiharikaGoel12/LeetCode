def fact1():
    print("cal fact of 1 ")
    x = 1
    print("done cal fact of 1 ")
    return x

def fact2():
    print("cal fact of 2 ")
    x = 2 * fact1()
    print("done cal fact of 2 ")
    return x


def fact3():
    print("cal fact of 3 ")
    x = 3 * fact2()
    print("done cal fact of 3 ")
    return x


def fact4():
    print("cal fact of 4 ")
    x = 4 * fact3()
    print("done cal fact of 4 ")
    return x

def fact5():
    print("cal fact of 5 ")
    x = 2 * fact4()
    print("done cal fact of 5 ")
    return x

def fact(val):
    print("recur cal fact of {} ".format(val))
    if val==1:
        print("done recur cal fact of {} ".format(val))
        return 1
    x =  val * fact(val-1)
    print("done recur cal fact of {} ".format(val))
    return x

print(fact(val=5))
print(fact5())