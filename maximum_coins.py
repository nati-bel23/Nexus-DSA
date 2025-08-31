 def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)  
        n = len(piles) // 3       
        total = 0
        idx = 1  
        for _ in range(n):
            total += piles[idx]
            idx += 2  
        return total
