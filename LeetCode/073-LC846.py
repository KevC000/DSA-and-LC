# Hand of Straights

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        frequency = Counter(hand)
        heap = [[n, freq] for n, freq in frequency.items()]
        heapq.heapify(heap)

        while heap:
            if len(heap) < groupSize:
                return False
            back_to_heap = []

            top_val, top_count = heap[0]
            for i in range(top_val, top_val+groupSize):
                curr_val, curr_count = heapq.heappop(heap)
                if curr_val != i:
                    return False
                if curr_count > 1:
                    back_to_heap.append([curr_val, curr_count-1])
            for card in back_to_heap:
                heapq.heappush(heap, card)
        return True

# Time: O(NlogN) Space: O(N)
# We use a heap to store the frequency of each card.
# We pop the top card from the heap and check if we can form a group of size groupSize.
# If we can't, we return False.
# If we can, we pop the next groupSize-1 cards from the heap and check if they are consecutive.
# If they are, we continue. If not, we return False.
# If we can form all the groups, we return True.
