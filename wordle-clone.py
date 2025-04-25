import pygame
import numpy as np
import random
from sys import exit

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((633, 900))
        pygame.display.set_caption("Wordle Clone")
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = Board(self.screen, self)
        self.keyboard = Keyboard(self.screen, self)
        self.game_won = False
        self.rounds = 0
        self.win_word = ""
        self.all_guesses = [[]]
        self.matching_letters = []
        self.animation_running = False
        self.animations = AnimationManager(self.screen, self)
        self.current_display = DisplayScreen(self.screen, self)
        
        
    def run(self):
        while self.running:
            if self.current_display.get_game_display() == "START":
                self.handle_screen_events()
                self.current_display.draw_start_screen()
            elif self.current_display.get_game_display() == "PLAY":
                self.handle_events()
                self.update()
                self.draw()
            elif self.current_display.get_game_display() == "PAUSE":
                self.draw()
                self.handle_screen_events()
                self.current_display.draw_back_arrow()
            elif self.current_display.get_game_display() == "END":
                self.handle_screen_events()
                self.current_display.draw_end_screen()
            elif self.current_display.get_game_display() == "QUIT":
                self.running = False
            pygame.display.update() 
            self.clock.tick(60)
    
    def restart_game(self):
        self.all_guesses = [[]]
        self.matching_letters = []
        if self.win_word != "":
            self.rounds += 1
            self.game_won = False
        list = ['rebus', 'siege', 'banal', 'gorge', 'query', 'abbey', 'proxy', 'aloft', 'gauge']
        self.win_word = random.choice(list).upper()
    def was_game_won(self):
        return self.game_won
    
    def set_game_won(self, game_won):
        self.game_won = game_won
    
    def handle_screen_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif not self.animation_running:
                self.current_display.update(event)
                          
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif not self.animation_running:
                self.keyboard.update(event, self.board, self.win_word)
           
    def update(self):
        pass 
        
        
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.board.draw()
        self.keyboard.draw(self.matching_letters)
        
    def get_all_guesses(self):
        return self.all_guesses
    
    def update_all_guesses(self, new_guesses):
        self.all_guesses = new_guesses
        
    def get_matching_letters(self):
        return self.matching_letters
    
    def update_matching_letters(self, new_matching_letters):
        self.matching_letters = new_matching_letters
        

