import pygame
from tkinter import *
from tkinter import messagebox
import infoChicken
from infoChicken import ally_hp, ene_hp, currentally_hp, currentenemy_hp
import roosterfile

class Game:
    def __init__(self):
        self.balance = 1000
        self.run = False
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        
        self.side_panel = 400
        self.screen_width = 720
        self.screen_height = 720
        self.screen = None
        self.background_img = None
        

    def start_game(self):
        pygame.init()
        self.run = True
        self.gui.destroy()

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Battle")
        font = pygame.font.Font('freesansbold.ttf', 32)
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        text = font.render('GeeksForGeeks', True, green, blue)
        textRect = text.get_rect()
        textRect.center = (200,200)

        self.background_img = pygame.image.load("background.jpg").convert_alpha()
        self.game_loop()


    def draw_bg(self):
        self.screen.blit(self.background_img, (0, 0))

    def game_loop(self):
        while self.run:
       
            self.clock.tick(self.fps)
            self.draw_bg()
    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.update()

        pygame.quit()

    def add_funds(self):
        pass

    def run_gui(self):
        self.gui = Tk()
        self.gui.configure(background="#003b00")
        self.gui.title("Main Menu")
        self.gui.geometry("720x720")

        Balance = Label(self.gui, text=f"Balance: ${self.balance}", font=("Arial", 14), bg="#003b00", fg="#00ff41")
        Title = Label(self.gui, text="Cock Fight", bg="#003b00", fg="#00ff41", font=("Arial", 35, "bold"))

        StartButton = Button(self.gui, text="Start", command=self.start_game, bg="#003b00", fg="#00ff41", font=("Arial", 20, "bold"))
        fundsButton = Button(self.gui, text="Add Funds", command=self.add_funds, bg="#003b00", fg="#00ff41", font=("Arial", 20, "bold"))
        fundsLabel = Label(self.gui, text="Add Funds", bg="#003b00", fg="#00ff41", font=("Arial", 35, "bold"))

        Balance.pack(side=TOP, anchor=NW, padx=10)
        Title.pack()
        StartButton.pack(pady=(0, 10))
        fundsLabel.pack()
        fundsButton.pack(pady=(0, 10))

        self.gui.mainloop()


if __name__ == "__main__":
    game = Game()
    game.run_gui()
