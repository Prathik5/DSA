
#  todo:    LARGEST CONSECUTIVE SEQUENCE (NEETCODE 150, PROBLEM NUMBER - 128, MEDIUM)

from inputs import LargestSequenceInput


def LargestSequence(nums: list[int]):
    numSet = set(nums)  # ! Here we are making the given array a set
    longest = 0  # ! We are initializing the longest consecutive sequence to be 0

    for n in nums:
        if (n - 1) not in numSet:  # ! We check if the number's previous number is in the set already or not
            length = 0  # ! This is to keep count of the sequence
            while (n + length) in numSet:
                length += 1  # ! Once the starting element is found, start counting
            # ! Take the max and then return the maximum one
            longest = max(length, longest)

    print(longest)
    return longest


LargestSequence(LargestSequenceInput)
