class Solution:
    def isValid(self, s: str) -> bool:
        openers = {"[": 0, "{": 1, "(": 2}
        closers = {"]": 0, "}": 1, ")": 2}
        open_stack = []

        for char in s:
            if char in openers:
                open_stack.append(char)
            else:
                if not open_stack or closers[char] != openers[open_stack.pop()]:
                    return False

        return True if not open_stack else False