# Reverse Bits
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 31
        while power >= 0:
            digit = n & 1
            res <<= 1
            res ^= digit
            n >>= 1
            power-=1
        return res
# Time: O(1) Space: O(1)
# Count: we iterate through the 32 bits of the number.
# We get the current digit by ANDing the number with 1.
# We shift the result left by 1.
# We XOR the result with the digit.
# We shift the number right by 1.
# We decrement the power.
# We return the result.
