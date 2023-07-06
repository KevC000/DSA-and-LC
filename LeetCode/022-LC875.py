# Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/k)
            if total_time <= h:
                res = min(res,k)
                r = k-1
            else:
                l=k+1
        return res
    
# Time: O(NlogM) Space O(1)
# We can can eat from 1 to max(piles) per hour, and since koko wants to take her time we need to minimize the number of bananas she is eating(k)
# 1 to max(piles) is a sorted array of numbers so we can use binary search.
# We can check each possible answer with binary search by checking the total time sit takes by checking to total time by iterating trhought the pile.
# If we are successful we want to minimize the rate koko eats so we move towards the lower half after updating the minimum.
# Else we we move farther to the right to find a possible k.