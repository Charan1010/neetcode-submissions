class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_hist = {}

        for ele in strs:

            sorted_ele = "".join(sorted(ele))

            if sorted_ele in anagram_hist:
                anagram_hist[sorted_ele].append(ele)
            else:
                anagram_hist[sorted_ele] = [ele]

        return list(anagram_hist.values())
        
