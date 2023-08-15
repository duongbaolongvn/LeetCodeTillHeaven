class Solution:
    def longestPalindrome(self, s: str) -> str:
       
        def LP(l,r):
            while l >= 0 and r < len(s):
                if s[l] != s[r]: break
                l -= 1
                r += 1
            return l+1, r
        
        resL, resR = 0, 0
        
        for i in range(len(s)):
            l, r = LP(i, i)
            if (r-l) > (resR - resL):
                resR = r
                resL = l
                
            l, r = LP(i,i+1)
            if (r-l) > (resR - resL):
                resR = r
                resL = l
                
        return s[resL:resR]
        