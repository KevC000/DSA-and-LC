# Gas Station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        res = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i]-cost[i]
            if total < 0:
                total = 0
                res = i+1
        return res
    
# Time: O(N) Space: O(1)
# We check if the total gas is greater than the total cost.
# We use a variable to store the total gas.
# If the total gas is less than 0, we reset the total gas and start from the next station.
# If we can complete the circuit, we return the starting station.