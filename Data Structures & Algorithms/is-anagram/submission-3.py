class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d_s = {}

        for ele in s:
            if ele in d_s:
                d_s[ele] += 1
            else:
                d_s[ele] = 1

        d_t = {}

        for ele in t:
            if ele in d_t:
                d_t[ele] += 1
            else:
                d_t[ele] = 1

        #print(d_s)
        #print("----------------")
        #print(d_t)

        return d_s == d_t
        