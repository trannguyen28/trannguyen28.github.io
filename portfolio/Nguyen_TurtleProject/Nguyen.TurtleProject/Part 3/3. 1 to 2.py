import turtle

turtle.speed(0)

def square():
    x = 10
    for i in range (10):
        for i in range (0, 4):
            turtle.forward(x)
            turtle.left(90)
        x = x + 10
        
square()
