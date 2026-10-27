class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_list = []
        unique_triplets = set()
        for i, num1 in enumerate(nums):
            s = {}
            for num2 in nums[i+1:]:

                if num2 in s:
                    sorted_triplet = str(sorted(s[num2]+[num2]))
  
                    if sorted_triplet not in unique_triplets:
                        unique_triplets.add(sorted_triplet)
                        final_list.append(s[num2]+[num2])

                s[0 - num1 - num2] = [num1, num2]

        return final_list
            
