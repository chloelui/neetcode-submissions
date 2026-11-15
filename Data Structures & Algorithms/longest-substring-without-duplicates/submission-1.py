class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxL = 0, 0
        seen = set()

        for r in range(len(s)):
            if s[r] in seen:
                maxL = max(maxL, r - l)
                while l < r and s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])

        maxL = max(maxL, len(s) - l)

        return maxL