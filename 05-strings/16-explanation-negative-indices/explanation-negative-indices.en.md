# Negative Indices

For your convenience, Python allows you to use negative indices.
This equivalence holds:

```python
string[-index] == string[len(string) - index]
```

In other words, a negative index starts counting from the end.

### `EXAMPLE`

```python
>>> string = "abcd"
>>> string[-1]
"d"

>>> string[-2]
"c"
```
