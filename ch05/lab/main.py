import pygame
iters = {}
n = 15
upper_limit = 50
max_so_far = 0
num_so_far = 0


def func(n):
 count = 0
 while n != 1:
   if n % 2 == 0:
     n = n / 2    
     count = count + 1
   else:
     n = 3*n+1
     count = count + 1   
 return(count)


for i in range(2, upper_limit + 1):
 iters[i] = func(i)

print(iters)


max_value = 0
max_value_so_far = 0
blue = [220, 220, 220]
purple = [0, 220, 0]
orange = [220, 220, 0]
scale = 15
display = pygame.display.set_mode()


pygame.font.init()
iters2 = []

for j in range(2, upper_limit + 1):
  iters2 +=[(j*scale, func(j)*scale)]
  if max_value_so_far < func(j):
    max_value = j
    max_value_so_far = func(j)
 
print(max_value_so_far) 

new_display = pygame.Surface(display.get_size())
if len(iters2) >= 2:
  pygame.draw.lines(new_display, purple, False, iters2)
new_display = pygame.transform.flip(new_display, False, True)
display.blit(new_display, (0, 0))
pygame.display.update()
font = pygame.font.Font(None, 20)
msg = font.render("Max so far:"+str(max_value_so_far), True, orange)
display.blit(msg, (0, 0))
pygame.display.update()
pygame.time.wait(1000)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      