# Recursive and iterative implementations of factorial with explanatory comments.

def factorial_recursive(n: int) -> int:
    """
    Compute factorial(n) using recursion.
    - Raises TypeError if n is not an int.
    - Raises ValueError if n is negative.
    Examples:
        factorial_recursive(5) -> 120
    """
    if not isinstance(n, int):
        raise TypeError("factorial_recursive() expects an integer")
    if n < 0:
        raise ValueError("factorial_recursive() expects a non-negative integer")
    # Base case: 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return 1
    # Recursive step
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Compute factorial(n) using an iterative loop.
    - Raises TypeError if n is not an int.
    - Raises ValueError if n is negative.
    Examples:
        factorial_iterative(5) -> 120
    """
    if not isinstance(n, int):
        raise TypeError("factorial_iterative() expects an integer")
    if n < 0:
        raise ValueError("factorial_iterative() expects a non-negative integer")
    result = 1
    # Multiply result by each integer from 2 up to n
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    samples = [0, 1, 5, 10]
    for x in samples:
        print(f"{x}! recursive -> {factorial_recursive(x)}")
        print(f"{x}! iterative -> {factorial_iterative(x)}")

# Recursive and iterative implementations of factorial with explanatory comments.

def factorial_recursive(n: int) -> int:
    """
    Compute factorial(n) using recursion.
    - Raises TypeError if n is not an int.
    - Raises ValueError if n is negative.
    Examples:
        factorial_recursive(5) -> 120
    """
    if not isinstance(n, int):
        raise TypeError("factorial_recursive() expects an integer")
    if n < 0:
        raise ValueError("factorial_recursive() expects a non-negative integer")
    # Base case: 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return 1
    # Recursive step
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Compute factorial(n) using an iterative loop.
    - Raises TypeError if n is not an int.
    - Raises ValueError if n is negative.
    Examples:
        factorial_iterative(5) -> 120
    """
    if not isinstance(n, int):
        raise TypeError("factorial_iterative() expects an integer")
    if n < 0:
        raise ValueError("factorial_iterative() expects a non-negative integer")
    result = 1
    # Multiply result by each integer from 2 up to n
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    samples = [0, 1, 5, 10]
    for x in samples:
        print(f"{x}! recursive -> {factorial_recursive(x)}")
        print(f"{x}! iterative -> {factorial_iterative(x)}")