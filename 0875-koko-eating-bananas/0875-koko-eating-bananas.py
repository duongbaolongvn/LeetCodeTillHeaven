class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        lo,hi=1,max(piles)
        while lo<=hi:
            mid=lo+(hi-lo)//2
            count=0
            for i in piles:
                count+=i//mid
                if i%mid!=0:
                    count+=1
            if count>h:
                lo=mid+1
            else:
                hi = mid - 1
        return lo