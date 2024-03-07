def is_palindrome(s):
    reversed_s = s[::-1]
    return s == reversed_s


s = input()
result = is_palindrome(s)
print(result)