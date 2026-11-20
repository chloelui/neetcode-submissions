class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                if nums[r] >= nums[m]:
                    if nums[r] >= target:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    l = m + 1
            else:
                if nums[l] <= nums[m]:
                    if nums[l] > target:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    r = m - 1

        return ans