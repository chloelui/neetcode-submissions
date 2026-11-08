class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        
        if len(s) != len(t):
            return False
        
        letters_s = Counter(s)
        letters_t = Counter(t)
        
        for letter in letters_s:
            if letter not in letters_t:
                return False
            if letters_s[letter] != letters_t[letter]:
                return False

        return True