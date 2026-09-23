class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        Sdict = {}
        Tdict = {}


        for character in s:
            if character in Sdict:
                Sdict[character] +=1
            else:
                Sdict[character] = 1
        

        for character in t:
            if character in Tdict:
                Tdict[character] +=1
            else:
                Tdict[character] = 1
        

        return Sdict == Tdict