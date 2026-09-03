class Solution:

    def encode(self, strs: List[str]) -> str:
        pieces = []

        for word in strs:
            pieces.append(str(len(word)) + "#" + word)
        
        return "".join(pieces)


    def decode(self, s: str) -> List[str]:

        pieces = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j+=1
        
            numberList = []

            while i != j:
                numberList.append(s[i])
                i+=1
            
            number = int("".join(numberList))

            charList = []

            for k in range(i+1, i + number + 1):
                charList.append(s[k])
            
            pieces.append("".join(charList))

            i += (number + 1)


        return pieces
