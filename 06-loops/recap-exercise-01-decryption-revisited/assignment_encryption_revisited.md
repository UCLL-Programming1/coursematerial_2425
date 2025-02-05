# Assignment encryption (revisited)

### You should know
- Arithmetic, functions
- Booleans, conditionals, None
- Strings
- Loops

Revisit the encryption recap exercise of the previous chapter. In that exercise you implemented 4 different decryption strategies. We're going to build on this work in this exercise.

### Strategy 5

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
