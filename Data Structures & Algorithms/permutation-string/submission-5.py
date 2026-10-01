class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        r=0
        l=0
        alphaFreq1= [0] * 26
        alphaFreq2= [0] * 26

        for character in s1:
            alphaFreq1[ord(character) - ord("a")] +=1



        while r<len(s2):
            alphaFreq2[ord(s2[r]) - ord("a")] +=1
            if (r-l+1) < len(s1):
                r+=1
                continue
            

            
            if alphaFreq1 == alphaFreq2:
                return True
            
            alphaFreq2[ord(s2[l]) - ord("a")] -=1
            l+=1
            r+=1

        

        return False

        