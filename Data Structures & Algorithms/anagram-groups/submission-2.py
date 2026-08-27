class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        thisDict = {}
        
        for i in range(0,len(strs)):
            myList = [0] * 26
            for k in range(0, len(strs[i])):
                myList[ord(strs[i][k]) - ord("a")] += 1
            tup = tuple(myList)
            if tup not in thisDict:
                thisDict[tup] = [strs[i]]
            else:
                thisDict[tup].append(strs[i])
        
        final_list = []
        for key in thisDict:
            final_list.append(thisDict[key])
        
        return final_list
        