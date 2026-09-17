class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #still O(log n) time and O(1) space

        #Understand
        #Input = list of ints (nums) = rotated sorted array
        #output = int = index of the target value

        #Match - Binary Search -> similar to find min in sorted arr

        #Plan
        #we know there may be up to 1 inflection point

        #in find min in sorted arr, we had left and right
        #left = 0, right = len(nums)-1
        #if nums[mid] > nums[right]:
            #we know the min is to the right
        #else:
        #   we know the min is to the left or is mid

        #in this case, target is 1
        #[3, 4, 5, 6, 1, 2]
        #left = 0, right = 5
        #mid = 2 (5)
        #need to compare nums[mid] to nums[right] AND compare them to the target too
        #5 > 2, so min is to the right, target is 1 (less than 5)
        #since 1 < 2 and 1 < 5, we know the target is in between mid and right (left = mid+1)
        #left = 3, right = 5
        #mid = 4
        #found, return


        #[3, 5, 6, 0, 1, 2], target = 4
        #left = 0, right = 5
        #mid = 2 (6)
        #compare nums[mid] to nums[right]
        #6 > 2


        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            #Case 1: left half is normally sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1 #target is within the sorted left half

                else:
                    left = mid + 1 #target is to the right half

            #Case 2: Right half is normally sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 #target is within the sorted right half
                else:
                    right = mid - 1 #target is in the left half

        return -1


