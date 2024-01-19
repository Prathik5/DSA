from collections import defaultdict
from inputs import groupAnagramsInput


def GroupAnagram(strs: list[str]):
    # ! Very Important, here we are declaring a hashmap which will have values in them as list, this is how you define them
    res = defaultdict(list)

    for s in strs:
        # ! Here you are initializing an array, which will go inside the hashmap, just like we did for the hasharray
        count = [0] * 26

        for c in s:
            # ! Now we are inserting the values one by one in the array.
            count[ord[c] - ord["a"]] += 1

        # ! Here, you are appending the value s in the index count in res wala hashmap, since res is a dict(list) wala map, it takes only tuples as inputs, so tuples
        res[tuple(count)].append(s)

    print(res.values)
    return res.values()


GroupAnagram(groupAnagramsInput)
