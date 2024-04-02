
class Game:
    def __init__(self,id):
        self.p0Went = False
        self.p1Went = False
        self.ready = False
        self.id = id
        self.dare = ""
        self.p0Challenger = False
        self.p1Challenger = False
        self.odds = 0
        self.p1Guess = 0
        self.p0Guess = 0

    def getOdds(self):
        return self.odds

    def play(self,player,dare,odds,accepted,challenger):
        self.dare = dare
        self.odds = odds
        self.accepted = True

    def setGuess(self,player,guess):
        int(guess)
        if player == '0':
            self.p0Guess = guess
            self.p0Went = False
        else:
            self.p1Guess = guess
            self.p1Went = False

    def setDare(self,dare):
        self.dare = dare

    def setOdds(self,odds):
        int(odds)
        self.odds = odds


    def whoisChallenger(self, data):
        if data == "challenger0" and not self.p1Challenger:
            self.p0Challenger = True
        elif data == "challenger1" and not self.p0Challenger:
            self.p1Challenger = True
        if data == "challenger0":
            self.p0Went = True
        else:
            self.p1Went = True


    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p0Went and self.p1Went


    def challengerWin(self):
        #check if valid guess in client
        g1 = self.p1Guess
        g0 = self.p0Guess
        if g1 == g0:
            return True

    def resetWent(self):
        self.p0Went = False
        self.p1Went = False
        self.dare = ""
        self.odds = 0
        self.p1Guess = 0
        self.p0Guess = 0