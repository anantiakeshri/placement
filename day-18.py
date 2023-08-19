import turtle as t
import random

kachua = t.Turtle()

''' you cannot use "kachua.colormode" because 'colormode' is a standard turtle graphics library in Python, 
    and the colormode method is not associated with the turtle object. '''
t.colormode(255)  

# Generating random colors 
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

## printing random patterns using turtle
kachua.speed(0)
kachua.pensize(10)
direction = [0, 90, 180, 270]

for _ in range(200):
    kachua.color(random_colour())
    kachua.forward(30)
    kachua.setheading(random.choice(direction))


#code by Anantia Keshri