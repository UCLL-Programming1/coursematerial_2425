# Slicing

Say you want the first three characters in a string:

```python
string = "abcdef"
first_three = string[0] + string[1] + string[2]
```

While this code works, it is very cumbersome.
_Slicing_ will make this process much simpler:

```python
string = "abcdef"
first_three = string[0:3]
```

When indexing using something of the form `i:j`, you will get the substring that ranges from index `i` up to index `j`.

## `IMPORTANT`

Note that the slice `string[i:j]` does _not_ include the character at index `j`.

There are a few variations on this syntax:

| Syntax  | Description                                           |
| ------- | ----------------------------------------------------- |
| `s[:j]` | Same as `s[0:j]`                                      |
| `s[i:]` | Same as `s[i:len(s)]`                                 |
| `s[:]`  | Same as `s[0:len(s)]`, i.e., returns the whole string |

## Steps

It is also possible to specify a step: `s[start:end:step]`.

```python
>>> "abcdefg"[::2]
"aceg"
```

Negative steps allow you to reverse the substring:

```python
>>> "abcd"[::-1]
"dcba"

>>> "abcdefg"[4:2:-1]

```
