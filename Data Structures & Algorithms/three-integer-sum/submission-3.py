class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        final_l = []

        for ind, ele in enumerate(nums):

            if ind !=0 and nums[ind-1] == nums[ind]:
                continue


            left = ind +1
            right = len(nums) -1


            total = 0 - ele 

            while left < right:

                curr_total = nums[left] + nums[right]

                if curr_total < total :
                    left += 1
                elif curr_total > total:
                    right -= 1
                else:
                    final_l.append([ele, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and  nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

        return final_l



