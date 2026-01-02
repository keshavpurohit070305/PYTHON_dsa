class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        position_to_fill = n - 1
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square :
                result[position_to_fill] = left_square
                left += 1
            else:
                result[position_to_fill] = right_square
                right -= 1
            position_to_fill  -= 1
        return result
