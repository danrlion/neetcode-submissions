from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        answer: list[list[int]] = []
        def backtracking(start_index: int, path: List[int], target_remaining: int):
            if target_remaining == 0:
                answer.append(path[:])
                return
            if target_remaining < nums[start_index]: # prune
                return
            # constraint: numbers have index equal or higher to avoid duplicates
            for edge in range(start_index, len(nums)):
                target_remaining -= nums[edge]
                path.append(nums[edge])
                backtracking(edge, path, target_remaining)
                target_remaining += nums[edge]
                path.pop()

        backtracking(0, [], target)
        
        return answer