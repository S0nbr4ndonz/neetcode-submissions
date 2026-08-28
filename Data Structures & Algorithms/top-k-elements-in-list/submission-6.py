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
        
        for i in range((len(myList)-1), 0, -1):
            for number in myList[i]:
                finalList.append(number)

                if len(finalList) == k:
                    return finalList        