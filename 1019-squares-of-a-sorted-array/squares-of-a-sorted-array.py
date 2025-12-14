class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list = []
        for i in nums:
            list.append(i * i)

        list.sort()
        return list