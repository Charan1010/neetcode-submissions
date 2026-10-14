class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = [1, 1]

        no_of_zeros = 0

        for num in nums:

            if num == 0:
                no_of_zeros += 1
                prod[0] = prod[0]*num
            else:
                prod[0] = prod[0]*num
                prod[1] = prod[1]*num

        #print(prod[0])

        if no_of_zeros > 1:
            return [0]*len(nums)
        

        final_l =[]
        for num in nums:
            if num == 0:
                final_l.append(prod[1])
            else:
                final_l.append(prod[0]//num)

        return final_l

