class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = {k: 0 for k in set(nums)}
        for i in range(len(nums)):
            occurrences[nums[i]] += 1
        times_to_return = sorted(occurrences.values(), reverse=True)[:k]
        return [number for number,times in occurrences.items() if times in times_to_return]
        
        

