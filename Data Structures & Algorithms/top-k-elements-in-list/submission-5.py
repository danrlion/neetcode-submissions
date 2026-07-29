from heapq import heapify, heappop
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d: dict[int, int] = defaultdict(int) # num: freq
        for n in nums:
            d[n] += 1
        d = [(-freq, num) for num,freq in d.items()]
        heapify(d)
        return [heappop(d)[1] for i in range(k)]
        