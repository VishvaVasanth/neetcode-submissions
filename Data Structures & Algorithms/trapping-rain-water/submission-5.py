class Solution:
    def trap(self, height: List[int]) -> int:

        lmax =0 
        rmax = 0
        total = 0

        l = 0
        r = len(height)-1

        while (l<r):

            if height[l]<= height[r]:
                if height[l]<lmax:
                    total += lmax-height[l]
                    l+=1
                    
                else:
                    lmax = height[l]
                    l+=1
            else:
                if rmax > height[r]:
                    total += rmax-height[r]
                    r-=1
                else:
                    rmax = height[r]
                    r-=1
        return total
                    
        