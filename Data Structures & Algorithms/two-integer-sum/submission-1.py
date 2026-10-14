class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d_mem = {}

        for ind, ele in enumerate(nums):

            remain = target - ele

            if remain in d_mem:
                return [d_mem[remain], ind] 

            d_mem[ele] = ind




        