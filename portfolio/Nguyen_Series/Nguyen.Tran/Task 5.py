print ('This is a list of the first n terms of the Fibonacci series.')
n = int(input('Please enter the value of n: '))

a = 0
b = 1
           
for i in range (1, n + 1):
    if (i == 1):
        c = 1
    else:
        c = a + b
        a = b
        b = c
    print(c)
