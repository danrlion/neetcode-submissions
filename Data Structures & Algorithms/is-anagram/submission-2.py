from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # edge case
            return False
        
        d_s = defaultdict(int)
        d_t = defaultdict(int)
        for i in range(len(s)):
            d_s[s[i]] += 1
            d_t[t[i]] += 1
        if d_s == d_t:
            return True
        return False
        
        