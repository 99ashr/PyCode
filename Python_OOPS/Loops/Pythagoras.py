def pythagoras():
    """This method is defined to calculate the pythagoras of the given 3 numbers"""
    pl = []
    range_ = int(input(
        "Enter the range up to which you want to find the combination of the pythagoras numbers: "))
    for a in range(1, range_+1):
        for b in range(a, range_+1):
            for c in range(b, range_+1):
                if a**2+b**2 == c**2:
                    pl.append([a, b, c])
                elif b**2+c**2 == a**2:
                    pl.append([a, b, c])
                elif c**2+a**2 == b**2:
                    pl.append([a, b, c])
    return pl


print(pythagoras())
