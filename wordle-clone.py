import pygame
from sys import exit

list = ['rebus', 'siege', 'banal', 'gorge', 'query', 'abbey', 'proxy', 'aloft']
pygame.init()
screen = pygame.display.set_mode((633, 900))
clock = pygame.time.Clock()
text_font = pygame.font.Font('font/testFont.ttf', 50)
guess = []

def drawSquares():
    rows = 6
    letters = 5
    x_pos = 148
    y_pos = 100
    for i in range(rows):
        for j in range(letters):
            pygame.draw.rect(screen, (120, 124, 127), (x_pos, y_pos, 62, 62), 2)
            if i == 0 and j < len(guess):  # Only draw letters for the current row
                letter_surface = text_font.render(guess[j], False, (0, 0, 0))
                letter_rect = letter_surface.get_rect(center=(x_pos + 31, y_pos + 40))
                screen.blit(letter_surface, letter_rect)
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
    if len(guess) < 5:
        guess.append(letter)
        print(letter)
        print(guess)
    else:
        print("filled")
    # for i in range(rows):
    #     for j in range(letters):
    #         pygame.draw.rect(screen, (120, 124, 127), (x_pos, y_pos, 62, 62), 2)
    #         x_pos += 70
    #     x_pos = 148
    #     y_pos += 70
    
def removeLetter():
    if guess:
        guess.pop()
        print(guess)
    else:
        print("empty")

def checkWord():
    if guess and len(guess) == 5:
        if "".join(guess) == "WEIRD":
            print("You win")
            return False
        else:
            print("Try again")
    else:
        print("word not complete, len: ", len(guess))
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