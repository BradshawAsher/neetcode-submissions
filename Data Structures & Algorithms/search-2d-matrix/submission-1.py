class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #sorted in non-decreasing order (ascending)
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])

        #1. Binary search the rows to find which row could contain target
        top, bot = 0, rows-1
        target_row = -1

        while top <= bot:
            mid_row = (top + bot) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                target_row = mid_row
                break

            elif matrix[mid_row][0] > target:
                bot = mid_row - 1

            else:
                top = mid_row + 1
        
        if target_row == -1:
            return False

        #2. Standard binary search on the chosen row
        row = matrix[target_row]
        left, right = 0, cols - 1
        
        while left <= right:
            mid = (left + right) // 2

            if row[mid] == target:
                return True
            
            elif row[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1

        return False




