# Search a 2D Matrix
from ast import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_start = 0
        row_end = len(matrix)-1

        
        while row_start <= row_end:
            mid = (row_start + row_end)//2
            if target > matrix[mid][-1]:
                row_start = mid+1
            elif target < matrix[mid][0]:
                row_end = mid-1
            else:
                break
        
        if row_start > row_end: return False

        row = (row_start + row_end)//2
        col_start, col_end = 0, len(matrix[0])-1

        while col_start <= col_end:
            mid = (col_start+col_end)//2
            if target > matrix[row][mid]:
                col_start = mid+1
            elif target < matrix[row][mid]:
                col_end = mid-1
            else:
                return True
        return False

# Thought process:    
# Time O(log(m * n) Space O(1)
# To solve this is log time we need to perform binary search. 
# How do we perform binary search on matrix/2D array? First find the row it belongs to then the column.
# Get the mid row if the target is greater than the greatest value in the mid row we look to the higher half of the rows, and lower rows if it's less than the lowest.
# If it's not in any row we return False.
# Once you find the row it's just regulary bianry search :). Return True if it's in that row if not return False.

# Self-Analysis:
# I knew it was a binary search problembecause of the tag on NC150, but wasn't sure how it could be applied to a matrix, so I thought of alternatives.
# First I thought of using two pointers twice instead of binary serch but I realized it would be N+M time.
# Then I realized I could split the matrix in two halves by rows then by columns and perform bianry search twice.
# Conceptually I understood but coding it up was a bit tricky for me but I did it :).
