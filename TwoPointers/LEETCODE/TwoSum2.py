
# todo: TWO SUM - II (NEETCODE 150, PROBLEM NUMBER - 167, MEDIUM)

# ? Here we are given a sorted list, that starts with index 1, and we have to return the indices of the elements that add upto the given target

# * Since we know that the list is sorted, we can make use of two pointers. We first go through the list from the left and check if it is smaller than the target, if it is go to the next element, if it is larger, move the right element to the next block behind it.

from inputs import TwoSumIIlist, TwoSumIITarget


def TwoSumII(nums: list[int], target: int) -> list[int]:

    L, R = 0, len(nums) - 1

    while L < R:
        curSum = nums[L] + nums[R]

        if curSum < target:
            L += 1
        elif curSum > target:
            R -= 1
        else:
            print([L + 1, R + 1])
            return [L + 1, R + 1]


TwoSumII(TwoSumIIlist, TwoSumIITarget)
