
# todo: LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS(NEETCODE 150, PROBLEM NUMBER - 3, MEDIUM)

# ? Here we are given a set of characters in a string, we have to look for the longest substring in the string, where the characters do not repeat.

# * To solve this we use sliding window approach, we assign two pointers and slide the pointers to check until we get a repeated value. So once we hear repeated value and stuff, we have to use set or more particularly hashset to solve this, we store values in hashset and check if the next value in the window are already in the set, if they are there, we terminate the window and move on to the next ones.

# * Time complexity - O(n)

# * Space complexity - O(n)

def longestSubString(s: str) -> int:
    charSet = set()
    l = 0  # ! here we are initializing the left pointer
    maxLength = 0  # ! Initializing the maxlength

    for r in range(len(s)):
        while s[r] in charSet:  # ! To check if the value already exists
            charSet.remove(s[l])  # ! If it exists remove that
            l += 1  # ! Since it already exists, move the left pointer ahead
        charSet.add(s[r])  # ! If it doesn't exist add it to the set

        # ! Checking the max length of the charset, the best way is to calculate the difference between the right pointer and left pointer, we add 1 because indexing starts with 0
        maxLength = max(maxLength, r - l + 1)

    print(maxLength)
    return maxLength


longestSubString("abcabcabc")
