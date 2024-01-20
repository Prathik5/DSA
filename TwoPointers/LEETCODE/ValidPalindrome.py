
# todo: VALID PALINDROME(NEETCODE 150, PROBLEM NUMBER - 125, EASY)

# ? Here we are given a set of alphanumeric characters/ String. We have to check whether this string is palindrome or not.

# * So, to check the first and the last element we can use two pointers and it becomes easy. We are told we have to check for only alphanumeric characters, we can ignore the spaces and stuff. So check for that case as well.

from inputs import validPalindromeInput1, validPalindromeInput2


def validPalindrome(s: str) -> bool:
    L, R = 0, len(s) - 1

    while L < R:
        # ! Here we use isalnum to check whether it is an alphanumeric character
        while L < R and s[L].isalnum() == False:
            L += 1
        while L < R and s[R].isalnum() == False:
            R -= 1

        if s[L].lower() != s[R].lower():
            print("False")
            return False
        else:
            L += 1
            R -= 1
    print("TRUE")
    return True


validPalindrome(validPalindromeInput1)
validPalindrome(validPalindromeInput2)
