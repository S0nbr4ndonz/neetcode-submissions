class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        thisSet = set()

        for number in nums:
            thisSet.add(number)

        longestConsecutive = 0
        

        for number in thisSet:
            cont = True
            currentConsecutive = 1
            currentNumber = number
            if (number - 1) in thisSet:
                continue
            else:
                while cont == True:
                    if (currentNumber + 1) in thisSet:
                        currentConsecutive +=1
                        currentNumber +=1
                    else:
                        if currentConsecutive > longestConsecutive:
                            longestConsecutive = currentConsecutive
                        cont = False
                    

        return longestConsecutive
        