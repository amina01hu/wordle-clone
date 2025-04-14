import pygame
import numpy as np
from sys import exit

list = ['rebus', 'siege', 'banal', 'gorge', 'query', 'abbey', 'proxy', 'aloft']
pygame.init()
screen = pygame.display.set_mode((633, 900))
clock = pygame.time.Clock()
text_font = pygame.font.Font('font/testFont.ttf', 40)
all_guesses = [] # all guess
guess = [] # word

def drawSquares():
    rows = 6
    letters = 5
    x_pos = 148
    y_pos = 100
    for i in range(rows):
        for j in range(letters):
            pygame.draw.rect(screen, (120, 124, 127), (x_pos, y_pos, 62, 62), 2)
            if i < len(all_guesses):
                if j < len(all_guesses[i]):  # Only draw letters for the current row
                    letter_surface = text_font.render(all_guesses[i][j], False, (0, 0, 0))
                    letter_rect = letter_surface.get_rect(center=(x_pos + 31, y_pos + 35))
                    screen.blit(letter_surface, letter_rect)
                # x_pos = 148
            x_pos += 70
        x_pos = 148
        y_pos += 70


def getKeyPressed():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            addLetter("A")
        elif event.key == pygame.K_b:
            addLetter("B")
        elif event.key == pygame.K_c:
            addLetter("C")
        elif event.key == pygame.K_d:
            addLetter("D")
        elif event.key == pygame.K_e:
            addLetter("E")
        elif event.key == pygame.K_f:
            addLetter("F")
        elif event.key == pygame.K_g:
            addLetter("G")
        elif event.key == pygame.K_h:
            addLetter("H")
        elif event.key == pygame.K_i:
            addLetter("I")
        elif event.key == pygame.K_j:
            addLetter("J")
        elif event.key == pygame.K_k:
            addLetter("K")
        elif event.key == pygame.K_l:
            addLetter("L")
        elif event.key == pygame.K_m:
            addLetter("M")
        elif event.key == pygame.K_n:
            addLetter("N")
        elif event.key == pygame.K_o:
            addLetter("O")
        elif event.key == pygame.K_p:
            addLetter("P")
        elif event.key == pygame.K_q:
            addLetter("Q")
        elif event.key == pygame.K_r:
            addLetter("R")
        elif event.key == pygame.K_s:
            addLetter("S")
        elif event.key == pygame.K_t:
            addLetter("T")
        elif event.key == pygame.K_u:
            addLetter("U")
        elif event.key == pygame.K_v:
            addLetter("V")
        elif event.key == pygame.K_w:
            addLetter("W")
        elif event.key == pygame.K_x:
            addLetter("X")
        elif event.key == pygame.K_y:
            addLetter("Y")
        elif event.key == pygame.K_z:
            addLetter("Z")
        elif event.key == pygame.K_BACKSPACE:
            removeLetter()
        elif event.key == pygame.K_RETURN:
            return checkWord()
    return True

def addLetter(letter):
    # check if all_guess is not full
    if len(all_guesses) < 6:
        # check if all_guesses is empty or if the last guess has 5 letters
        if not all_guesses or all_guesses[-1][-1] == "\n" or len(all_guesses[-1]) < 5:
            # append empty array to all_guesses
            all_guesses.append([])
            # append letter to last array in all_guesses
            all_guesses[-1].append(letter)
            print(all_guesses[-1])
            print(all_guesses)
        else:
            print("last guess is full")
        
    else:
        print("you have already guesses 5 times")
        
        
def removeLetter():
    # check if all_guesses is not empty
    if all_guesses:
        # check if last guesses is not empty
        if all_guesses[-1]:
            # remove last letter in last guess
            all_guesses[-1].pop()
            print(all_guesses[-1])
        else:
            "word empty"
    else:
        print("all_guesses array empty")

def checkWord():
    # check if all_guesses is not empty 
    if all_guesses:
        # check if the last guess has 5 letters
        if len(all_guesses[-1]) == 5:
            if "".join(all_guesses[-1]) == "JOKES":
                print("You win")
                return False
            else:
                # append new array for new word
                #all_guesses.append([])
                print(all_guesses)
                print("Try again")
            all_guesses[-1].append("\n")
        else:
            print("word not complete, len: ", len(all_guesses[-1]))
    else:
        print("Please enter word first")
    return True

game_active = True
score = 0



    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        else:
            if game_active:
                screen.fill((255, 255, 255))
                # draw starting squares
                drawSquares()
                # get keyboard input
                game_active = getKeyPressed()
            else:
                pygame.quit()
                exit()
                
                
                
            
                
                
                
                
                
    pygame.display.update()
    clock.tick(60)