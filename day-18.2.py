from turtle import Turtle, Screen
import random

kachua = Turtle()

kachua.shape("turtle")

#Drawing different shapes Tri, Sq, Penta, Hexa, Hecta, Octa, Nona and decagon.
colours = ["medium slate blue", "magenta", "plum", "black", "red", "silver", "maroon", "seagreen", "tomato", "lime", "yellow", "cornflower blue"]

def draw_shape(num_Sides):
    angle = 360/num_Sides
    for _ in range(num_Sides):
        kachua.forward(100)
        kachua.left(angle)
        
for shape_sides in range(3, 11):
    kachua.color(random.choice(colours))
    draw_shape(shape_sides)
    


parda = Screen()
parda.exitonclick()