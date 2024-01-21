
# todo: THREE SUM(NEETCODE 150, PROBLEM NUMBER - 15, MEDIUM)
# ? Here we have to return triplets list which contains the numbers which sum upto 0. We can't repeat the triplets in the array. And the order doesn't matter. Just don't repeat.

# * TO solve this, we first sort the given array, so that we can use two pointers on them. Once we are sure that they are sorted, and have solution, we can run some pointers around and check if they sum upto 0.

# * Time complexity - O(nlogn) + O(n^2) => O(n^2)......because we don't care about nlogn because it's a smaller value as compared to n^2

# * Space Complexity = O(n)......as we create another array and append the triplets to it

from inputs import threeSumList


def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    for ind, val in enumerate(nums):
        # ! Here we are checking if the left and the right index are having the same number, if so, we just continue.
        if ind > 0 and val == nums[ind - 1]:
            continue
        L, R = ind + 1, len(nums) - 1

        while L < R:
            threesumS = val + nums[L] + nums[R]

            if threesumS < 0:
                L += 1
            elif threesumS > 0:
                R -= 1
            else:
                res.append([ind, nums[L], nums[R]])
                # ! Here we are moving ahead and going to the next ones
                L += 1
                R -= 1
                while nums[L] == nums[L - 1] and L < R:
                    L += 1
    print(res)
    return res


threeSum(threeSumList)
