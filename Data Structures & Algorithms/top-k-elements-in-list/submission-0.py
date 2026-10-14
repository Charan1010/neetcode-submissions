class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        d_s = {}

        for ele in nums:
            if ele in d_s:
                d_s[ele] += 1
            else:
                d_s[ele] = 1

        freq_eles = []

        for key,val in d_s.items():
            freq_eles.append((val, key))

        freq_eles = sorted(freq_eles, reverse = True)

        print(freq_eles)

        final_l = []

        for i in range(k):
            final_l.append(freq_eles[i][1])

        return final_l
