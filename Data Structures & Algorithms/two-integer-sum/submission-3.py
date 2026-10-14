class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        balance = {}

        for i in range(len(nums)):
            if nums[i] in balance:
                return [balance[nums[i]], i]
            balance[target - nums[i]] = i
            


        

        

        