class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d_i = {}

        for ind, ele in enumerate(nums):

            remain = target - ele

            if remain in d_i:
                return [d_i[remain], ind]

            d_i[ele] = ind


        