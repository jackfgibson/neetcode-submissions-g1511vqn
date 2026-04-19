class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            y, x = heapq.heappop(heap), heapq.heappop(heap)
            if -x<-y:
                heapq.heappush(heap, y-x)

        if len(heap)==1: return -heap[0]
        return 0
