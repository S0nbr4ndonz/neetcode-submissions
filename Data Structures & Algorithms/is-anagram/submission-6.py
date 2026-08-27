class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        Sdict = {}
        Tdict = {}

        for i in range(0, len(s)):
            if s[i] in Sdict:
                Sdict[s[i]] += 1
            else:
                Sdict[s[i]] = 1
            
            if t[i] in Tdict:
                Tdict[t[i]] += 1
            else:
                Tdict[t[i]] = 1

        if Sdict == Tdict:
            return True
        
        return False