from turtle import *
import random, math

DART_POS = []
PI = math.pi
Radi = 120

def venn_diagram():
    #function to create venn diagrams

    colors = ['red','blue','green']
    diagram = Turtle()
    diagram.speed('fast')

    diagram.color(colors[0])
    diagram.begin_fill()
    diagram.penup()
    diagram.back(210)
    diagram.left(90)
    diagram.pendown()
    diagram.circle(-120)

    diagram.right(90)
    diagram.penup()
    diagram.home()

    diagram.color(colors[1])
    diagram.forward(90)
    diagram.forward(120)
    diagram.left(90)
    diagram.pendown()
    diagram.circle(120)


    diagram.right(90)
    diagram.penup()
    diagram.home()

    diagram.color(colors[2])
    diagram.left(90)
    diagram.forward(150)
    diagram.forward(120)
    diagram.right(90)
    diagram.pendown()
    diagram.circle(-120)
    diagram.penup()

    diagram.hideturtle()

def generate_dart():
    dart = Turtle()
    dart.penup()

    #generating random coordinates for the dart
    xcoor = random.randint(-300, 300)
    ycoor = random.randint(-300, 300)

    #append x,y coordinates too Global Variable
    DART_POS.append(xcoor)
    DART_POS.append(ycoor)

    dart.goto(xcoor,ycoor)
    dart.pendown()
    dart.dot(10, 'purple')

def evaluateDartPosition():
    """function evaluates where the dart lands, and based on where
    it lands returns to the user the amount of points gained"""

    if ((x - red_center[0]) ** 2 + (y - red_center[1]) ** 2 < Radi ** 2) and ((x - blue_center[0]) ** 2 + (y - blue_center[1]) ** 2 < Radi ** 2) and ((x - green_center[0]) ** 2 + (y - green_center[1]) ** 2 < Radi ** 2):
        tr.write("1000 Points!\nDart has landed in all three circles")
    elif (((x - red_center[0]) ** 2 + (y - red_center[1]) ** 2 < Radi ** 2) and (
                (x - blue_center[0]) ** 2 + (y - blue_center[1]) ** 2 < Radi ** 2)):
        tr.write("500 Points!\nDart landed in two circles")
    elif (((x - red_center[0]) ** 2 + (y - red_center[1]) ** 2 < Radi ** 2) and ((x - green_center[0]) ** 2 + (y - green_center[1]) ** 2 < Radi ** 2)):
        tr.write("500 Points!\nDart landed in two circles")
    elif (((x - blue_center[0]) ** 2 + (y - blue_center[1]) ** 2 < Radi ** 2) and (
                (x - green_center[0]) ** 2 + (y - green_center[1]) ** 2 < Radi ** 2)):
        tr.write("500 Points!\nDart landed in two circles")
    elif ((x - blue_center[0]) ** 2 + (y - blue_center[1]) ** 2 < Radi ** 2):
        tr.write("100 Points!\nDart landed in one circle")
    elif ((x - red_center[0]) ** 2 + (y - red_center[1]) ** 2 < Radi ** 2):
        tr.write("100 Points!\nDart landed in one circle")
    elif ((x - green_center[0]) ** 2 + (y - green_center[1]) ** 2 < Radi ** 2):
        tr.write("100 Points!\nDart landed in one circle")
    else:
        tr.write("0 Points, Sorry ... \nDart landed outside all circles")



if __name__ == '__main__':
   window = Screen()
   tr = Turtle()
   tr.hideturtle()

   #create venn diagram
   venn_diagram()

   #generate dart
   generate_dart()

   #dart coordinates
   x = DART_POS[0]
   y = DART_POS[1]

   #centers of each circle
   red_center = [-90, 0]
   blue_center = [90, 0]
   green_center = [0, 150]

   tr.penup()
   tr.goto(0, -150)
   tr.pendown()

   #Evaluate the position of the dart to see how many points gained
   evaluateDartPosition()



   window.mainloop()