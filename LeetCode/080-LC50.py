# Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {0:1, 1:x}

        def calculateRoot(i):
            if i in cache:
                return cache[i]
            cache[i] =  calculateRoot(i//2) * calculateRoot(i-(i//2))
            return cache[i]
        
        return calculateRoot(n) if n>0 else 1/calculateRoot(abs(n))


# Time: O(logN) Space: O(logN)
# We use a cache to store the results of the powers of x.
# We use recursion to calculate the power of x.
# If the power is in the cache, we return the result.
# Otherwise, we calculate the power of x by calculating the power of x/2 and x-x/2.
# We return the result.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1: return 1
        if x == 0: return 0

        if n<0:
            x, n = 1/x, -n
        res, num, power = 1,x,n
        while power != 1:
            if power%2==0:
                num = num*num
                power/=2
            else:
                res*=num
                power-=1
        return res*num
    
# Time: O(logN) Space: O(1)
# We use a while loop to calculate the power of x.
# If the power is even, we square x and divide the power by 2.
# If the power is odd, we multiply the result by x and subtract the power by 1.
# We return the result multiplied by x.
