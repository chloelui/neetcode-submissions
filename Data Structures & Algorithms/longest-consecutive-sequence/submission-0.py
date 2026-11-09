class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        best = 0
        for x in nums:
            if x - 1 not in nums:
                curr = 1
                y = x + 1
                while y in nums:
                    y += 1
                    curr += 1
                best = max(best, curr)

        return best