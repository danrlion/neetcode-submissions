class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(s)) for s in strs]
        grouped_anagrams = {k: [] for k in set(sorted_strs)}
        for i in range(len(strs)):
            text = sorted_strs[i]
            grouped_anagrams[text].append(strs[i])
        return list(grouped_anagrams.values())
