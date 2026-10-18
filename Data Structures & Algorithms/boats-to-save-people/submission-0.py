class Solution:
    def numRescueBoats(self, p: list[int], limit: int) -> int:

        boat = 0
        p.sort()

        n = len(p)

        l = 0
        r= n-1

        while l<=r:

            if p[l]+p[r] <= limit:
                l+=1
            r-=1
            boat+=1
        return boat
        