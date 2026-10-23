class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        postfix = 1
        final_elements= []

        for i in range(len(nums)):
            final_elements.append(prefix)
            prefix = prefix*nums[i]

        for i in range(len(nums)-1, -1, -1):
            final_elements[i] = final_elements[i]*postfix
            postfix = postfix*nums[i]

        #print(final_elements)

        return final_elements



        