import turtle

def square():
    for i in range (0, 4):
        turtle.forward(100)
        turtle.left(90)

def triangle():
    for i in range (0, 3):
        turtle.forward(100)
        turtle.left(120)

def pentagon():
    for i in range (0, 5):
        turtle.forward(100)
        turtle.left(72)

def hexagon():
    for i in range (0, 6):
        turtle.forward(100)
        turtle.left(60)

def nonagon():
    for i in range (0, 9):
        turtle.forward(80)
        turtle.left(40)

def decagon():
    for i in range (0, 10):
        turtle.forward(80)
        turtle.left(36)

print ('This turtle can draw: ')
print ('An Equlateral Triangle (3)')
print ('A Square (4)')
print ('A Regular Pentagon (5)')
print ('A Regular Hexagon (6)')
print ('A Regular Nonagon (9)')
print ('A Regular Decagon (10)')
x = input ('Please choose which shape you want the turtle to draw by entering the number inside the parentheses: ')
if x == '3':
    triangle()
elif x == '4':
    square()
elif x == '5':
    pentagon()
elif x == '6':
    hexagon()
elif x == '9':
    nonagon()
elif x == '10':
    decagon()
