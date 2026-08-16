class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minheap =[]
        heapq.heapify(minheap)

        result =[]

        for num in points:
            a = num[0]
            b = num[1]

            dist = ((a)**2 +(b)**2)**(1/2)

            heapq.heappush(minheap,(dist,num))
        
        for i in range(k):
            
            result.append(heapq.heappop(minheap)[1])
        
        return result
            


        