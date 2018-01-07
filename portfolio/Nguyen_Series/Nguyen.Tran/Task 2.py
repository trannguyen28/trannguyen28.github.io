import math

print ('Please enter a value in radians to evaluate its cosine: ')
x = float(input())

def series(x):
    a = 0
    for n in range (50):
        y =((-1)**n)*(x**(2*n))/math.factorial(2*n)
        a = a + y
    return a

print ('The cosine of ' + str(x) + ' radians is: ' + str(series(x)))
