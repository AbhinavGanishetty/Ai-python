
# ...existing code...
def is_prime(n: int) -> bool:
    """
    Return True if n is a prime number, otherwise False.

    Examples:
        is_prime(2) -> True
        is_prime(15) -> False
    """
    if not isinstance(n, int):
        raise TypeError("is_prime() expects an integer")
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    sample = [0, 1, 2, 3, 4, 17, 18, 19, 20, 7919]
    for x in sample:
        print(f"{x}: {is_prime(x)}")