from collections import defaultdict
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def sort_intervals(intervals: list[list[int]]) -> list[list[int]]:
            sorted_intervals: list[list[int]] = []
            d_firsts: dict[key, list[list[int]]] = defaultdict(list)
            for interval in intervals:
                d_firsts[interval[0]].append(interval)
            for first in sorted(d_firsts.keys()):
                sorted_intervals.extend(d_firsts[first])
            return sorted_intervals
        
        answers: list[list[int]] = []
        for interval in sort_intervals(intervals):
            if not bool(answers):
                answers.append(interval)
            else:
                contained: bool = False
                i: int = 0
                while i < len(answers) and not contained:
                    firsts = [answers[i][0], interval[0]]
                    lasts = [answers[i][1], interval[1]]
                    if max(firsts) <= min(lasts):
                        answers[i] = [min(firsts), max(lasts)]
                        contained = True
                        break
                    i += 1
                if not contained: 
                    answers.append(interval)
        return answers
                    


