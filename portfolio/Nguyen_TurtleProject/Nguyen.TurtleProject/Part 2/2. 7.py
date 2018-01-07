import turtle

n = int(input('Please enter how many sides you want to make a regular polygon: '))

window = turtle.Screen()
window.colormode(255)
window.bgcolor(255, 255, 255)
t = turtle.Turtle()
t.speed (0)

def AnyRegPly(n):
    d = 360/n
    s = 800/n
    r = 255
    g = 0
    b = 0
    for i in range (n):
        t.forward(s)
        t.left(d)
        t.color(r, g, b)
        r = r - 50
        g = g + 30
        b = b + 50  
        if r < 0:
            r = 255
            AnyRegPly(n)
        elif g > 255:
            g = 0
            AnyRegPly(n)
        elif b > 255:
            b = 0
            AnyRegPly(n)

AnyRegPly(n)

