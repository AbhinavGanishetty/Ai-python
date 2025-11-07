# ...existing code...
def largest_in_list(iterable):
    """
    Return the largest item in iterable.
    - Accepts any non-empty iterable of comparable items.
    - Raises TypeError if input is not iterable or items are not mutually comparable.
    - Raises ValueError if iterable is empty.
    Time: O(n), Space: O(1)
    """
    try:
        it = iter(iterable)
    except TypeError:
        raise TypeError("largest_in_list() expects an iterable")

    try:
        max_val = next(it)
    except StopIteration:
        raise ValueError("largest_in_list() expects a non-empty iterable")

    for x in it:
        try:
            if x > max_val:
                max_val = x
        except TypeError:
            raise TypeError("Elements of iterable are not mutually comparable")
    return max_val


def largest_in_list_builtin(iterable):
    """
    Simpler version using Python builtin max().
    Raises the same exceptions for empty or non-iterable inputs.
    """
    return max(iterable)  # max will raise TypeError/ValueError appropriately


if __name__ == "__main__":
    samples = [
        [3, 1, 4, 1, 5],
        [-10, -2, -30],
        [42],
    ]
    for s in samples:
        print(s, "->", largest_in_list(s))
    # demonstration of builtin
    print("builtin max ->", largest_in_list_builtin([1, 9, 2]))