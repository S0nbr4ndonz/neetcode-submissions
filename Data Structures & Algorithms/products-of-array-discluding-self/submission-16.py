class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        suffix = [1] * len(nums)
        prefixProduct = 1
        suffixProduct = 1

        result = []

        for i in range(0, len(nums)):
            prefix.append(prefixProduct)
            prefixProduct *= nums[i]
        
        for i in range(len(nums) -1, -1, -1):
            suffix[i] = suffixProduct
            suffixProduct *= nums[i]
        

        for i in range(0, len(nums)):
            result.append(suffix[i] * prefix[i])

        
        return result
            