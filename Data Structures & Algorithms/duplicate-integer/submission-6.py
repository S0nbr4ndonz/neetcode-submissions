class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        return len(set(nums)) != len(nums)
     