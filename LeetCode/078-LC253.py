
# Meeting Rooms II
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        room_count = 1
        heap = [intervals[0][1]]
        for start, end in intervals[1:]:
            if start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            room_count = max(room_count, len(heap))
        return room_count

# Time: O(NlogN) Space: O(N)
# We sort the intervals.
# We use a heap to store the end of the intervals.
# We iterate through the intervals and compare the start of the current interval with the end of the earliest ending interval.
# If the start of the current interval is greater than or equal to the end of the earliest ending interval, we pop the earliest ending interval from the heap.
# We push the end of the current interval to the heap.
# We update the room count to be the maximum of the room count and the length of the heap.
