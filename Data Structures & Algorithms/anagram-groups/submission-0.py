class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashing approach
        anagrams = {}

        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)

        return list(anagrams.values())