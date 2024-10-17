# Assignment encryption-decryption

### You should know
- Arithmetic, functions
- Booleans, conditionals, None
- Strings


## Decrypting messages

Two pupils have developed their own encryption system to secretly pass messages to each other in class. It is up to you to write functions decrypting their texts based on their different methods. 

### Strategy 1
Their first strategy is to replace all o’s with A’s. Write a function `decode1(word)` to decipher the word (crack the code) returning the original word.

```python
>>> decode1("SchAAl")
"School"
```

<details>
    <summary > <font size="+1"> Understanding the assignment</font></summary>

Before reading the specific encryption methods and thinking about how to decipher them, it is important to fully understand the assignment.

We are talking about **encrypting and decrypting** words. But what does that mean? What is the encrypted word and what the decrypted? And the original one? 

#### Explanation encryption-decryption
We have a word, say “duck”, we want to encrypt. The encryption method we use is to reverse the order of the letters, therefore the encrypted word is “kcud”. To go back from this encrypted word “kcud”, we apply the process of decryption. The resulting decrypted word is “duck”, the same word as the original one. Encrypting and decrypting are reversed processes. 

![example duck](scheme1.png)

In this example we encrypted the word by reversing the order of the letters. How do we decrypt the word?

<details>
<summary>Show answer</summary>
Reversing the order of the letters again.
</details>
<br>
The pupils did the process of encryption, we need to write code to decrypt the words. Let’s fill in the scheme.

![scheme](scheme2.png)
</details>
<br>
Write your code in the file student.py

### Strategy 2
As their messages could easily be cracked by the teacher and other students, they implemented another strategy. Every letter of the word was followed by another random letter. 

Write a function `decode2(word)` to decrypt the coded message.

```python
>>> decode2("hqovtzdpozgm")
"hotdog"
```

<details>
<summary> Hint </summary>
<mark>h</mark>q<mark>o</mark>v<mark>t</mark>z<mark>d</mark>p<mark>o</mark>z<mark>g</mark>m
</details>

### Strategy 3
Their third strategy is to reverse the first word of a sentence.

```python
>>> decode3("sepocseleT are too expensive.")
"Telescopes are too expensive."
```

### Strategy 4
Their newest strategy, is their most successful, according to them. The word itself is not shuffled nor injected with other letters. Letters are merely added before and after the word. The original word is half as long as the encrypted word and hidden within the encrypted word. The first letter of the original word is the third letter of the encrypted word. Write a function `decode4(word)`to decrypt the encrypted word.

```python
>>> decode4("oddolfijnnjifl")
"dolfijn

>>> decode4("oddolfijnnjiflK")
"dolfijn

```

### Strategy 5
*For this exercise you need to be familiar with loops.*

To ensure the secrecy of their messages, the pupils decide to combine their 4 strategies. First they apply strategy 3, followed by strategy 4, strategy 2 and lastly strategy 1. Write a function `decode5(sentence)`, that takes as input an encrypted sentence and returns the decrypted or original sentence. Use the functions you already defined to limit duplicated code in `decode5(sentence)`.

Hint: think about the encryption-decryption scheme.

```python
sentence = "MDEneEdU oAXnkgaCteJE vMtokdrHarpltSKuspcc aaaudAev xzsRkVrSoDlolMernyFZpRHQDdkX QggivNajnoQU youKdSeq lnegtwrvatpeXeUu"       

>>> decode5(sentence)
"de kat krapt de krollen van de trap"

sentence = "rAxNejhfTrns maGwcaifrIcRuEmzsHtxaUnVcSeWsllKnmsYiMiFwQpMZyRhabPu aHhPhyajvfeViSYg xrfAcphhadnqgIeodAAXyDjTcFGT"

>>> decode5(sentence)
"The circumstances have changed"
```

## Encryption

If you want to challenge yourself, you can try to create functions to encode words using these strategies. Name the functions `encode1(word)`, `encode2(word)` etc. You can correct your encryption codes by decrypting the results. Does it return the original word?

```python
>>> word = "duck"
>>> encoded = encode1(word)
>>> result = decode1(encoded)
>>> result == word
True
```
