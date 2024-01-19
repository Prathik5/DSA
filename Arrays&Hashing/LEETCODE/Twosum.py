def Twosum(nums, target: int):
    prevMap = {}  # ! So here we are declaring an empty hashmap

    for ind, val in enumerate(nums):
        # ! We here are taking the difference to fill the hashmap to decrease time complexity
        diff = target - val
        if diff in prevMap:
            print(prevMap[diff], ind)
            # ! We here are returning the index of the difference in hashmap and the index of iteration
            return [prevMap[diff], ind]
        # ! If it is not the desired element to return, we add this element into the hashmap and then look forward for the next element
        prevMap[val] = ind
    return


Twosum([2, 7, 11, 15], 9)
