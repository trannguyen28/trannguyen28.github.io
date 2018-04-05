import time

t = int(input('Please enter an integer: '))

def countdown(t):
    print (t)
    while t > 0:
        time.sleep(1)
        t = t - 1
        print (t)
    if t == 0:
        print ('Timer done!')

countdown(t)
