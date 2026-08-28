class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        thisDict = {}

        for i in range(0, len(nums)):
            if nums[i] not in thisDict:
                thisDict[nums[i]] = 1
            else:
                thisDict[nums[i]] += 1
        
        myList = [[] for _ in range(len(nums)+1)]

        for key in thisDict:
            myList[thisDict[key]].append(key)

        
        finalList = []
        i = len(myList)-1
        leftToGet = k

        while len(finalList) < k and leftToGet > 0:
            if len(myList[i]) !=0:
                for j in range(0, len(myList[i])):
                    finalList.append(myList[i][j])
                    leftToGet -= 1

                    if leftToGet == 0:
                        break
                    
            

            i -= 1

        return finalList
        