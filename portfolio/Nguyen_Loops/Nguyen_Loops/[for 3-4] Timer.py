import time

t = int(input('Please enter an integer: '))

def countdown(t):
    print (t)
    for i in range (0, t):
        time.sleep(1)
        t = t - 1
        print (t)
    if t == 0:
        print ('Timer done!')

countdown(t)
