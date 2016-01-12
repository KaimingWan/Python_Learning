__author__ = 'Kaiming'


def is_palindrome(s):
    s = str(s)
    for n in range(len(s)):
        if s[n] != s[len(s) - 1 - n]:
            return False
    return True


output = filter(is_palindrome, range(1, 1000))
print(list(output))
