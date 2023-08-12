# Spiral Matrix

class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0) # 1

            if matrix and matrix[0]: 
                for line in matrix:
                    result.append(line.pop())

            if matrix:
                result+=matrix.pop()[::-1]

            if matrix and matrix[0]:
                for line in matrix[::-1]:
                    result.append(line.pop(0))
        return result

# Time: O(N) Space: O(1)
# We iterate through the matrix.
# We add the first row to the result.
# We add the last element of each row to the result.
# We add the last row in reverse order to the result.
# We add the first element of each row in reverse order to the result.
# We return the result.