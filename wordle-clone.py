import pygame
import numpy as np
from sys import exit

list = ['rebus', 'siege', 'banal', 'gorge', 'query', 'abbey', 'proxy', 'aloft']
pygame.init()
screen = pygame.display.set_mode((633, 900))
clock = pygame.time.Clock()
text_font = pygame.font.Font('font/testFont.ttf', 35)
all_guesses = [[]] # all guess
matching_letters = []
location_letters = []
win_word = "JOKES"


def drawSquares():
    rows = 6
    letters = 5
    x_pos = 148
    y_pos = 100
    box_width = 2
    box_colour = (120, 124, 127)
    for i in range(rows):
        for j in range(letters):
            pygame.draw.rect(screen, (211, 214, 218), (x_pos, y_pos, 62, 62), 2)
            if i < len(all_guesses):
                if j < len(all_guesses[i]):  # Only draw letters for the current row
                    if len(matching_letters) > i and len(matching_letters[i]) == 5: 
                        box_colour =  matching_letters[i][j][1]
                        box_width = 0
                        text_colour = (255,255,255)
                    else:
                        box_colour = (120, 124, 127)
                        box_width = 2
                        text_colour = (0, 0, 0)
                    pygame.draw.rect(screen, box_colour, (x_pos, y_pos, 62, 62), box_width)
                    letter_surface = text_font.render(all_guesses[i][j], True, text_colour)
                    letter_rect = letter_surface.get_rect(center=(x_pos + 31, y_pos + 35))
                    screen.blit(letter_surface, letter_rect)
            x_pos += 70
        x_pos = 148
        y_pos += 70

def animateGuess(current_row, current_word):
    # create box animation 
    for idx, letter in enumerate(current_word):
        print("Current Row: ", current_row, " Current Word: ", current_word)
        x_pos = 148 + (70 * idx)
        y_pos = 100 + (70 * (current_row - 1))
        height = 62
        box_width = 2
        box_colour = (120, 124, 127)
        letter_colour = (0, 0, 0)
        for i in range(40):
            pygame.time.delay(15)
            # redraw background before printing new square animation
            pygame.draw.rect(screen, (255, 255, 255), (x_pos, y_pos, 62, 62), 0) 
            if i < 20:
                height -= 3
            else:
                height += 3
                box_width = 0
                box_colour = matching_letters[current_row - 1][idx][1]
                letter_colour = (255, 255, 255)
            pygame.draw.rect(screen, box_colour, (x_pos, y_pos + (62 - height) // 2, 62, height), box_width)
            letter_surface = text_font.render(letter, True, letter_colour)
            letter_rect = letter_surface.get_rect(center=(x_pos + 31, y_pos + 35))
            letter_crop = pygame.Rect(x_pos, y_pos + (62 - height) // 2, 62, height)
            screen.set_clip(letter_crop)
            screen.blit(letter_surface, letter_rect)
            screen.set_clip(None)
            pygame.display.update()
            
    
    
    
    

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
    if len(all_guesses) < 7:
        # check if all_guesses is empty or if the last guess has 5 letters
        if len(all_guesses[-1]) < 5:
            # append letter to last array in all_guesses
            all_guesses[-1].append(letter)
            print(all_guesses[-1])
            print(all_guesses)
        else:
            print("last guess is full")
        
    else:
        print("you have already guesses 5 times")
        
def storeWord(word):
    colours = []
    for idx, letter in enumerate(word):
        if letter == win_word[idx]:
            colours.append([letter, (108, 169, 101)])
        elif letter in win_word:
            colours.append([letter, (200, 182, 83)])
        else: 
            colours.append([letter, (120, 124, 127)])
    matching_letters.append(colours) 
    
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
            storeWord(all_guesses[-1])
            current_word, current_row = all_guesses[-1], len(all_guesses)
            if "".join(all_guesses[-1]) == "JOKES":
                print("You win")
            else:
                # if it does not match, check if all turns are up
                if len(all_guesses) != 6:
                    all_guesses.append([])
                    print(all_guesses)
                    print("Try again")
                else: 
                    print("Game Over")
            # put animation here
            animateGuess(current_row, current_word)
            return False
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
                game_won = getKeyPressed()
            else:
                pygame.quit()
                exit()
                      
    pygame.display.update()
    clock.tick(60)