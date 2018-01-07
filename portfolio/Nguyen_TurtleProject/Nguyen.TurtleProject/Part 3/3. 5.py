import turtle

n = int(input('Please enter how many sides you want to make a regular polygon: '))
turtle.speed(0)

def AnyRegPly(n):
    s = 100/n
    for i in range (0, 5):
        d = 360/n
        for i in range (n):
            turtle.forward(s)
            turtle.left(d)
        s = s + 10
    
AnyRegPly(n)
    


