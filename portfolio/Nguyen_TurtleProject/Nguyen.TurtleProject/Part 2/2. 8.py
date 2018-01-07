import turtle

n = int(input('Please enter how many sides you want to make a regular polygon: '))

window = turtle.Screen()
t = turtle.Turtle()
window.colormode(255)
window.bgcolor(255, 255, 255)
t.speed (1)

def AnyRegPly(n):
    d = 360/n
    s = 800/n
    for i in range (n):
        t.color(255, 0, 0)
        t.shapetransform(10, 11, 12, 13)
        t.stamp()
        t.forward(s)
        t.left(d)
                 
AnyRegPly(n)


