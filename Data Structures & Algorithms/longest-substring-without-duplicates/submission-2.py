class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxL = 0, 0
        mp = {}

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            maxL = max(maxL, r - l + 1)

        return maxL