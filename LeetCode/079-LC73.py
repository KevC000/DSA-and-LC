# Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_to_zeroes = set()
        cols_to_zeroes = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows_to_zeroes.add(r)
                    cols_to_zeroes.add(c)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows_to_zeroes or c in cols_to_zeroes:
                    matrix[r][c] = 0
                    
# Time: O(MN) Space: O(M + N)
# We iterate through the matrix and store the rows and columns that need to be zeroed out.
# We iterate through the matrix again and zero out the rows and columns that need to be zeroed out.
