
# todo: TWO POINTERS

# ? Here we are given a list of SORTED integers, we have to traverse through it and find the indices whose elements add upto the  target sum. There exists exactly one solution

# * How we go about is, We initialize two pointers, left and right, and then we go through. First we check the sum of the first and last element, if it is greater than target, we move the right pointer left side by one step. If it is lesser than the target sum, we move the left pointer by one step to the right. We continue doing this until we find the right answer.

def TwoPointer(nums: list[int], target: int) -> list[int]:
    L, R = 0, len(nums) - 1

    while L < R:
        if nums[L] + nums[R] > target:
            R -= 1
        elif nums[L] + nums[R] < target:
            L += 1
        else:
            print([L, R])
            return [L, R]


TwoPointer([1, 2, 3, 4, 7, 9], 7)
