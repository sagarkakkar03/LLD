from abc import ABC, abstractmethod
from enum import Enum

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range (size)]
    
    def addPiece(self, row, col, playingPiece):
        if self.board[row][col]:
            self.printBoard()
            return False
        self.board[row][col] = playingPiece.symbol
        self.printBoard()
        return True
    
    def getFreeCells(self):
        freeCells = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == None:
                    freeCells.append((row, col))
        return freeCells

    def printBoard(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == None:
                    print('| |', end = '')
                else:
                    print(f'|{self.board[row][col]}|', end = '')
            print()

class PieceType(Enum):
    O, X = 0, 1

class Player:
    def __init__(self, playerId, playerName, symbol: PieceType):
        self.playerId = playerId
        self.playerName = playerName
        self.symbol = symbol
        self.losses = 0
        self.wins = 0

    def Win(self):
        self.wins += 1

    def Lose(self):
        self.losses += 1


class PlayerX(Player):
    def __init__(self,playerId, playerName,symbol = 'X'):
        super().__init__(playerId, playerName, symbol)

class PlayerO(Player):
    def __init__(self, playerId, playerName, symbol = 'O'):
        super().__init__(playerId, playerName, symbol)


class Game:
    def __init__(self, boardSize):
        self.board = None
        self.players = []
        self.moves = []
        self.turn = 0
        self.initialize(boardSize)
        self.boardSize = boardSize

    def Backtrack(self):
        lastMove = self.moves.pop()
        self.turn -= 1
        self.board = lastMove


    def initialize(self, boardSize):
        self.board = Board(boardSize)

    def startGame(self):
        self.board.printBoard()
        while True:
            print('row, col = ', end='')
            row, col = input().split()
            row, col = int(row), int(col)
            playingPiece = self.players[self.turn%len(self.players)]
            print(playingPiece.symbol, self.turn, len(self.players))
            move = self.board.addPiece(row, col, playingPiece)

            if not move:
                print('Invalid Move')
                continue

            self.moves.append(self.board)

            if self.isWinner(playingPiece):

                return

            if len(self.board.getFreeCells()) == 0:
                break

            self.turn += 1

        return 'Tie'


    def isWinner(self, playingPiece):
        for row in range(self.boardSize):
            count = 0
            for col in range(self.boardSize):
                if self.board.board[row][col] == playingPiece.symbol:
                    count += 1

            if count ==3:
                print(f'winner is {playingPiece.playerName}')
                playingPiece.Win()
                self.LeaderBoard()
                return True

    def LeaderBoard(self):
        print('Leadeboardr')
        for i in self.players:
            print(i.symbol, i.wins)
game =Game(4)
game.startGame()
