class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in Map:
                return [Map[complement], i]
            Map[nums[i]] = i


   