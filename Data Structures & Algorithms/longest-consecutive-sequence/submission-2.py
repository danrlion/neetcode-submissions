from heapq import heapify, heappop
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # edge case
        if not bool(nums):
            return 0
        answers = [1]
        heapify(nums)
        last_used = heappop(nums)
        for i in range(0, len(nums)): # to not go over the list of elements
            current = heappop(nums)
            if current - last_used > 1: # not consecutive
                answers.append(1)
            else: # consecutive
                answers[-1] += current - last_used

            last_used = current
        
        return max(answers)