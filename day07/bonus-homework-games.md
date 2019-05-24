## PYTHO02 Week 4 Bonus Challenge: Games


### 1. Hangman
- Define a secret word, for example 'COWBOY'. Show the user a string a blank characters that indicate which letters they have guessed, for example `_ _ _ _ _ _` at the start of the game, `_ O _ _ O _` if they have guessed 'O' correctly, etc.
- Ask the user to guess a letter. If they guess correctly, congratulate them. If they guess incorrectly, show them an ASCII art drawing (google it) of a man being hung. The drawing should have one part finished if they have guessed wrong once, two parts finished if they have guessed wrong twice, etc (I suggest keeping the different stages of the drawing in a list of strings).
- If the user guesses correctly before the man hangs, congratulate them. If not, they must behold the full spectacle of the ASCII man hanging from the gallows.
- Note that you should write a solution that works for _any_ secret word, i.e. don't hardcode the letters or length of the secret word into your solution.

### 2. Tic Tac Toe
- Create a 2-player version of the classic game ("takes only seconds to learn, but minutes to master"), which will ask each user for their move, show the current board layout after each move, and detect when a user has won the game or the game ends in a draw. It should also prevent a user from playing a move into a square that is already occupied.
- Print a 3 x 3 empty game board and ask the user for the position of their move (it's up to you to decide how they specify the position coordinates for their move). Determine if the specified move is legal, and if so, whether it wins the game. If the game is won, print a congratulatory message. Otherwise, print the new state of the board and ask the other user for their move, and so on until the end of the game.
- ADVANCED: create a one-person version of the game where the user plays against the computer. The code you write for the computer's moves can use strategies from simple and dumb (random moves), to more clever (looking for any better-than-average moves which are still available) to sophisticated and unbeatable ('minimax' recursive algorithm to generate tree of all possible future moves from current board state and give each one a score, to determine best move). Start from the simplest and work your way up, if you're interested in this version!
*HINTS:*
- Use functions to break down the different parts of the game! One function to draw the game board or hangman state, one function to get input from the user and validate it, one function to check if a move is legal or if the guessed letter is correct, etc.
- When testing your game code, fake a game by calling a play_move() function repeatedly to simulate a game of specific moves. Don't add the actual user input until the end - otherwise it will take too long to test your game repeatedly.
- Use `.format()` to display the tic tac toe board!
