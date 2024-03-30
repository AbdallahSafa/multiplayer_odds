
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
        self.accepted = False
        self.p1Guess = 0
        self.p0Guess = 0

    def getOdds(self):
        return self.odds

    def play(self,player,dare,odds,accepted,challenger):
        self.dare = dare
        self.odds = odds
        self.accepted = True
        if challenger == True and player == 0:
            self.p0Challenger = True
            self.p0Went = True
        elif challenger == True and player == 1:
            self.p1Challenger = True
            self.p1Went = True

        #implement later
        # if not accepted:
        #     self.dare = ""
        #     self.odds = 0

    def whoisChallenger(self, data):
        if data == "challenger0":
            self.p0Challenger = True
        elif data == "challenger1":
            self.p1Challenger = True


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
        self.accepted = False
        self.p1Guess = 0
        self.p0Guess = 0