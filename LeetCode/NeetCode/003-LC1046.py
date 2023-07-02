#Last Stone Weight

from ast import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)

        while len(stones)>1:
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1

            if x != y:
                heapq.heappush(stones,(y-x)*-1)
        if len(stones) == 1:
            return stones[0]*-1
        return 0
    
# O(N) Time O(1) Space
#Since python uses minheap by default we will want convert all the numbers to negative before heapifying so the positive counter part of the negative will be at the top.
#We keep popping the top 2 stones form the heap and check if the values are equal. If not, we return the difference back to the heap.
#We then return the last stone if it exists else we return 0.