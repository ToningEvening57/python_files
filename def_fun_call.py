def isDivisible(x, y):
    if x % y:
        return true
    else:
        return false

def isDivisible2(x, y):
    if x % y:
        print(True)
    else:
        print(False)


is1 = isDivisible(float(input()), float(input()))
is2 = isDivisible2(float(input()), float(input()))
