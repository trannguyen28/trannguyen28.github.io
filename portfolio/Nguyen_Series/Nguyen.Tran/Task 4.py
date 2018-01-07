import math

def series(x):
    a = 0
    for n in range (50):
        y =((-1)**n)*(x**(2*n))/math.factorial(2*n)
        a = a + y
    return a

def deg_rad(x):
    rad = x * math.pi / 180
    return rad

choice = input('Would you like to use Radians (rad) or Degrees (deg) to evaluate cosine? ')
choice = choice.lower()

if choice == 'rad':
    x = float(input('Please enter a value in Radians: '))
    print ('The cosine of ' + str(x) + ' radians is: ')
    print (str(series(x)))
elif choice == 'deg':
    x = float(input('Please enter a value in Degrees: '))
    print ('The cosine of ' + str(x) + ' degrees is: ')
    x = deg_rad(x)
    print (str(series(x)))



