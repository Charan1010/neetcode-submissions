class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d_global = {}

        for st in strs:
            sort_st = str(sorted(st))

            if sort_st in d_global:
                d_global[sort_st].append(st)
            else:
                d_global[sort_st] = [st]

        print(d_global)

        return list(d_global.values())

        


            
        