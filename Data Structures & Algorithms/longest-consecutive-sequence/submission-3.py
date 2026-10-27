class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seq_len = {}
        #max_conseq_len = -float("inf")

        for num in nums:

            if num in seq_len:
                continue
            else:
                if (num-1 in seq_len) and (num+1 in seq_len):
                    length = seq_len[num-1] + seq_len[num+1] + 1
                    seq_len[num-seq_len[num-1]] = length
                    seq_len[num+seq_len[num+1]] = length
                    seq_len[num] = length
                elif num-1 in seq_len:
                    length = seq_len[num-1] + 1
                    seq_len[num] = length
                    seq_len[num-seq_len[num-1]] = length
                elif num+1 in seq_len:
                    length = seq_len[num+1] + 1
                    seq_len[num] = length
                    seq_len[num+seq_len[num+1]] = length
                else:
                    seq_len[num] = 1

            #print(seq_len)

        #print(seq_len)

        if len(seq_len) > 0:
            return max(seq_len.values())
        else:
            return 0

        