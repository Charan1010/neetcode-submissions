class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        total_distinct = len(set(nums))

        if total_distinct != len(nums):
            return True

        return False