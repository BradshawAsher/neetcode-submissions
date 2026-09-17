class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #sorted in non-decreasing order (ascending)
        #binary search
        #Understand
        #input = 2d matrix of sorted numbers
        #output = bool (t or f)

        #M - match = binary search

        #Plan
        #find mid each iteration of a loop
        #while left <= right
        #mid = left + right // 2 (or left + righ + 1) // 2 i forgot
        #left = (0, 0), right = (2, 3)
        #row_length = 4, so right = 2 * 4+3 = 11th

        #mid = (avg(left_x+right_x), avg(left_y+right_y))

        #if matrix[mid[0]][mid[1]] == matrix: return True
        #if matrix[mid[0]][mid[1]] < matrix:
            #move left up
            #left = (mid[0], mid[1]+1) #need to handle out of bounds for carries
        #else:
            #means move right down
            #right = (mid[0], mid[1]-1) #need to handle oob for carries
        
        #return False

        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix[mid // cols][mid % cols]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        
        return False
        