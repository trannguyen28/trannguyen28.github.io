import turtle

n = int(input('Please enter how many sides you want to make a regular polygon: '))
t = turtle.Turtle()
t.speed(0)

def AnyRegPly(n):
    s = 100/n
    r = s
    d = 360/n
    for i in range (1, 10):
        s = r * i
        t.up()
        t.goto(0, 0)
        t.left((180-d)/2)
        t.right(180)
        t.forward((s**2 + (s**2/4))**(1/2))
        t.left(180-((180-d)/2))
        t.down()
        for a in range (1, n + 1):
            t.forward(s)
            t.left(d)           

AnyRegPly(n)




