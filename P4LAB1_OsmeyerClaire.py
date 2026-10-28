# P4LAB1_OsmeyerClaire.py
# Claire Osmeyer
#P4 Lab1
#use turtle and loops to draw a square and a triangle 

# Import the library 
import turtle

# create the turtle window and drawing object
win = turtle.Screen()
win.bgcolor("cyan")
pen = turtle.Turtle()

# set turtle options
pen.pensize(5) 
pen.pencolor("red")
pen.shape("turtle")

#code to draw a shapes
pen.fillcolor("yellow")
pen.begin_fill()

for side in range(6):
    pen.forward(100)
    pen.left(90)

    if side == 3:
        pen.end_fill()



# While loop that excutes 3 times
pen.fillcolor("black")
pen.begin_fill()

sides = 3
while sides > 0:
    pen.forward(100)
    pen.right(120)
    sides = sides - 1

pen.end_fill()

# wait for user to close window
win.mainloop()


