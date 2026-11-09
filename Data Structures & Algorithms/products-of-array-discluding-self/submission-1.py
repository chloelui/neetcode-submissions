class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(nums)

        res = [0] * len(nums)
        for i in range(len(nums)):
            prod = 1
            for num, count in c.items():
                if num == nums[i] and count > 1:
                    prod *= (num ** (count - 1))
                elif num != nums[i]:
                    prod *= (num ** count)
            res[i] = prod

        return res