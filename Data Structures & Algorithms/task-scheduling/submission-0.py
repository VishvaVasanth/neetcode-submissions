class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []

        for c in freq.values():
            heap.append(-c)

        heapq.heapify(heap)

        queue = deque()
        time =0

        while heap or queue:
            time+=1
            if queue and  queue[0][1]==time:
                heapq.heappush(heap,queue.popleft()[0])


            if heap:
                c = 1+ heapq.heappop(heap)
                
                if c:
                    queue.append([c,time+n+1])
        return time 

        

        
        

            



        