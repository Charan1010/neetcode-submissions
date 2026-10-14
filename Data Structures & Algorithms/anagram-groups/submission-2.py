class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = {}
        for st in strs:

            sorted_st = "".join(sorted(st))

            if sorted_st in anagram:
                anagram[sorted_st].append(st)
            else:
                anagram[sorted_st] = [st]

        return list(anagram.values())