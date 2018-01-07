def function(x):
    y = x**2 + 3*x + 1
    return y

sum = 0
for i in range (2,6):
    print (function(i))
    if i in range (2,5):
        print ('+')
    else:
        print ('=')
    sum = sum + function(i)
print (sum)