class Board:
    def __init__(self, screen, game):
        self.screen = screen
        self.rows = 6
        self.columns = 5
        self.game = game
        self.text_font = pygame.font.Font('font/testFont.ttf', 35)
        self.title_font = pygame.font.Font('font/testFont.ttf', 30)
        
    
    def draw(self):
        x_pos = 148
        y_pos = 100
        all_guesses = self.game.get_all_guesses()
        matching_letters = self.game.get_matching_letters()
        box_width = 2
        box_colour = (120, 124, 127)
        title_surface = self.title_font.render("Wordle", True, (0, 0, 0))
        title_rect = title_surface.get_rect(center = (316, 50))
        self.screen.blit(title_surface, title_rect)
        for i in range(self.rows):
            for j in range(self.columns):
                pygame.draw.rect(self.screen, (211, 214, 218), (x_pos, y_pos, 62, 62), 2)
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
                        pygame.draw.rect(self.screen, box_colour, (x_pos, y_pos, 62, 62), box_width)
                        letter_surface = self.text_font.render(all_guesses[i][j], True, text_colour)
                        letter_rect = letter_surface.get_rect(center=(x_pos + 31, y_pos + 35))
                        self.screen.blit(letter_surface, letter_rect)
                x_pos += 70
            x_pos = 148
            y_pos += 70
        
    def add_letter(self, letter):
          # check if all_guess is not full
        all_guesses = self.game.get_all_guesses()
        if len(all_guesses) < 7:
            # check if all_guesses is empty or if the last guess has 5 letters
            if len(all_guesses[-1]) < 5:
                # append letter to last array in all_guesses
                all_guesses[-1].append(letter)
                self.game.update_all_guesses(all_guesses)
                self.game.animations.animate_letter(len(all_guesses), all_guesses[-1])
            else:
                print("last guess is full")
            
        else:
            print("you have already guesses 5 times")
                
    def remove_letter(self):
        all_guesses = self.game.get_all_guesses()
        if all_guesses:
            if all_guesses[-1]:
                all_guesses[-1].pop()
                self.game.update_all_guesses(all_guesses)
            else:
                print("word empty")
        else:
            print("all guesses empty")
    
    def check_word(self, win_word):
          # check if all_guesses is not empty 
        all_guesses = self.game.get_all_guesses()
        if all_guesses:
            # check if the last guess has 5 letters
            if len(all_guesses[-1]) == 5:
                self.store_word(all_guesses[-1], win_word)
                current_word, current_row = all_guesses[-1], len(all_guesses)
                if "".join(all_guesses[-1]) == win_word:
                    self.game.set_game_won(True)
                    self.game.current_display.set_game_display("END")
                else:
                    # if it does not match, check if all turns are up
                    if len(all_guesses) != 6:
                        all_guesses.append([])
                        self.game.update_all_guesses(all_guesses)
                        print("Try again")
                    else: 
                        self.game.current_display.set_game_display("END")
                # put animation here
                self.game.animations.animate_guess(current_row, current_word)
                self.game.draw()
                if self.game.was_game_won():
                    self.game.animations.animate_win(current_row, current_word)
            else:
                print("word not long enough")
                self.game.animations.animate_error()
        else:
            print("Please enter word first")
                 
    def store_word(self, word, win_word):
        colours = []
        matching_letters = self.game.get_matching_letters()
        current_colour = (120, 124, 127)
        
        # Track which letters in the word have been matched
        win_word_used = [False] * len(win_word)
        
        # Handle matching letters first
        for idx, letter in enumerate(word):
            if letter == win_word[idx]: # letter is at the currnet index
                current_colour = (108, 169, 101)
                win_word_used[idx] = True # mark this letter as used
            else:
                current_colour = (120, 124, 127)
            colours.append([letter, current_colour])
            
        # Handle letters as wrong position
        for idx, letter in enumerate(word):
            if colours[idx][1] == (108, 169, 101):
                continue
            if letter in win_word: # letter is somewhere in the word
                # Find an unused occurence of letter in win_word
                for win_idx, win_letter in enumerate(win_word):
                    if win_letter == letter and not win_word_used[win_idx]:
                        current_colour = (200, 182, 83)
                        win_word_used[win_idx] = True
                        break
                else:
                    current_colour = (120, 124, 127)
            else:
                current_colour = (120, 124, 127)   
            colours[idx][1] = current_colour     
            
        matching_letters.append(colours) 
        self.game.update_matching_letters(matching_letters)
                   
 

