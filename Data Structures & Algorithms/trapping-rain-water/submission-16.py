class Solution:
    def trap(self, height: List[int]) -> int:

        
        contained = 0
        l = 0
        r = len(height) -1
        lmax = height[l]
        rmax=height[r]

        while l < r:
            if lmax <= rmax:
                contained += lmax- height[l]
                l+=1
                if lmax < height[l]:
                    lmax = height[l]
            else:
                contained+= rmax - height[r]
                r-=1
                if rmax < height[r]:
                    rmax = height[r]

        return contained 
                

        