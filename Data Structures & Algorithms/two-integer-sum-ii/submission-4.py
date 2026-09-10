class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if len(numbers) == 2:
            return [1,2]

        l = 0
        r = len(numbers)-1

        while l < r:
            currentSum = numbers[l] + numbers[r]

            if currentSum == target:
                return [l+1, r+1]
            elif currentSum > target:
                r-=1
            else:
                l+=1
        




        
        