class Keyboard:
    def __init__(self, screen, game):
        self.all_keys = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", 
                    "A", "S", "D", "F", "G", "H", "J", "K", "L", 
                    "ENTER", "Z", "X", "C", "V", "B", "N", "M", "BACK"]
        self.screen = screen
        self.game = game
        self.all_rect = []
        self.key_font = pygame.font.Font('font/franklin.ttf', 20)
        self.bigger_key = pygame.font.Font('font/franklin.ttf', 14)
        
    def draw(self, matching_letters):
        
        x_pos = 104
        y_pos = 570
        for i in self.all_keys:
            box_colour = (211, 214, 218)
            text_colour = (0, 0, 0)
            increase_width = 43 # how much x_pos will be increased by 
            box_width = 38 # how much the width of the box will be
            current_text = self.key_font # setting font
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
                current_text = self.bigger_key
            key = pygame.draw.rect(self.screen, box_colour, (x_pos, y_pos, box_width, 50), 0, 3) 
            if len(self.all_rect) < 28:
                self.all_rect.append((i, key)) 
            letter_surface = current_text.render(i, True, text_colour)
            letter_rect = letter_surface.get_rect(center=(key.centerx, (key.centery - 2)))
            self.screen.blit(letter_surface, letter_rect)
            x_pos += increase_width 
        
    def handle_mouse_input(self, event, board, win_word):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, val in enumerate(self.all_rect):
                if val[1].collidepoint(event.pos):
                    if val[0] == "ENTER":
                        board.check_word(win_word)
                    elif val[0] == "BACK":
                        board.remove_letter()
                    else:
                        board.add_letter(val[0])

    def handle_key_input(self, event, board, win_word):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                board.add_letter("A")
            elif event.key == pygame.K_b:
                board.add_letter("B")
            elif event.key == pygame.K_c:
                board.add_letter("C")
            elif event.key == pygame.K_d:
                board.add_letter("D")
            elif event.key == pygame.K_e:
                board.add_letter("E")
            elif event.key == pygame.K_f:
                board.add_letter("F")
            elif event.key == pygame.K_g:
                board.add_letter("G")
            elif event.key == pygame.K_h:
                board.add_letter("H")
            elif event.key == pygame.K_i:
                board.add_letter("I")
            elif event.key == pygame.K_j:
                board.add_letter("J")
            elif event.key == pygame.K_k:
                board.add_letter("K")
            elif event.key == pygame.K_l:
                board.add_letter("L")
            elif event.key == pygame.K_m:
                board.add_letter("M")
            elif event.key == pygame.K_n:
                board.add_letter("N")
            elif event.key == pygame.K_o:
                board.add_letter("O")
            elif event.key == pygame.K_p:
                board.add_letter("P")
            elif event.key == pygame.K_q:
                board.add_letter("Q")
            elif event.key == pygame.K_r:
                board.add_letter("R")
            elif event.key == pygame.K_s:
                board.add_letter("S")
            elif event.key == pygame.K_t:
                board.add_letter("T")
            elif event.key == pygame.K_u:
                board.add_letter("U")
            elif event.key == pygame.K_v:
                board.add_letter("V")
            elif event.key == pygame.K_w:
                board.add_letter("W")
            elif event.key == pygame.K_x:
                board.add_letter("X")
            elif event.key == pygame.K_y:
                board.add_letter("Y")
            elif event.key == pygame.K_z:
                board.add_letter("Z")
            elif event.key == pygame.K_BACKSPACE:
                board.remove_letter()
            elif event.key == pygame.K_RETURN:
                board.check_word(win_word)

    def mouse_tracking(self):
        x_mouse, y_mouse = pygame.mouse.get_pos()
        cursor_changed = False
        for i, val in enumerate(self.all_rect):
            if val[1].collidepoint((x_mouse, y_mouse)):
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
                cursor_changed = True
                break
            
        if not cursor_changed:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW) 
    
    def update(self, event, board, win_word):
        self.handle_mouse_input(event, board, win_word)
        self.handle_key_input(event, board, win_word)
        self.mouse_tracking()
        
    
