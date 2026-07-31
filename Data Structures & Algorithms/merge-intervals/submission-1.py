from collections import defaultdict
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answers: list[list[int]] = []
        intervals.sort(key = lambda i: i[0])
        for interval in intervals:
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
                    


