class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        

        pair = []
        numsDict = {}

        for i in range(0, len(nums)):
            numsDict[nums[i]] = i
        

        for i in numsDict:
            if (target - i) in numsDict:
                if (target - i) != i:
                    return [numsDict[i], numsDict[(target - i)]]
                else:
                    for j in range(0, numsDict[i]):
                        if nums[j] == i:
                            return [j, numsDict[i]]