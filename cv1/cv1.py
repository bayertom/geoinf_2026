from math import *


def quadratic (a, b, c):
    #Discriminant
    D = b**2 - 4*a*c 

    #D > 0
    if D > 0:
        x_1 = (-b+sqrt(D))/(2*a)
        x_2 = (-b-sqrt(D))/(2*a)

    #D = 0
    elif D == 0:
        x_1 = -b/(2*a)
        x_2 = x_1

    #D < 0
    else:
        x_1=nan
        x_2=nan
    
    return x_1, x_2


a = 4
b = 6
c = 1

x_1, x_2 = quadratic(a, b, c)

print(x_1, x_2)