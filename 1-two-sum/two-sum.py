class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            number_needed = target - nums[i]

            if number_needed in hashmap:
                return[hashmap[number_needed],i]

            else:
                hashmap[nums[i]] = i