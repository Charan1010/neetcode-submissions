class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs_sorted_dict = {}

        for st in strs:

            key = str(sorted(st))

            if key in strs_sorted_dict.keys():
                strs_sorted_dict[key].append(st)
            else:
                strs_sorted_dict[key] = [st]

        return list(strs_sorted_dict.values())

        