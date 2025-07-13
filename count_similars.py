
from collections import Counter

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq = Counter()

        for word in words:
            key = ''.join(sorted(set(word)))  
            freq[key] += 1

        count = 0
        for k in freq.values():
            count += k * (k - 1) // 2  

        return count
