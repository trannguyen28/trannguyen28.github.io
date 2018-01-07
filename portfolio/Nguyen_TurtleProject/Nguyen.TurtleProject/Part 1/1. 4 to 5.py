import turtle

n = int(input('Please enter how many sides you want to make a regular polygon: '))

def AnyRegPly(n):
    d = 360/n
    s = 800/n
    for i in range (n):
        turtle.forward(s)
        turtle.left(d)
        
AnyRegPly(n)
    
# As the regular polygon has more sides, it looks more like a circle, but it will never be a circle. 

