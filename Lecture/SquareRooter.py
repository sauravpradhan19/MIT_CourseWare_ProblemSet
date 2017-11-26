# code for square root
def rootFinder(a,x):
    if a*a>= x - 10E-4 and a*a<= x+ 10E-4:
        return a
    elif a*a>x:
        return rootFinder((a-x/a)/2,x)
    else:
        return rootFinder((a+x/a)/2,x)