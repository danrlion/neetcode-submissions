class Solution:
    def isValid(self, s: str) -> bool:
        # first closing char need to match last openning char
        # if openning char -> add to stack
        # if closing char -> validate and remove last element from stack
        if len(s) % 2 != 0:
            return False
        stack: list[str] = []
        close_c = [")", "]", "}"]
        valid = ["()", "{}", "[]"]
        for i in range(len(s)):
            c = s[i]
            if c in close_c:
                if not bool(stack):
                    return False
                if "".join([stack[-1], c]) not in valid:
                    return False
                stack.pop()
            else:
                stack.append(c)
        if len(stack) > 0:
            return False
        return True
