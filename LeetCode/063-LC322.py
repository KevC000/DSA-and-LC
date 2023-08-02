# Coin Change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [amount+1] * (amount+1)
        cache[0] = 0
        for a in range(1,amount+1):
            for c in coins:
                if a - c >= 0:
                    cache[a] = min(cache[a], 1 + cache[a-c])
                                       
        return cache[amount] if cache[amount] != amount+1 else -1


# Time: O(n) Space: O(n)
# We use dynamic programming to find the minimum number of coins required to make the amount.
# We use a list to store the minimum number of coins required to make the amount from 0 to amount.
# We initialize the list with amount+1.
# We set the first element of the list to 0.
# We iterate over the list from 1 to amount+1.
# We iterate over the coins.
# We check if the current amount - the current coin is greater than or equal to 0.
# We set the current element of the list to the minimum of the current element of the list and 1 + the element of the list at the index of the current amount - the current coin.
# We return the last element of the list if it is not equal to amount+1, else we return -1.

