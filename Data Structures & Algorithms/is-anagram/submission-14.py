class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = {}
        for i in s:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1

        print(d1)

        for i in t:
            if i in d1:
                d1[i] -= 1
                if d1[i] == 0:
                    del d1[i]


        print(d1)

        if len(d1.keys()) == 0:
            return True
        else:
            return False


        