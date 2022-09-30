import turtle 
#1. import modules
import random
x = random.randrange(1,5)
y = random.randrange(1,5)
#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('white')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('red')
leonardo.color('purple')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-50,10)
leonardo.goto(-50,-10)

## 5. Your PART A code goes here
michelangelo.forward(random.randint(0,10))
leonardo.forward(random.randint(0,10))
michelangelo.goto(-10,5)
leonardo.goto(-10,-5)
for run in range(10):       
  michelangelo.forward(random.randint(0,5))
  leonardo.forward(random.randint(0,5))

michelangelo.goto(-10,5)
leonardo.goto(-10,-5)

window.exitonclick()

# PART B - complete part B here
import pygame
pygame.init()
window = pygame.display.set_mode()
import math

white = [255,255,255,255]
pink = [255, 20, 147, 255]
window.fill(white)

#triangle
coords=[]
num_sides=3
side_length=20
offset=100
for i in range(num_sides):
  theta= (2.0 * math.pi * i / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords_tri=(x,y)
  coords.append(coords_tri)
  
pygame.draw.polygon(window, pink, coords)
pygame.display.flip()
pygame.time.wait(500)
coords.clear()

#square
num_sides2=4
coords_2=[]
for i in range(num_sides2):
  theta= (2.0 * math.pi * i / num_sides2)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords_square=(x,y)
  coords.append(coords_square)

window.fill(white)
pygame.draw.polygon(window, pink, coords)
pygame.display.flip()
pygame.time.wait(1000)
coords.clear()

#hexagon
num_sideshex=6
coords_hex=[]
for i in range(num_sideshex):
  theta= (2.0 * math.pi * i / num_sideshex)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords_hex=(x,y)
  coords.append(coords_hex)

window.fill(white)
pygame.draw.polygon(window, pink, coords)
pygame.display.flip()
pygame.time.wait(1000)
coords.clear()

#nonagon
num_sidesnon=9
coords_non=[]
for i in range(num_sidesnon):
  theta= (2.0 * math.pi * i / num_sidesnon)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords_non=(x,y)
  coords.append(coords_non)

window.fill(white)
pygame.draw.polygon(window, pink, coords)
pygame.display.flip()
pygame.time.wait(1000)
coords.clear()

#circle
num_sidescirc=360
coords_circ=[]
for i in range(num_sidescirc):
  theta= (2.0 * math.pi * i / num_sidescirc)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords_circ=(x,y)
  coords.append(coords_circ)

window.fill(white)
pygame.draw.polygon(window, pink, coords)
pygame.display.flip()
pygame.time.wait(1000)
coords.clear()
