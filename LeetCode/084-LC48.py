# Rotate Image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0,len(matrix)-1
        t, b = 0, len(matrix)-1
        
        while l < r and t < b:
            for i in range(r-l):
                t,b = l,r
                temp = matrix[t][l+i]
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][r-i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = temp
            r-=1
            l+=1


# Time: O(N) Space: O(1)
# We create variables for the left, right, top, and bottom boundaries.
# We iterate through the matrix.
# We swap the elements in the corners of the matrix.
# We swap the elements in the middle of the matrix.
# We return the matrix.