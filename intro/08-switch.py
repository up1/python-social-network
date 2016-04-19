# no switch in python but you can do something like switch with dict and function
def switch(x):
    cases = {
            "a": 1,
            "b": 2,
            "c": 3,
            }

    if cases.has_key(x):
        return cases[x]
    else:
        return 0 # default value


print switch("a") # 1
print switch("b") # 2
print switch("c") # 3
print switch("d") # 0
