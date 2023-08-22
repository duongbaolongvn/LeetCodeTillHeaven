class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnts = defaultdict(int)
        
        lo, hi, n = 0, 0, len(s)
        ans = 1
        while hi < n:
            cnts[s[hi]] += 1
            while (hi - lo + 1) - max(cnts.values()) > k:
                cnts[s[lo]] -= 1
                lo += 1
            
            hi += 1
            ans = max(ans, hi - lo)
            
        return ans