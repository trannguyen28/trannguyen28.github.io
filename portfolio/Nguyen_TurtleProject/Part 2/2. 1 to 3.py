import turtle

print ('1 to 10: slowest to fast')
print ('0: fastest')

def square():
    s = int(input('Please enter the speed of the turtle from 0, 10: '))
    for i in range (0, 4):
        turtle.forward(100)
        turtle.left(90)
        turtle.speed(s)

square()


# 0 is the fastest, 1 is the slowest.
