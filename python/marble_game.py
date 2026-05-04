import random

class MarbleGame():
    def __init__(self, rounds=0, cash=1000, bag=["red", "red", "red", "red", "green", "green", "green", "green", "green", "green"]):
        self.rounds = rounds
        self.cash = cash
        self.bag = bag

    def gameStatus(self):
        if self.cash >= 500 and self.rounds <= 10:
            print("Game continues")
            return True
        else:
            print(f"Game over. Total cash = {self.cash}")
            return False

    def playRound(self, bet):
        self.bet = bet
        marble = random.choice(self.bag)
        if marble == "green":
            self.cash += self.bet
            print(f"User won bet {self.bet}")
        else:
            self.cash -= self.bet
            print(f"User lost bet {self.bet}")
        self.rounds += 1
        print(f"Total Rounds Played {self.rounds}")
        print(f"Total Cash Remaining {self.cash}")

    def beginGame(self):
        if self.gameStatus() == True:
            self.playRound(int(input('Choose your bet value: ')))
            self.beginGame()
        else:
            exit

mygame = MarbleGame()
mygame.beginGame()
