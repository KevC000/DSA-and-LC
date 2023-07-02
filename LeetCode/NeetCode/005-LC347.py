#Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    
        freq = {}
        counts = [[] for i in range(len(nums)+1)]

        for n in nums: 
            freq[n] = freq.get(n,0)+1
        for num, count in freq.items():
            counts[count].append(num)
        
        res = []
        for i in range(len(counts)-1,-1,-1):
            for n in counts[i]:
                res.append(n)
                if len(res) == k:
                    return res
            

# Keep track of frequency using a dictionary.
# Order the value based on frequency which is represented as the index in a list.
# Iterate throught the that list and append the the values to the resulting list starting from the last index until the resultinglist is length k.