"""
AI-GENERATED TEST CASES & PRIME CHECK FUNCTION
---------------------------------------------

Justification for test cases:
1. Small primes: ensure basic correctness.
2. Small non-primes (0,1,negatives): check edge definition.
3. Simple composite: even number > 2 should fail.
4. Large primes: ensure performance and correctness.
5. Large composites: ensure algorithm rejects them.
6. Perfect square: must fail.
7. Prime near perfect square: ensures full divisor checking.
"""

# -------- is_prime IMPLEMENTATION -------- #

def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


# -------- AI-GENERATED TEST CASES -------- #

test_cases = {
    2: True,        # smallest prime
    3: True,        # next prime
    1: False,       # not prime
    0: False,       # edge case
    -5: False,      # negatives not prime
    4: False,       # simple composite
    97: True,       # mid-range prime
    7919: True,     # large prime
    100: False,     # composite with small factor
    9999: False,    # large composite
    49: False,      # perfect square
    47: True        # prime near perfect square
}

# -------- TEST RUNNER -------- #

print("RUNNING TESTS...\n")

all_passed = True

for n, expected in test_cases.items():
    result = is_prime(n)
    passed = (result == expected)
    all_passed &= passed
    print(f"n={n:5} | expected={expected} | got={result} | PASS={passed}")

print("\n--------------------------------")
print("ALL TESTS PASSED!" if all_passed else "SOME TESTS FAILED.")
print("--------------------------------")