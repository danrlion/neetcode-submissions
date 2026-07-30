from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer: list[list[int]] = []
        def backtracking(start_index: int, path: List[int]):
            if sum(path) == target:
                answer.append(path[:])
                return
            # constraint: numbers have index equal or higher to avoid duplicates
            for edge in range(start_index, len(nums)):
                if sum(path) + nums[edge] > target:
                    continue
                path.append(nums[edge])
                backtracking(edge, path)
                path.pop()

        backtracking(0, [])
        
        return answer