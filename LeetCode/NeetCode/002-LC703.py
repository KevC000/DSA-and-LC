#Kth Largest Element in a Stream
from ast import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# Use heap to sort the elements
# Pop until len of the heap is k and theese are you kth largest elements.
# Add: push to heap and keep popping until the length of heap is k.
# return element at 0th index which is the largest in the heap aka the kth largest.