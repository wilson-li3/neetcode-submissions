class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_brackets = {")":"(", "]":"[", "}":"{"}
        for p in s:
            if p in closing_brackets:
                if not stack or stack[-1] != closing_brackets[p]:
                    return False
                stack.pop()
            else:
                stack.append(p)
        return True if not stack else False