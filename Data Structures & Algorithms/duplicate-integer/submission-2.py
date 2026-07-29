class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        if len(set(nums)) != len_nums:
            return True
        return False