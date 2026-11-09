def is_palindrome(s: str) -> bool:
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - 1 - i]: # mismatch gefunden!
            return False
    return True

print("anna?", is_palindrome("anna"))
print("antna?", is_palindrome("antna"))
print("otto?", is_palindrome("otto"))
print("Anna?", is_palindrome("Anna"))
print("gnubelebung?", is_palindrome("gnubelebung"))