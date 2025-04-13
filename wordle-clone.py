import pygame
from sys import exit

list = ['rebus', 'siege', 'banal', 'gorge', 'query', 'abbey', 'proxy', 'aloft']
pygame.init()
screen = pygame.display.set_mode((633, 900))
clock = pygame.time.Clock()
starting_surf = pygame.image.load("assets/starting-squares.png")
starting_rect = starting_surf.get_rect(center = (316, 300))
print(starting_rect.x)

# DRAW STARTING SQUARES 6 rows of 5 letter words

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
                # screen.blit(starting_surf, starting_rect)
                # first row
                pygame.draw.rect(screen, (120, 124, 127), (148, 100, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (148, 170, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (148, 240, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (148, 310, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (148, 380, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (148, 450, 62, 62))
                # second row
                pygame.draw.rect(screen, (120, 124, 127), (218, 100, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (218, 170, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (218, 240, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (218, 310, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (218, 380, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (218, 450, 62, 62))
                # third row
                pygame.draw.rect(screen, (120, 124, 127), (288, 100, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (288, 170, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (288, 240, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (288, 310, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (288, 380, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (288, 450, 62, 62))
                # fourth row
                pygame.draw.rect(screen, (120, 124, 127), (358, 100, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (358, 170, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (358, 240, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (358, 310, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (358, 380, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (358, 450, 62, 62))
                # fifth row
                pygame.draw.rect(screen, (120, 124, 127), (428, 100, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (428, 170, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (428, 240, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (428, 310, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (428, 380, 62, 62))
                pygame.draw.rect(screen, (120, 124, 127), (428, 450, 62, 62))
                
                
    pygame.display.update()
    clock.tick(60)