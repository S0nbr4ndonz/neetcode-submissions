class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0
        l=0
        r=0
        sCharacters = [0] * 26
        highestFrequency = 0
        while l < len(s) and r < len(s):
            sCharacters[ord(s[r]) - ord("A")] +=1
            for character in sCharacters:
                if character > highestFrequency:
                    highestFrequency = character
            if (r-l+1) - highestFrequency <= k:
                if (r-l+1) > longest:
                    longest = (r-l+1)
            else:
                sCharacters[ord(s[l]) - ord("A")] -=1
                l+=1
            r+=1


        return longest

        
            

        
        