class Solution:
    word_lengths = []

    def encode(self, strs: List[str]) -> str:
        Solution.word_lengths = [len(word) for word in strs]
        s = "".join(strs)
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        last, curr = 0, 0
        for word_length in Solution.word_lengths:
            curr += word_length
            res.append(s[last:curr])
            last = curr
        return res