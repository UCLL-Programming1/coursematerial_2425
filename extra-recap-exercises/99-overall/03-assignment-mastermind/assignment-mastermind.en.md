# Mastermind

Mastermind consists in finding a secret code. This code consists of an indefinite number of digits. For this, you are allowed to make multiple guesses. For each guess you get feedback in the form of two numbers :

* The first number indicates how many digits you guessed correctly.
* The second number is the number of digits that appear in the code, but in a different place.

Suppose the code is 1 2 3 4 and you guess 1 5 3 2. The feedback you get on this is 2 1 :

* The first digit 1 is correct and is in the correct position, as is the third digit 3.
* The second digit 2 of the code does occur in your guess, but in your guess it is in the fourth position instead of the second.

### `TASK`
Write a function `mastermind(code, guess)` that, given two lists of numbers code and guess, returns the feedback as a list of two numbers.


#### USAGE

```python
>>> mastermind([],[])
[0,0]

>>> mastermind([1],[1])
[1,0]

>>> mastermind([1],[2])
[0,0]

>>> mastermind([1,2],[2,1])
[0,2]

>>> mastermind([1,2],[1,1])
[1,0]

>>> mastermind([1,1,1],[1,1,2])
[2,0]

>>> mastermind([1,2,3,4],[1,3,2,4])
[2,2]
```



