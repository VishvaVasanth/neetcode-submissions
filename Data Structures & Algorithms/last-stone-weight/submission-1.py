class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxheap = []
        heapq.heapify(maxheap)

        for num in stones:
            heapq.heappush(maxheap,(num*-1))
        
        while len(maxheap)>1:
            a =heapq.heappop(maxheap)
            b = heapq.heappop(maxheap)

            c = (a*-1)-(b*-1)            
            heapq.heappush(maxheap,(-1*c))
            
        return (-1 * heapq.heappop(maxheap))
                

            














        