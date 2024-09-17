# All Equal

### `TASK`

Write a function `all_equal(xs)` that returns `True` if all elements of `xs` are equal to each other, `False` otherwise.

#### `HINT 1`

Equality is transitive, meaning that if `a == b` and `b == c`, you get `a == c` for free.

#### `HINT 2`

Check that `xs[0] == xs[1]`, then `xs[1] == xs[2]`, and so on until the end.

#### `HINT 3`

Say `xs` contains 5 elements.
You will then need to perform the following comparisons:

- `xs[0] == xs[1]`
- `xs[1] == xs[2]`
- `xs[2] == xs[3]`
- `xs[3] == xs[4]`

We can generalize this to simply `xs[i] == xs[i+1]` with `i` going from `0` to `3`.
