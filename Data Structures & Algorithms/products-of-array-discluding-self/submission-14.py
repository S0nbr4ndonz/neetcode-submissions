class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        result = []
        zeroCount = 0

        for number in nums:
            if number == 0:
                zeroCount += 1
                continue

            product *= number
                

        for number in nums:
            if zeroCount == 1:
                if number != 0:
                    result.append(0)
                else:
                    result.append(product)
            elif zeroCount > 1:
                result.append(0)
            else:
                result.append((product // number))
        
        return result
        