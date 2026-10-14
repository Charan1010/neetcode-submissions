class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict_freq = {}
        final_l = []

        for num in nums:

            if num in dict_freq:
                dict_freq[num] += 1
            else:
                dict_freq[num] = 1

        invert_dict_freq = [(val, key)for key, val in dict_freq.items()]

        sorted_invert_dict_freq = sorted(invert_dict_freq, reverse= True)

        return list(map(lambda x: x[1], sorted_invert_dict_freq))[0:k]

         



