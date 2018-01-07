import turtle

window = turtle.Screen()
window.colormode(255)
window.bgcolor(222, 222, 222)
turtle.speed (5)
# turtle.color(255, 255, 255): white
# turtle.color(255, 0, 0): red
# turtle.color(0, 0, 0): black

def square():
    r = 255
    g = 0
    b = 0
    for i in range (4):
        turtle.color(r, g, b)
        r = r - 50
        g = g + 30
        b = b + 50
        turtle.forward(300)
        turtle.left(90)

square()


