# ...existing code...
def reverse_string(s: str) -> str:
    """
    Return a new string which is the reverse of s.

    Examples:
        reverse_string("abc") -> "cba"
    """
    if not isinstance(s, str):
        raise TypeError("reverse_string() expects a str")
    return s[::-1]

if __name__ == "__main__":
    samples = ["hello", "", "A", "racer", "🙂👍", "abib"]
    for t in samples:
        print(f"'{t}' -> '{reverse_string(t)}'")
# ...existing code...