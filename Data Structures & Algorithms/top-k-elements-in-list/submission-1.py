class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums))]

        count_nums = {}
        for num in nums:
            count_nums[num] = count_nums.get(num, 0) + 1

        for num, count in count_nums.items():
            freqs[count - 1].append(num)

        ans = []
        i, tracker = len(freqs) - 1, 0
        while i >= 0 and tracker < k:
            if freqs[i]:
                ans.extend(freqs[i])
                tracker += len(freqs[i])
            i -= 1

        return ans