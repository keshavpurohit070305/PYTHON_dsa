class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        current_sum = 0

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum == target:
                return[l+ 1 , r + 1]
            elif current_sum < target:
                l = l + 1
            else:
                r = r - 1 