# Assignment Tic Tac Toe

### You should know
- Arithmetic, functions
- Booleans, conditionals, None
- Strings
- Loops
- Tuples and lists
- Sets

## Tic Tac Toe
Your task is to create a Tic Tac Toe game that can be played in the terminal by two players. Write the script step by step, by identifying the necessary information and game flow. 
Tip: Playing the game might be of great help!

### Game Rules
Tic Tac Toe is a two-player game on a 3x3 grid. Players take turns placing their symbol on the board, aiming to align three symbols in a row, column, or diagonal. If neither player manages to align three symbols and the board is full, the game ends in a tie.

### Requirements
* Display the game board as a 3x3 grid
* Each player should be able to enter their name and choose a unique symbol (tick).
* Players should take turns to place their symbol in an empty cell by entering the cell’s index (0-8).
* The game should check for a winner after each move and announce if a player has won or if the game is a tie.
* If a player selects an occupied cell, instruct them to choose a different cell.

EXTRA
* Display a grid with the indices to make it easier for the players to choose the right index.
* Implement input validation to ensure only valid integers (0-8) are accepted for cell selection.

<details> <summary><font size="+1">Getting started</font></summary>
If you're unsure how to start, try playing Tic Tac Toe on paper to understand the game flow. Use comments to outline the game structure and break down the code into smaller functions.

</details>

<details> <summary><font size="+1">Example output</font></summary>

    Please enter the name of player 1: Joske
    Joske, choose a tick: * 
    Please enter the name of player 2: Fien
    Fien, choose a tick: O
      |   |
      |   |
      |   |

    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8

    Fien, it is your turn.
    Enter the index of the field you would like to place your tick on: 0

    O |   |
      |   |
      |   |

    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8

    Joske, it is your turn.
    Enter the index of the field you would like to place your tick on: 1

    O | * |
      |   |
      |   |

    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8

    Fien, it is your turn.
    Enter the index of the field you would like to place your tick on: 2

    O | * | O
      |   |
      |   |

    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8

    Joske, it is your turn.
    Enter the index of the field you would like to place your tick on: 3

    O | * | O
    * |   |
      |   |

    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8

    Fien, it is your turn.
    Enter the index of the field you would like to place your tick on: 4

    O | * | O
    * | O |
      |   |

    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8

    Joske, it is your turn.
    Enter the index of the field you would like to place your tick on: 5

    O | * | O
    * | O | *
      |   |

    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8

    Fien, it is your turn.
    Enter the index of the field you would like to place your tick on: 7

    O | * | O
    * | O | *
      | O |

    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8

    Joske, it is your turn.
    Enter the index of the field you would like to place your tick on: 6

    O | * | O
    * | O | *
    * | O |

    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8

    Fien, it is your turn.
    Enter the index of the field you would like to place your tick on: 8

    O | * | O
    * | O | *
    * | O | O

    Fien won!

</details>