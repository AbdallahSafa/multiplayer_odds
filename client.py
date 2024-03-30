import pygame
from network import Network
from game import Game
import pickle
pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Odds")

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False





def menuScreen():
    run = True
    n = Network()
    player = int(n.getP())
    clock = pygame.time.Clock()
    game = n.send("get")
    btn = Button("CHALLENGER", 100, 100, (0,255,0))
    while run:
        clock.tick(60)
        win.fill((128,128,128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Odds", 1, (255,0,0))
        win.blit(text, (100, 200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if btn.click(pos) and game.connected():
                    if player == 0:
                        if not game.p0Went:
                            n.send("p0Challenger")
                    elif (player == 1):
                        if not game.p1Went:
                            n.send("p1Challenger")
while True:
    menu_screen()