class AnimationManager:
    def __init__(self, screen, game):
        self.screen = screen
        self.alpha_change = 255
        self.game = game
        self.error_image = pygame.transform.scale(pygame.image.load('assets/not_enough_error.png').convert_alpha(), (200, 50))
        self.error_rect = self.error_image.get_rect(center=(316, 100))
        self.text_font = pygame.font.Font('font/testFont.ttf', 35)

    def animate_guess(self, row, word):
    # create animation for guess
        self.game.animations_running = True
        matching_letters = self.game.get_matching_letters()
        for idx, letter in enumerate(word):
            x_pos = 148 + (70 * idx)
            y_pos = 100 + (70 * (row - 1))
            height = 62
            box_width = 2
            box_colour = (120, 124, 127)
            letter_colour = (0, 0, 0)
            for i in range(40):
                pygame.time.delay(15)
                # redraw background before printing new square animation
                pygame.draw.rect(self.screen, (255, 255, 255), (x_pos, y_pos, 62, 62), 0) 
                if i < 20:
                    height -= 3
                else:
                    height += 3
                    box_width = 0
                    box_colour = matching_letters[row - 1][idx][1]
                    letter_colour = (255, 255, 255)
                pygame.draw.rect(self.screen, box_colour, (x_pos, y_pos + (62 - height) // 2, 62, height), box_width)
                letter_surface = self.text_font.render(letter, True, letter_colour)
                letter_rect = letter_surface.get_rect(center=(x_pos + 31, y_pos + 35))
                letter_crop = pygame.Rect(x_pos, y_pos + (62 - height) // 2, 62, height)
                self.screen.set_clip(letter_crop)
                self.screen.blit(letter_surface, letter_rect)
                self.screen.set_clip(None)
                pygame.display.update()
        self.game.animations_running = False
      
    def animate_letter(self, current_row, current_word):
        # make box and letter pop
        self.game.animations_running = True
        scale_factor = 62
        if current_row > 0 and len(current_word) < 6:
            x_pos = 148 + (70 * (len(current_word) - 1))
            y_pos = 100 + (70 * (current_row - 1))
            for i in range(20):
                pygame.time.delay(3)
                pygame.draw.rect(self.screen, (255, 255, 255), 
                                (x_pos + (62 - scale_factor) // 2, y_pos + (62 - scale_factor) // 2, scale_factor, scale_factor), 0) 
                if i < 10:
                    scale_factor += 1
                else:
                    scale_factor -= 1
                pygame.draw.rect(self.screen, (120, 124, 127), (x_pos + (62 - scale_factor) // 2, y_pos + (62 - scale_factor) // 2, scale_factor, scale_factor), 2)
                letter_surface = self.text_font.render(current_word[-1], True, (0, 0, 0))
                updated = scale_factor / 62
                scaled_letter = pygame.transform.scale(letter_surface, (int(letter_surface.get_width() * updated), int(letter_surface.get_height() * updated)))
                letter_rect = scaled_letter.get_rect(center=(x_pos + 31, y_pos + 35))
                self.screen.blit(scaled_letter, letter_rect)
                pygame.display.update()
        self.game.animations_running = False
       
    def animate_error(self):
        self.alpha_change = 255
        self.game.animations_running = True
        self.error_image.set_alpha(self.alpha_change)
        for i in range(40):
            while self.alpha_change > 0:
                pygame.time.delay(50)
                self.screen.fill((255, 255, 255))
                self.game.draw()
                self.error_image.set_alpha(self.alpha_change)
                self.screen.blit(self.error_image, self.error_rect)
                pygame.display.update()
                if self.alpha_change == 255:
                    pygame.time.delay(1000)
                self.alpha_change -= 20
        self.game.animations_running = False

    def animate_win(self, row, word):
        self.game.animations_running = True
        original_y_positions = []  # Store the original y positions of the boxes

        # Calculate the positions of each box
        for idx in range(len(word)):
            x_pos = 148 + (70 * idx)
            y_pos = 100 + (70 * (row - 1))
            original_y_positions.append(y_pos)

        # Perform the jump animation in a wave-like motion
        for frame in range(30):  # Total frames for the animation
            self.game.board.draw()  # Redraw the board
            for idx, letter in enumerate(word):
                x_pos = 148 + (70 * idx)
                y_pos = original_y_positions[idx]

                # Calculate the jump height using a sine wave effect
                jump_offset = int(10 * abs(np.sin((frame - idx * 2) * (np.pi / 15))))  # Adjust the multiplier for wave effect
                y_pos -= jump_offset
                pygame.draw.rect(self.screen, (255, 255, 255), (x_pos, original_y_positions[idx] - 10, 62, 62 + 10), 0)

                # Draw the box
                pygame.draw.rect(self.screen, (108, 169, 101), (x_pos, y_pos, 62, 62), 0)
                letter_surface = self.text_font.render(letter, True, (255, 255, 255))
                letter_rect = letter_surface.get_rect(center=(x_pos + 31, y_pos + 35))
                self.screen.blit(letter_surface, letter_rect)

            pygame.display.update()
            pygame.time.delay(30)  # Delay between frames

        self.game.animations_running = False

class Button:
    def __init__(self, label, rect, font, bg_colour, text_colour, box_type):
        self.label = label
        self.rect = rect
        self.font = font
        self.bg_colour = bg_colour
        self.text_colour = text_colour
        self.box_type = box_type

    def move_y(self, change):
        self.rect.move_ip(0, change)
        
    def change_label(self, label):
        self.label = label
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_colour, self.rect, self.box_type, 20)
        text_surface = self.font.render(self.label, True, self.text_colour)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
        

class DisplayScreen:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.current_display = "START"
        self.cube_surface = pygame.transform.scale(pygame.image.load("assets/wordle_cube.png").convert_alpha(), (80, 80))
        self.cube_rect = self.cube_surface.get_rect(center=(316, 300))
        self.title_font = pygame.font.Font('font/testFont.ttf', 50)
        self.desc_font = pygame.font.Font('font/franklin.ttf', 20)
        self.button_font = pygame.font.Font('font/franklin.ttf', 15)
        self.buttons = [
            Button("Play", pygame.Rect(241, 465, 150, 40), self.button_font, (0, 0, 0), (227, 227, 225), 0),
            Button("Play Again", pygame.Rect(241, 515, 150, 40), self.button_font, (0, 0, 0), (0, 0, 0), 1),
            Button("Exit", pygame.Rect(241, 565, 150, 40), self.button_font, (0, 0, 0), (0, 0, 0), 1),
        ]
        self.back_button = Button("Back", pygame.Rect(25, 25, 100, 40), self.button_font, (0, 0, 0), (255, 255, 255), 0)
        
    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif self.current_display == "START":
                self.update(event)
                self.draw_start_screen()
            elif self.current_display == "END":
                self.update(event)
                self.draw_end_screen()
        
                    
    def set_game_display(self, current_display):
        self.current_display = current_display
    
    def get_game_display(self):
        return self.current_display 
    
    def draw_back_arrow(self):
        self.back_button.draw(self.screen)
    
    def handle_mouse_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if self.current_display != "PAUSE":
                for button in self.buttons:
                    if button.is_hovered(mouse_pos):
                        if button.label == "Play" or button.label == "Play Again":
                            self.game.restart_game()
                            self.set_game_display("PLAY")
                        elif button.label == "View Stats":
                            self.set_game_display("PAUSE")
                        elif button.label == "Exit":
                            self.game.running = False
            else: 
                if self.back_button.is_hovered(mouse_pos):
                    self.set_game_display("END")
        
    def mouse_tracking(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.current_display != "PAUSE":
            for button in self.buttons:
                if button.is_hovered(mouse_pos):
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
                    return
        else:
            if self.back_button.is_hovered(mouse_pos):
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
                    return
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)     
    
    def update(self, event):
        self.handle_mouse_input(event)
        self.mouse_tracking()
    
    def draw_start_screen(self):  
        # wordle cube
        self.screen.fill((227, 227, 225))
        self.screen.blit(self.cube_surface, self.cube_rect)
        # title
        title_surface = self.title_font.render("Wordle", True, (0, 0, 0))
        title_rect = title_surface.get_rect(center = (316, 380))
        self.screen.blit(title_surface, title_rect)
        # game desc
        desc_surface = self.desc_font.render("Get 6 chances to guess a 5-letter word", True, (0, 0, 0))
        desc_rect = desc_surface.get_rect(center = (316, 425))
        self.screen.blit(desc_surface, desc_rect)
        # start buttons
        self.buttons[0].change_label("Play")
        for button in self.buttons:
            if button.label != "Play Again":
                if button.label == "Exit" and button.rect.y == 565:
                    button.move_y(-50)
                button.draw(self.screen)
        pygame.display.update()

    def draw_end_screen(self):
        # was game on
        game_won = self.game.was_game_won()
        # wordle cube
        self.screen.fill((227, 227, 225))
        self.screen.blit(self.cube_surface, self.cube_rect)
        # title
        title_surface = self.title_font.render("Wordle", True, (0, 0, 0))
        title_rect = title_surface.get_rect(center = (316, 380))
        self.screen.blit(title_surface, title_rect)
        # game desc
        desc_surface = self.desc_font.render("You win" if game_won else f"Game Over, Word was: {self.game.win_word}", True, (0, 0, 0))
        desc_rect = desc_surface.get_rect(center = (316, 425))
        self.screen.blit(desc_surface, desc_rect)
        # start buttons
        self.buttons[0].change_label("View Stats")
        for button in self.buttons:
            if button.label == "Exit" and button.rect.y == 515:
                button.move_y(50)
            button.draw(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()