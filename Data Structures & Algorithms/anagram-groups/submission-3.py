from collections import defaultdict
from typing import List, Dict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: Dict[str, List[str]] = defaultdict(list)

        for i_l in range(len(strs)):
            word = "".join(sorted(strs[i_l]))
            result[word].append(strs[i_l])
        return list(result.values())



