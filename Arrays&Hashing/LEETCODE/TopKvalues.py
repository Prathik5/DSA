def TopKValues(nums: list[int], k: int):

    hashmap = {}
    freq = [[] for i in range(len(nums) + 1)]

    for i in nums:
        # ! This is how you count each character in a hashmap
        hashmap[i] = 1 + hashmap.get(i, 0)
    for num, cnt in hashmap.items():  # ! This is a loop to add the number of elements repeating how many ever times in the array that position
        # ! Here we appended that number in the index of count in frequency array
        freq[cnt].append(num)

    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:  # !This for loop is because every item inserted in the frequency is an array, so you gotta get that elements
            res.append(n)
            if len(res) == k:
                print(res)
                return res


TopKValues([1, 1, 1, 2, 2, 8, 1, 5, 5, 7, 8, 3,
           3, 3, 1, 4, 7, 8, 9, 12, 3, 3], 4)
