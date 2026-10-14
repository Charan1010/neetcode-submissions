class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)

        max_len = 0

        for ele in nums_set:

            if ele - 1 in nums_set:
                continue
            else:
                curr_len = 1

                while ele + 1 in nums_set:
                    curr_len += 1
                    ele += 1

                if curr_len > max_len:
                    max_len = curr_len

        return max_len
        