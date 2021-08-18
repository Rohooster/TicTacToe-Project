"""
This is the main class we used to run the tic tac toe game.
The other classes were put in as arguments, and we put the
main functions of the skeleton code here. These were:
gameLoop, playAgain, and gameItself.
"""


class GameLoopManager:
    def __init__(self):
        self.board = Board()
        self.playerManager = PlayerManager()

    # function that we put most of the main “game loop”
    # code into, and it actually uses the functions and runs the game.
    def gameItself(self):
        gameIsPlaying = True

        while gameIsPlaying:
            # Sets turn
            turn = self.playerManager.getLetter()
            # creates board and sets it up, move cycle happens
            self.board.drawBoard()
            move = self.playerManager.getPlayerMove(self.board.isSpaceFree)
            self.board.makeMove(turn, move)
            # if winner is detected, this runs
            if self.board.isWinner(turn):
                self.board.drawBoard()
                print(f'Hooray! Player {turn} has won the game!')
                gameIsPlaying = False
            # in case of a tie, this runs
            else:
                if self.board.isBoardFull():
                    self.drawBoard()
                    print('The game is a tie!')
                    break
                # switches turn if there is no win and its not a tie
                else:
                    self.playerManager.switchTurn()

    # has the primary while statement(while true:) inside of it,
    # and this function was created in order to sort out some errors
    # and make it easier for us to allow the user to pick how many times they played.
    def gameLoop(self):
        print('Welcome to Tic Tac Toe!')

        while True:
            # Reset the board
            self.board.resetBoard()
            # switches turn
            turn = self.playerManager.getLetter()
            print(f'The player using letter {turn} will go first.')
            # runs the actual game
            self.gameItself()
            # checks if user wants to play again
            if not self.playAgain():
                break

    # function was the unedited playAgain function we received in the skeleton code.
    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')


"""
This is the class we put all board related functions into. 
We put: drawBoard, getBoardCopy, makeMove, isSpaceFree, isWinner, 
and resetBoard into this class; every function except resetBoard 
is copied from the skeleton code. 
"""


class Board:
    def __init__(self):
        # instance variable, maintains the state of the board.
        self.board = [' '] * 10

    # The method draws the board onto the console.
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

    # getBoardCopy creates a duplicate of the board and returns it to visually update the player to the game
    def getBoardCopy(self):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        # gets the values of the board
        for i in self.board:
            dupeBoard.append(i)

        return dupeBoard

    # makeMove takes parameters to define what the player wants to move as their turn
    def makeMove(self, letter, move):
        self.board[move] = letter

    # isSpaceFree returns true if the space is open to be filled on the board
    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[int(move)] == ' '

    # Determines if the board is full by checking if there are any spaces left.
    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

    # isWinner checks every way the player can win every turn, and returns true if a player has won
    def isWinner(self, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use le instead of letter so we don't have to type as much.

        return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or  # across the top
                (self.board[4] == le and self.board[5] == le and self.board[6] == le) or  # across the middle
                (self.board[1] == le and self.board[2] == le and self.board[3] == le) or  # across the bottom
                (self.board[7] == le and self.board[4] == le and self.board[1] == le) or  # down the left side
                (self.board[8] == le and self.board[5] == le and self.board[2] == le) or  # down the middle
                (self.board[9] == le and self.board[6] == le and self.board[3] == le) or  # down the right side
                (self.board[7] == le and self.board[5] == le and self.board[3] == le) or  # diagonal
                (self.board[9] == le and self.board[5] == le and self.board[1] == le))  # diagonal

    # resetBoard consists of a for loop resetting all changes to the board.
    def resetBoard(self):
        for x in range(1, 10):
            self.board[x] = ' '


"""
THIS class handles player-related functions and manages the turn state(x or o).
It contains three functions: getPlayerMove, getLetter, and switchTurn 
"""


class PlayerManager:
    def __init__(self):
        # class variable, manages turn
        self.turn_counter = 0

    # Asks the player to input a number between 1 and 9, and returns and integer version of that number
    def getPlayerMove(self, isSpaceFree):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(move):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    # Returns the letter of the of the current turn(x or o),
    # by looking at a specialized counter variable that keeps track of it
    def getLetter(self):
        # implementation goes here
        if self.turn_counter == 0:
            return 'X'
        else:
            return 'O'

    # Changes the turn from x to o
    def switchTurn(self):
        self.turn_counter = 1 - self.turn_counter
