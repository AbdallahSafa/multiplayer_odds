import pygame
from network import Network
pygame.font.init()
import pickle

width = 700
height = 500
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
        text = font.render(self.text, 1, (0,0,0))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


def menuScreen():
    print("entered menu")
    run = True
    n = Network()
    player = int(n.getP())
    print("You are player", player)

    clock = pygame.time.Clock()
    game = n.send("get")
    btn = Button("DARE", 275, 200, "#fff47c")
    while run:
        bg = pygame.image.load("menuDice.jpg")
        win.blit(bg, (0, 0))
        font = pygame.font.Font("Minecraftia.ttf", 100)
        text = font.render("ODDS",True,"#fff47c")
        rect = text.get_rect(center=(350, 100))
        win.blit(text,rect)

        clock.tick(60)
        btn.draw(win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if btn.click(pos):
                    if player == 0:
                        if not game.p0Went:
                            game = n.send("challenger0")
                            run = False
                    elif player == 1:
                        if not game.p1Went:
                            game = n.send("challenger1")
                            run = False
    print(game.p0Challenger)
    print(game.p1Challenger)
    main()


def main():
    pygame.quit()


menuScreen()