import pygame
import numpy as np
from sys import exit

list = ['rebus', 'siege', 'banal', 'gorge', 'query', 'abbey', 'proxy', 'aloft']
pygame.init()
screen = pygame.display.set_mode((633, 900))
clock = pygame.time.Clock()
text_font = pygame.font.Font('font/testFont.ttf', 35)
key_font = pygame.font.Font('font/franklin.ttf', 20)
bigger_key = pygame.font.Font('font/franklin.ttf', 14)
all_guesses = [[]] # all guess
matching_letters = []
all_rect = []
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
            
def animateLetter(current_row, current_word):
    # make box and letter pop
    scale_factor = 62
    if current_row > 0 and len(current_word) < 6:
        x_pos = 148 + (70 * (len(current_word) - 1))
        y_pos = 100 + (70 * (current_row - 1))
        for i in range(20):
            pygame.time.delay(5)
            pygame.draw.rect(screen, (255, 255, 255), 
                             (x_pos + (62 - scale_factor) // 2, y_pos + (62 - scale_factor) // 2, scale_factor, scale_factor), 0) 
            if i < 10:
                scale_factor += 2
            else:
                scale_factor -= 2
            pygame.draw.rect(screen, (120, 124, 127), (x_pos + (62 - scale_factor) // 2, y_pos + (62 - scale_factor) // 2, scale_factor, scale_factor), 2)
            letter_surface = text_font.render(current_word[-1], True, (0, 0, 0))
            updated = scale_factor / 62
            scaled_letter = pygame.transform.scale(letter_surface, (int(letter_surface.get_width() * updated), int(letter_surface.get_height() * updated)))
            letter_rect = scaled_letter.get_rect(center=(x_pos + 31, y_pos + 35))
            screen.blit(scaled_letter, letter_rect)
            pygame.display.update()
  
def errorAnimate(current_row, current_word):
    # make row shake
    x_pos = 148
    y_pos = 100 + (70 * (current_row - 1))
    for i in range(20):
        for i in range(5):
            # pygame.time.delay(10)
            pygame.draw.rect(screen, (255, 255, 255), 
                                (x_pos, y_pos, 62, 62), 0) 
            x_pos += 70
            pygame.display.update()
        
        
        
    
    
          
def drawKeyboard():
    # draw first row
    all_keys = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", 
                 "A", "S", "D", "F", "G", "H", "J", "K", "L", 
                 "ENTER", "Z", "X", "C", "V", "B", "N", "M", "BACK"]
    x_pos = 104
    y_pos = 570
    for i in all_keys:
        box_colour = (211, 214, 218)
        text_colour = (0, 0, 0)
        increase_width = 43 # how much x_pos will be increased by 
        box_width = 38 # how much the width of the box will be
        current_text = key_font # setting font
        # setting the colour of box
        if len(matching_letters) > 0:
            for idx, val in enumerate(matching_letters):
                for j in val:
                    if i == j[0]:
                        box_colour = j[1]
                        text_colour = (255, 255, 255)
                        if box_colour == (108, 169, 101):
                            break
                else:
                    continue
                break

        if i == 'A':
            x_pos = 125
            y_pos = 628
        elif i == 'ENTER':
            x_pos = 104
            y_pos = 686
        if i == "ENTER" or i == "BACK":
            increase_width = 64
            box_width = 58
            current_text = bigger_key
        key = pygame.draw.rect(screen, box_colour, (x_pos, y_pos, box_width, 50), 0, 3) 
        if len(all_rect) < 28:
            all_rect.append((i, key)) # append the rect to the array to track collision
        letter_surface = current_text.render(i, True, text_colour)
        letter_rect = letter_surface.get_rect(center=(key.centerx, (key.centery - 2)))
        screen.blit(letter_surface, letter_rect)
        x_pos += increase_width 

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

def keyboardInput():
    if event.type == pygame.MOUSEBUTTONDOWN:
        for i, val in enumerate(all_rect):
            if val[1].collidepoint(event.pos):
                if val[0] == "ENTER":
                    checkWord()
                elif val[0] == "BACK":
                    removeLetter()
                else:
                    addLetter(val[0])

def addLetter(letter):
    # check if all_guess is not full
    if len(all_guesses) < 7:
        # check if all_guesses is empty or if the last guess has 5 letters
        if len(all_guesses[-1]) < 5:
            # append letter to last array in all_guesses
            all_guesses[-1].append(letter)
            animateLetter(len(all_guesses), all_guesses[-1])
            print(all_guesses[-1])
            print(all_guesses)
        else:
            print("last guess is full")
        
    else:
        print("you have already guesses 5 times")
        
def storeWord(word):
    # if verify the yellow parts
    colours = []
    indexes = []
    current_colour = (120, 124, 127)
    for idx, letter in enumerate(word):
        current_colour = (120, 124, 127)
        if letter == win_word[idx]: # letter is at the currnet index
            current_colour = (108, 169, 101)
        elif letter in win_word: # letter is somewhere in the word
            indexes = [i for i, val in enumerate(win_word) if val == letter] # get the index of the letter in correct word
            for index in indexes:
                if word[index] != win_word[index]:
                    current_colour = (200, 182, 83)
                else:
                    current_colour = (120, 124, 127)
        colours.append([letter, current_colour])
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
            print("word not long enough")
            errorAnimate(len(all_guesses), all_guesses[-1])
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
                # draw keyboard
                drawKeyboard()
                # get keyboard input
                keyboardInput()
                game_won = getKeyPressed()
            else:
                pygame.quit()
                exit()
                      
    pygame.display.update()
    clock.tick(60)