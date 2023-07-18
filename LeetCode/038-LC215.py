#Kth Largest Element in an Array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num*-1)
        
        res = 0
        for i in range(k):
            res = heapq.heappop(heap)*-1
        return res 
    
# Time: O(NlogN) Space: O(N)
# Push each element from the element to the heap
# Pop from the heap k times and that will the k the largest element.

