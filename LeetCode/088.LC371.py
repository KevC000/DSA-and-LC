# Sum of two integers
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask
        mask = 0xFFFFFFFF

        res = a ^ b
        carry = (a & b) << 1

        while carry & mask:
            temp = (res & carry) << 1
            res ^= carry
            carry = temp

        # Check if the 32nd bit is set (i.e., if the number is negative)
        if res & 0x80000000:
            return ~(res ^ mask)

        return res


# Time: O(1) Space: O(1)
# a will be the sum of the two numbers without carrying
# b will be the carry of the two numbers or the initial value of the second number and & mask to handle the negative numbers
# we keep iterating until b is 0 meaning there is no more carry
# we return a if a is less than 0x7FFFFFFF else we return ~(a ^ mask)
# a ^ mask will flip all the bits of a and ~ will flip it back
# this is to handle the negative numbers
