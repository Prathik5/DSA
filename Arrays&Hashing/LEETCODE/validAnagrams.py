def isAnagram(s, t):
    # *Step 1 :  First we check if the length of both the strings are same, else there is no point actually lol
    if len(s) != len(t):
        return False

    # * Now declare the hashmaps
    countT, countS = {}, {}

    # * Step 2 :  initialize this hashmap
    for i in range(len(s)):
        # ? Idu en andre countS alli hakiro string du first letter togondu store madu anta, get method yake hakidivi andre, starting alli 0 iratte alwa, so error baratte adikke
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

# * Step 3 : Now we are checking if the given input is in the hashmap
    for c in countS:
        if countS[c] != countT.get(c, 0):
            print("False")
        else:
            print("True")


isAnagram("car", "tar")
