class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # edge case
            return False
        s_s = sorted(s)
        t_s = sorted(t)
        i = 0
        while i < len(t_s):
            if s_s[i] != t_s[i]:
                return False
            i += 1
        return True