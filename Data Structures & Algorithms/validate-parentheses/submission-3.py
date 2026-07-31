class Solution:
    def isValid(self, s: str) -> bool:
        # first closing char need to match last openning char
        # if openning char -> add to stack
        # if closing char -> validate and remove last element from stack
        if len(s) % 2 != 0:
            return False
        stack: list[str] = []
        close_chars = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in close_chars:
                if not bool(stack) or stack[-1] != close_chars[c]:
                    return False
                stack.pop(-1)
            else:
                stack.append(c)
        
        return not bool(stack)
