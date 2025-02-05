# Assignment Twenty-one

### You should know
- Arithmetic, functions
- Booleans, conditionals, None
- Strings
- Loops
- Tuples and lists

## Twenty-one

Make a script to play twenty-one using the building blocks you already learnt during this course. Write the script step by step, by identifying the necessary information and game flow. 
Tip: Playing the game might be of great help!

### Game rules

The aim of the game is to get the sum of your hand cards to be 21 or as close as possible to 21 from below to score more points than the bank. If the total of the values is greater than 21, the player loses the game. 

* There is one bank with whom the players compete 
* There is at least 1 player. For this assignment it is sufficient to program the game for one player.
* All cards are worth their own value. A king is worth 3, a queen 2 and a jack (boer) 1.
* Ace is worth 1.
* Cards 2-6 and the jokers are not used
* The color of the card is not important.


### Game flow

The bank and all players get two cards. One is open, the other one closed (face down). The players place a bet withouth looking at the second card. They can only see the second card after placing the bet. The bet is not fixed, as they can increase the bet after every new card. Lowering the bet however, is not possible. During their turn, all players can ask cards from the bank until the point they pass, reach a total of 21 or exceed 21. When all players had their turn, it is up to the bank. The bank shows their second card. If the cards of the bank sum to 16 or lower, the bank takes another card. If the sum is 17 or higher, the bank passes. If the bank is finished, the round ends. 

All players with a score greater than the score of the bank win and receive the double of their bet. All players with a score equal to the score of the bank, get their bet back. All players with a score lower than the bank or higher than 21, lose their bet.

### Requirements
* Provide sufficient feedback and interaction so the players know what to do.
* A player starts with 250 euro in their wallet



<details>
    <summary > <font size="+1"> Getting started</font></summary>

* Identify the aim of the game
* Gather important information from the assignment and game rules.
* Identify the different steps of the game. Go into detail. It might help to play the game and note every step a player or bank takes.
* Create a scheme of the game flow and steps.

If you finished your scheme. Search for things you can link to programming concepts (information to store, repeated actions, ...). Which building blocks will you use? After laying out the structure, you can start programming.

1. Program the functions you identified.
2. Game setup (preparation before the actual start of the game.)
3. Game flow (Playing the game)
4. End


### Tip
* If this exercise is overwhelming to you, break it into parts using the guidelines above. 
* At a certain point you will need a function to change the order of x. Search the internet for a function and read the section below about modules and packages.

</details>

<details>
    <summary > <font size="+1"> Modules and packages</font></summary>

At a certain point you will need a function to change the order of x. This function is already programmed by someone else and available to you. In order to use that function, we need to import a module.

### Module
- A python file (.py) containing Python definitions and statements (collections of functions and global variables)
- example: import math, import random, os …
- Purpose: code organization 
- Use: 

	Say we have a file fibo.py with two functions fib(n) and fib2(n)
    ```Python
    import fibo #to import the module fibo
    #usage
    fibo.fib(500)
    ```

    To import the names fib, fib2 into the local namespace:
    ```Python
    from fibo import fib, fib2
    #usage
    fib(500)
    fib2(500)
    #fibo is not defined in the namespace
    ```
    
    ```Python
    #Importing all modules
    from fibo import *

    #Importing using a shorter name for the module
    import fibo as fb
        #usage
    fb.fib(500)
    
    #Importing using a different name for the function
    from fibo import fib as fibonacci
        #usage
    fibonacci(500)
    ```
- Python has built-in modules (`import sys`)

### Package

- A way of structuring Python’s module namespace by using “dotted module names”:
    A.B a submodule named B in a package named A
- Collection of different modules with an `_init_.py` file. Related modules in a directory hierarchy, multiple sub-modules and sub-packages.
- Use of dotted module names: No need to worry about variable names of other modules/packages
- Purpose: code distribution and reuse, F.e: `import numpy, pandas, matplotlib`
	`Import matplotlib.pyplot as plt`
-	`Import sound.effects.echo` (sound: package, effects: subpackage, echo: module)

Installing packages: We use pip to install new packages from the web. After installing pip, you can type in your terminal: `pip install ‘package name’`.


</details>

<details>
    <summary > <font size="+1"> Example output</font></summary>


    First card player: 3
    First card bank: 1
    __________________________
    Player's turn
    First card:  3
    Place a bet, enter a positive value:20
    Second card:  10
    Total of cards:  13

    Do you want another card or do you want to stop?
    If you whish to higher your bet, type a value. Type 0 to keep your current bet:50
    Your current bet: 70, wallet saldo: 180
    Your new card: 7
    Sum of your cards: 20

    Do you want another card or do you want to stop?stop
    ____________________________
    BANK IS PLAYING
    first card: 1
    second card: 1
    total of cards: 2

    Bank continues

    Your new card: 1
    Sum of your cards: 3

    Bank continues

    Your new card: 2
    Sum of your cards: 5

    Bank continues

    Your new card: 1
    Sum of your cards: 6

    Bank continues

    Your new card: 9
    Sum of your cards: 15

    Bank continues

    Your new card: 1
    Sum of your cards: 16

    Bank continues

    Your new card: 1
    Sum of your cards: 17

    Bank passes
    Player won 140 coins, new wallet balance: 320
</details>