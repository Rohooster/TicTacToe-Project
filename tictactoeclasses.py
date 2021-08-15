#GameLoopManager
#   game loop function
#   playAgain

import random

class GameLoopManager:
    def __init__(self):
        self.board = Board()
        self.playerManager = PlayerManager()


    #List of things to edit on this large annoying function
    '''Replace getBoard as see fit
    Completely remove all computer aspects from the game GameLoop
    Change the turn if else statement because the turns are taken by a different function(add that in too)
    Replace whogoesfirst implementation
    
    '''
    def gameLoop(self):
        print('Welcome to Tic Tac Toe!')

        while True:
            # Reset the board
            turn = self.playerManager.getLetter()
            print(f'The player using letter {turn} will go first.')
            gameIsPlaying = True

            while gameIsPlaying:
                turn = self.playerManager.getLetter()
                if turn == 'X':
                    self.board.drawBoard(self)
                    move = self.playerManager.getPlayerMove(self.board.isSpaceFree)
                    self.board.makeMove(turn, move)

                    if self.board.isWinner(turn):
                        self.board.drawBoard()
                        print(f'Hooray! Player {turn} has won the game!')
                        gameIsPlaying = False
                    else:
                        if self.board.isBoardFull():
                            self.drawBoard()
                            print('The game is a tie!')
                            break
                        else:
                            self.playerManager.switchTurn()

                else:
                    # TODO tomorrow
                    move = getComputerMove(theBoard, computerLetter)
                    makeMove(theBoard, computerLetter, move)

                    if isWinner(theBoard, computerLetter):
                        drawBoard(theBoard)
                        print('The computer has beaten you! You lose.')
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'player'

            if not self.playAgain():
                break

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')


#Board
#   We will need an array for this class, as we need a board to work these on XXX
#   board generator(display) XXX
#   add a letter to the board(makemove) XXX
#   getBoardCopy XXX
#   isSpaceFree XXX
#   chooseRandomMoveFromList(validate move) XXX
#   isBoardFull XXX
#   isWinner XXX


class Board:
    def __init__(self):
        self.board = [' '] * 10

    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')


    def getBoardCopy(self):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in self.board:
            dupeBoard.append(i)

        return dupeBoard

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(self.board, i):
                return False
        return True

    def isWinner(self, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.

        return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or  # across the top
                (self.board[4] == le and self.board[5] == le and self.board[6] == le) or  # across the middle
                (self.board[1] == le and self.board[2] == le and self.board[3] == le) or  # across the bottom
                (self.board[7] == le and self.board[4] == le and self.board[1] == le) or  # down the left side
                (self.board[8] == le and self.board[5] == le and self.board[2] == le) or  # down the middle
                (self.board[9] == le and self.board[6] == le and self.board[3] == le) or  # down the right side
                (self.board[7] == le and self.board[5] == le and self.board[3] == le) or  # diagonal
                (self.board[9] == le and self.board[5] == le and self.board[1] == le))  # diagonal

#PlayerManager
#   GetPlayerMove
#   switch_turns(not done yet)

class PlayerManager:
    #make sure you edit functions
    def __init__(self):
        self.turn_counter = 0

    # try passing things that are not available as args to function first before making instance vars:)
    def getPlayerMove(self, isSpaceFree):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(move):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def getLetter(self):
        #implementation goes here
        if self.turn_counter == 0:
            return 'X'
        else:
            return 'O'

    def switchTurn(self):
        self.turn_counter = 1 - self.turn_counter




#Functions we will remove:
#   getComputerMove
#   whoGoesFirst
#   inputPlayerLetter









