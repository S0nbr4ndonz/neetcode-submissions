class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        currentSub = set()
        l = 0
        longest = 0

        for i,character in enumerate(s):

            while character  in currentSub:
                currentSub.remove(s[l])
                l+=1
            
            currentSub.add(character)

            
            if longest < len(currentSub):
                longest = len(currentSub)
            
            
            

        return longest