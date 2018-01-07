import math

x = float(input('Please enter a value in degrees to evaluate its cosine: '))

def series(x):
    a = 0
    for n in range (50):
        y =((-1)**n)*(x**(2*n))/math.factorial(2*n)
        a = a + y
    return a

def deg_rad(x):
    rad = x * math.pi / 180
    return rad

print ('The cosine of ' + str(x) + ' degrees is: ')
x = deg_rad(x)
print (str(series(x)))
