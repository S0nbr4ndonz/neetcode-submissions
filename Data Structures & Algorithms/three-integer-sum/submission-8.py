class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        for i, number in enumerate(nums):
            if i>0 and number == nums[i-1]:
                continue


            target = 0 - number
            left = i+1
            right = len(nums)-1
            while left < right:

                currentSum = nums[left] + nums[right]

                if currentSum == target:
                    result.append([number, nums[left], nums[right]])
                    right-=1
                    left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                elif currentSum > target:
                    right -=1
                else:
                    left +=1
        

        return result


