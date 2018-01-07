import turtle

t = turtle.Turtle()
t.speed (0)

def square():
    for i in range (1, 7):
        for a in range (1, 5):
            t.forward(10 * i * 2)
            t.left(90)
        t.up()
        t.goto(-10 * i, -10 * i)
        t.down()
        
square()

