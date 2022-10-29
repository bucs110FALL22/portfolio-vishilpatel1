# setting up
import turtle
t = turtle.Turtle() 
screen =turtle.Screen()
screen.bgcolor("blue")
print("input true if you want the accesory and nothing if you don't")
buttons = input("Do you want buttons\n")
hat = input("Do you want a hat\n")
eyes = input("Do you want eyes\n")
arms = input("Do you want arms\n")
nose = input("Do you want a nose\n")

#circle function
def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor (color)
    t.goto (x, y)
    t.pendown()
    t.begin_fill()
    t.circle (radius)
    t.end_fill()
  
# body
draw_circle ("#ffffff", 30, 0, -40)
draw_circle ("#ffffff", 40, 0, -100)
draw_circle ("#ffffff", 60, 0, -200)
  
# eyes
if eyes:
  draw_circle ("#ffffff", 2, -10, -10) 
  draw_circle ("#ffffff", 2, 10, -10) 
  
# nose
if nose:
  draw_circle ("#FF6600", 3, 0, -15)  
   
# Drawing buttons on
if buttons:
  draw_circle ("#ffffff", 2, 0, -35)
  draw_circle ("#ffffff", 2, 0, -45)
  draw_circle ("#ffffff", 2, 0, -55)
  
  
  
# Function to draw arms 
def create_line(x, y, length, angle):
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.forward(length)
    t.setheading(angle + 20)
    t.forward(20)
    t.penup()
    t.back(20)
    t.pendown()
    t.setheading(angle - 20)
    t.forward(20)
    t.penup()
    t.home()
     
  
      
# arms
if arms:
  create_line(-70, -50, 50, 160) 
  create_line(70, -50, 50, 20) 
  
  
  
# Drawing hat
if hat:
  t.penup()
  t.goto (-35, 8)
  t.color ("red")
  t.pensize (6)
  t.pendown()
  t.goto (35, 8)
  
  t.goto (30, 8)
  t.fillcolor ("red")
  t.begin_fill()
  t.left (90)
  t.forward (15)
  t.left (90)
  t.forward (60)
  t.left (90)
  t.forward (15)
  t.end_fill()
