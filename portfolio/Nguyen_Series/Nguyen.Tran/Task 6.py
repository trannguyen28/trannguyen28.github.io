print ('This is a list of the first n terms of a series.')
n = int(input('Please enter the value of n: '))

a = 1
for i in range (1, n + 1):
    if i == 1:
        a = 1
    else:
        a = a * 3
    print (a)
