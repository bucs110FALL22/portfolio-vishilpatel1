import math
import pygame
import random

pygame.init()

Witdth = 400
Height = 400
Blue = [255, 0, 0]
Red = [0, 0, 255]
Black = [0, 0, 0]
Green = [173, 216, 230]
Pink = [255, 140, 105]


screen = pygame.display.set_mode([Height, Witdth])

# Choose which player will win
red_button_box = pygame.Rect(0, Height / 4, Height / 2, Witdth / 2)
blue_button_box = pygame.Rect(0, 0, Height / 2, Witdth / 2)
blue_button_box.topleft = red_button_box.topright
red_button = pygame.draw.rect(screen, Red, red_button_box)
blue_button = pygame.draw.rect(screen, Blue, blue_button_box)
pygame.display.flip()

guess = 0
print(
    "Please select the player who you think will win by clicking on the player color."
)
while guess == 0:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            if red_button_box.collidepoint(mouse_click_pos):
                guess = 1
            if blue_button_box.collidepoint(mouse_click_pos):
                guess = 2

# Set up board
screen.fill(Green)
pygame.draw.circle(screen, Pink, (Height / 2, Witdth / 2), Height / 2)
pygame.draw.line(screen, Black, (0, Height / 2), (Witdth, Height / 2))
pygame.draw.line(screen, Black, (Witdth / 2, 0), (Witdth / 2, Height))
pygame.display.flip()

player1_score = 0
player2_score = 0

# main game loop
for i in range(10):
    print(f"#ROUND{i + 1}")
    for j in range(2):
        x_pos = random.randrange(0, Witdth + 1)
        y_pos = random.randrange(0, Height + 1)
        distance_from_center = math.hypot(x_pos - Witdth / 2, y_pos - Height / 2)
        is_in_circle = distance_from_center <= Witdth / 2
        if is_in_circle:
            if j == 0:
                pygame.draw.circle(screen, Red, (x_pos, y_pos), 4)
                player1_score += 1
                print(f"player red throws...hit")
            else:
                pygame.draw.circle(screen, Blue, (x_pos, y_pos), 4)
                player2_score += 1
                print(f"player blue throws...hit")
        else:
            pygame.draw.circle(screen, Black, (x_pos, y_pos), 4)
            if j == 0:
                print(f"player red throws...miss")
            else:
                print(f"player red throws...miss")
        pygame.display.flip()
        pygame.time.wait(400)

# print winners
print(f"Player Red scored {player1_score}")
print(f"Player Blue scored {player2_score}")
print()
if player1_score > player2_score:
    print("Player Red Wins")
    if guess == 1:
        print("Your guess was correct")
    else:
        print("Your guess was incorrect")
elif player1_score < player2_score:
    print("Player Blue Wins")
    if guess == 2:
        print("Your guess was correct")
    else:
        print("Your guess was incorrect")
else:
    print("This was a draw")
    print("Your guess was incorrect")

pygame.time.wait(2500)
pygame.quit()