# TicTacToe-Project
The Repository for the TicTacToe project
Requirements:

Rules:
By default, the first move will be an X. It is up to the players to determine who goes first.
Choose a spot on the board by picking a number from 1-9
Spots on the board are oriented like this:

7
8
9
4
5
6
1
2
3


Try to make three in a row, and block your opponent from doing so; this is the objective of the game. 
If neither of you are able to do so, and all other squares are filled, the game will be a tie.
In both the situations mentioned above, the game will end. You will then be prompted if you want to repeat the game over. 




Design:
Classes:
GameLoopManager:
This is the main class we used to run the tic tac toe game. The other classes were put in as arguments, and we put the main functions of the skeleton code here. These were: gameLoop, playAgain, and gameItself.
Instance variables
Board: instance of the board
playerManager: instance of player manager
 gameItself 
function that we put most of the main “game loop” code into, and it actually uses the functions and runs the game. We had to edit out the primary if statement in order to remove the computer aspect of the game from the program, and only made use of the initial block of code, instead changing the “turn” variable we had created to change who was playing. 
gameLoop
 has the primary while statement(while true:) inside of it, and this function was created in order to sort out some errors and make it easier for us to allow the user to pick how many times they played. 
playAgain
 function was the unedited playAgain function we received in the skeleton code.
	
Board:
This is the class we put all board related functions into. We put: drawBoard, getBoardCopy, makeMove, isSpaceFree, isWinner, and resetBoard into this class. Every function except resetBoard is copied from the skeleton code. 

Instance variables
Board: the array that stores the board
resetBoard
a new function we created in order to reset the board, as that part was edited out of the game loop code that we changed. It simply consists of a for loop resetting all changes to the board.
getBoardCopy
The same function from the skeleton code, it creates a duplicate of the board, and returns it, to visually update the player to the game
makeMove
The same function from the skeleton code,  it takes parameters to define what the player wants to move as their turn
isSpaceFree
The same function from the skeleton code, it returns true if the space is open to be filled on the board
isWinner
The same function from the skeleton code, it checks every way the player can win every turn, and returns true if a player has won
drawBoard
The method draws the board onto the console. 
isBoardFull
Determines if the board is full by checking if there are any spaces left.


	


PlayerManager:
This class handles player-related functions and manages the turn state(x or o). It contains three functions: getPlayerMove, getLetter, and switchTurn
Instance variables
Turn_counter: a counter that manages the turns. 
getPlayerMove
Asks the player to input a number between 1 and 9, and returns and integer version of that number
getLetter
Returns the letter of the of the current turn(x or o), by looking at a specialized counter variable that keeps track of it
switchTurn
Changes the turn from x to o
