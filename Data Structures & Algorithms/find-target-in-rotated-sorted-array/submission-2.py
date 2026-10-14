class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) -1

        while start <= end: 

            pivot = (start+end)//2

            if nums[pivot] == target :
                return pivot

            if nums[start] <= nums[pivot]:

                if nums[start] <= target < nums[pivot]:
                    end = pivot - 1
                else:
                    start = pivot + 1

            else:

                if nums[pivot] < target <= nums[end]:
                    start = pivot + 1
                else:
                    end = pivot - 1

        return -1


        