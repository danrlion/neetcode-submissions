class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # edge case
            return False
        
        s_s = sorted(s)
        t_s = sorted(t)
        
        if s_s == t_s:
            return True
        else:
            return False