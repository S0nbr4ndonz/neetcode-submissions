class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        thisSet = set(nums)

        longestConsecutive = 0
        

        for number in thisSet:
            currentConsecutive = 1
            currentNumber = number
            if (number - 1) not in thisSet:
                while (currentNumber + 1) in thisSet:
                    currentConsecutive +=1
                    currentNumber +=1
                
                if currentConsecutive > longestConsecutive:
                    longestConsecutive = currentConsecutive
                    

        return longestConsecutive
        