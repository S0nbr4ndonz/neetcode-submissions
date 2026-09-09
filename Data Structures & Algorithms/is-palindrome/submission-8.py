class Solution:
    def isPalindrome(self, s: str) -> bool:

        leftPointer = 0
        rightPointer = len(s) - 1

        while leftPointer != rightPointer and leftPointer < rightPointer and rightPointer > leftPointer:
            
            while not s[leftPointer].isalnum() and leftPointer < rightPointer:
                leftPointer+=1
            
            while not s[rightPointer].isalnum() and rightPointer > leftPointer:
                rightPointer-=1
            

            if s[leftPointer].lower() != s[rightPointer].lower():
                return False
            
            leftPointer+=1
            rightPointer-=1
        
        return True
            