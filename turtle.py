#Veeru Senthil
import turtle as t 


#Sets up the screen, turtle speed, and color.
t.initializeTurtle(initial_speed=5) 
t.color('blue') 

#Instructs turtle to draw square with for loop
for w in range(4):
    t.forward(100)
    t.left(90)


#Instructs turtle to draw star with for loop
for i in range (5):
  t.forward(200)
  t.right(144)

#Turtle functiom

def turtleShape(sides):

  angle_meas = (sides-2)*180
  angle_meas = angle_meas / sides

  while sides:
    t.color('green')
    t.right (angle_meas)
    t.forward (100)


shape = int(input('How many sides does your shape have?'))
turtleShape(shape)





