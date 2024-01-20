
# todo: KADANE'S ALGORITHM(THIS IS A STANDARD ALGORITHM)
# ? Find the maximum sum of the sub array in the given array

# * So, how we go about it, first we assign the max sum as the first element in the array. Then later on we progress through the array, and then keep on adding it into the temporary array. Then, we check if the temporary sum is in negative, if it is we chuck it, and move on, if not we update the max sum. Later on we return this max sum

# * Time Complexity - O(n) : because we are looping through the array
# * Space complexity - O(n) : because we are creating another array

def KadanesAlgorithm(nums: list[int]) -> int:
    # ! Here we are initializing the max sum to be the first element, few people also assign it to be minus infinity
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        curSum = max(curSum, 0) + n
        maxSum = max(curSum, maxSum)
    print(maxSum)
    return maxSum


newList = [4, -1, 2, -7, 3, 4]
KadanesAlgorithm(newList)
