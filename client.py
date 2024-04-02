import pygame
from network import Network
pygame.font.init()

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


    clock = pygame.time.Clock()
    btn = Button("DARE", 275, 200, "#fff47c")
    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

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
    dare(n, player)
    odds(n, player)
    guess(n, player)
    winner(n, player)
    playAgain(n,player)



def dare(n, player):
    run = True
    clock = pygame.time.Clock()
    dare = ""
    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break
        bg = pygame.image.load("gameBackground.jpg")
        win.blit(bg, (0, 0))

        #challengerScreen
        if game.bothWent() and ((player == 0 and game.p0Challenger) or (player == 1 and game.p1Challenger)):
            #Need to have a text box
            font = pygame.font.Font("Minecraftia.ttf", 40)
            text = font.render("Enter your dare:", True, "#911300")
            #BUG WITH ENTERING AN EMPTY DARE
            rect = text.get_rect(center=(350, 100))
            win.blit(text, rect)
            for event in pygame.event.get():
                #cannot hold down buttons :( need to fix
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        dare = dare[:-1]

                    elif event.key == pygame.K_RETURN:
                        game = n.send(dare + "D")
                        run = False
                    else:
                        dare += event.unicode
            font = pygame.font.Font("Minecraftia.ttf", 30)
            text = font.render(dare, True, "#ae8fff")
            rect = text.get_rect(center=(350, 250))
            win.blit(text, rect)
        #challengedScreen
        elif game.bothWent():
            font = pygame.font.Font("Minecraftia.ttf", 40)
            text = font.render("Waiting for dare...", True, "#911300")
            rect = text.get_rect(center=(350, 100))
            win.blit(text, rect)
            if game.dare != "":
                run = False
        pygame.display.update()

def odds(n,player):
    run = True
    clock = pygame.time.Clock()
    odds = ""
    invalid = False
    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break
        bg = pygame.image.load("gameBackground.jpg")
        win.blit(bg, (0, 0))
        #challenger screen
        if game.bothWent() and ((player == 0 and game.p0Challenger) or (player == 1 and game.p1Challenger)):
            font = pygame.font.Font("Minecraftia.ttf", 40)
            text = font.render("Waiting for odds...", True, "#911300")
            rect = text.get_rect(center=(350, 100))
            win.blit(text, rect)
            if game.odds != 0:
                run = False
        #challenged screen
        else:
            font2 = pygame.font.Font("Minecraftia.ttf", 30)
            text2 = font2.render("odds to ...  " + game.dare, True, "#ae8fff")
            rect2 = text2.get_rect(center=(350, 100))
            font = pygame.font.Font("Minecraftia.ttf", 30)
            text = font.render("Enter your desired odds:", True, "#911300")
            rect = text.get_rect(center=(350, 175))
            win.blit(text2, rect2)
            win.blit(text, rect)
            if invalid:
                font = pygame.font.Font("Minecraftia.ttf", 30)
                text = font.render("Not Valid... ", True, "#4d0011")
                rect = text.get_rect(center=(350, 225))
                win.blit(text, rect)
            for event in pygame.event.get():
                #cannot hold down buttons :( need to fix
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        odds = odds[:-1]
                    elif event.key == pygame.K_RETURN:
                        try:
                            int(odds)
                        except ValueError:
                            invalid = True
                            odds = ""
                            break
                        game = n.send(odds + "O")
                        run = False
                    else:
                        odds += event.unicode
            font = pygame.font.Font("Minecraftia.ttf", 30)
            text = font.render(odds, True, "#ae8fff")
            rect = text.get_rect(center=(350, 265))
            win.blit(text, rect)
        pygame.display.update()


def guess(n,player):
    run = True
    invalid = False
    clock = pygame.time.Clock()
    guess = ""
    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break
        bg = pygame.image.load("gameBackground.jpg")
        win.blit(bg, (0, 0))

        font = pygame.font.Font("Minecraftia.ttf", 40)
        text = font.render("Odds set to " + game.odds, True, "#911300")
        rect = text.get_rect(center=(350, 100))
        font2 = pygame.font.Font("Minecraftia.ttf", 30)

        text2 = font2.render("Enter guess", True, "#ae8fff")
        rect2 = text2.get_rect(center=(350, 175))
        win.blit(text2, rect2)
        win.blit(text, rect)
        if invalid:
            font = pygame.font.Font("Minecraftia.ttf", 30)
            text = font.render("Not Valid... ", True, "#ae8fff")
            rect = text.get_rect(center=(350, 225))
            win.blit(text, rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    guess = guess[:-1]
                elif event.key == pygame.K_RETURN:
                    try:
                        int(guess)
                    except ValueError:
                        invalid = True
                        guess = ""
                        break
                    if int(guess) > int(game.odds):
                        invalid = True
                        guess = ""
                        break
                    else:
                        invalid = False
                        send = str(player) + guess + "G"
                        game = n.send(send)
                        run = False
                else:
                    guess += event.unicode
        font = pygame.font.Font("Minecraftia.ttf", 30)
        text = font.render(guess, True, "#ae8fff")
        rect = text.get_rect(center=(350, 265))
        win.blit(text, rect)
        pygame.display.update()

def winner(n,player):
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break
        bg = pygame.image.load("gameBackground.jpg")
        win.blit(bg, (0, 0))
        font = pygame.font.Font("Minecraftia.ttf", 40)
        text = font.render("Odds were set to " + str(game.odds), True, "#911300")
        rect = text.get_rect(center=(350, 100))
        win.blit(text, rect)
        #below code can be shortened
        # #guesses matched
        # LOGIC SHOULD BE REDONE BOTH MUST BE FALSE TO CHECK IF THEY BOTH WENT NEED TO RESET BOTHWENT IN BETWEEN
        #FUNC CALLS
        if game.p1Guess == game.p0Guess and (not game.p1Went and not game.p0Went):
            #challenger screen
            if (player == 0 and game.p0Challenger) or (player == 1 and game.p1Challenger):
                font = pygame.font.Font("Minecraftia.ttf", 20)
                text = font.render("SUCCESS! they also guessed " + game.p1Guess, True, "#911300")
                rect = text.get_rect(center=(350, 200))
                win.blit(text, rect)
            #challengee screen
            else:
                font = pygame.font.Font("Minecraftia.ttf", 25)
                text = font.render("You have to ... " + game.dare, True, "#911300")
                rect = text.get_rect(center=(350, 200))
                win.blit(text, rect)
            run = False
        elif not game.p1Went and not game.p0Went:
            font = pygame.font.Font("Minecraftia.ttf", 25)
            rect = text.get_rect(center=(350, 200))
            if player == 0:
                text = font.render("Nothing happens they said " + game.p1Guess , True, "#911300")
                win.blit(text, rect)
            elif player == 1:
                text = font.render(" Nothing happens they said " + game.p0Guess, True, "#911300")
                win.blit(text, rect)
            run = False
        pygame.display.update()



def playAgain(player,n):
    #implement game resetting and play again functionality
    i = 0
    while True:
        i += 1

menuScreen()