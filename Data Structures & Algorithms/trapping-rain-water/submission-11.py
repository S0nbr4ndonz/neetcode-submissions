class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        contained = 0

        for i, currentHeight in enumerate(height):
            if not stack:
                stack.append(i)
                continue
            
            while currentHeight > height[stack[-1]]:
                bottomIndex = stack.pop()
                if not stack:
                    break
                contained += (min(currentHeight, height[stack[-1]]) - height[bottomIndex]) * (i-stack[-1] - 1)

            stack.append(i)

        return contained 
                

        