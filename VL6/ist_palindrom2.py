def is_palindrome(s: str) -> bool:
    return s == s[::-1]

print("anna?", is_palindrome("anna"))
print("antna?", is_palindrome("antna"))
print("otto?", is_palindrome("otto"))
print("Anna?", is_palindrome("Anna"))
print("gnubelebung?", is_palindrome("gnubelebung"))