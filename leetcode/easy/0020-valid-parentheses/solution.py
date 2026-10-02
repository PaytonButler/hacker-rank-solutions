class Solution:
    def isValid(self, s: str) -> bool:
        closingPairs = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char in closingPairs:
                if not stack or closingPairs[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack
