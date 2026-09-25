class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        import math

        if n==h:
            return max(piles)
        total=sum(piles)  
        left=1
        right=max(piles)
        while left<=right:
           mid=(right+left)//2
           hours = 0
           for pile in piles:
            hours += math.ceil(pile / mid)
           if hours <= h:
            right = mid - 1
           else:
            left = mid + 1

        return left



        