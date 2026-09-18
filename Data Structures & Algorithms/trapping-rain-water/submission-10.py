class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        contained = 0


        for i,bar in enumerate(height):
            if not stack:
                stack.append(i)
                continue
            
            while bar > height[stack[-1]]:
                bottomIndex = stack.pop()
                if not stack:
                    break
                contained += ( min(height[stack[-1]], bar) - height[bottomIndex]) * (i - stack[-1] -1 )
                
            stack.append(i)

        return contained

        