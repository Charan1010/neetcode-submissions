class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_num = {}
        num_freq = {}
        highest_freq = -999999999
        final_list = []

        for ele in nums:

            if ele in num_freq:
                curr_freq = num_freq[ele]
                freq_num[curr_freq].remove(ele)

            else:
                curr_freq = 0

            incremented_freq = curr_freq + 1
            num_freq[ele] = incremented_freq

            if incremented_freq in freq_num:
                freq_num[incremented_freq].add(ele)
            else:
                freq_num[incremented_freq] = {ele}

            if incremented_freq > highest_freq :
                highest_freq = incremented_freq

        for i in range(highest_freq, 0, -1):
            if i in freq_num:
                for ele in freq_num[i]:
                    final_list.append(ele)
                    print(final_list)

                    if len(final_list) == k:
                        return final_list







        