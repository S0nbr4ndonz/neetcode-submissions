class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        
        numsDict = {}

        for i in range(0, len(nums)):
            if (target - nums[i]) not in numsDict:
                numsDict[nums[i]] = i
            else:
                return [numsDict[(target-nums[i])], i]
        

        