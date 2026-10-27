class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_list = []
        nums = sorted(nums)
        prev_num = -float("inf")
        print(nums)
        for i, num1 in enumerate(nums):
            if num1 != prev_num and num1 <= 0:
                s = {}
                hist_adds = set()
                for num2 in nums[i+1:]:
                    if num2 in s and num2 not in hist_adds:
                        final_list.append(s[num2]+[num2])
                        hist_adds.add(num2)
                    s[0 - num1 - num2] = [num1, num2]
            prev_num = num1

        return final_list
            
