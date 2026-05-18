# class design

from enum import Enum

class GameState(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    WON = "WON"
    DRAW = "DRAW"

class Game:
    def __init__ (self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.state = GameState.IN_PROGRESS
        
    def makeMove(self, player, column: int):
        if self.state is not GameState.IN_PROGRESS:
            return False
        if self.player is not self.current_player:
            return False
        
        row = self.board.placeDisc(column, player.getColor())
        if row == -1:
            return False
        
        if self.board.isFull():
            self.state = GameState.DRAW
        elif self.board.checkForWin():
            self.state = GameState.WON
        else:
            self.current_player = self.player2 if self.current_player is self.player1 else self.player1

        return True

    def checkCurrentPlayer(self):
        return self.current_player
    
    def getCurrentState(self):
        return self.state

class Board:
    def __init__(self, rows: int = 6, cols: int = 7):
        self.rows = rows
        self.cols = cols
        self.grid = []

        for row in range(rows):
            current_row = []

            for col in range(cols):
                current_row.append(None)

            self.grid.append(current_row)

    def isFull(self):
        for row in self.grid:
            for col in row:
                if col is None:
                    return False
        
        return True

    


    def getGrid(self):
        return self.grid
    
    def getRows(self):
        return self.rows
    
    def getCols(self):
        return self.cols


board = Board()
isfull = board.isFull()
print(isfull)