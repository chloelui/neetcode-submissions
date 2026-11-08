class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inds = {}
        for i in range(len(nums)):
            if target - nums[i] in inds:
                return [inds[target - nums[i]], i]
            inds[nums[i]] = i