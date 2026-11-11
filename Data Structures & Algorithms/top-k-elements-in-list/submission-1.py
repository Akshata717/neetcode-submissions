from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        arr = []
        while k > 0:
            max_key = max(c, key=c.get)
            arr.append(max_key)
            c.pop(max_key)
            k -= 1
        return arr