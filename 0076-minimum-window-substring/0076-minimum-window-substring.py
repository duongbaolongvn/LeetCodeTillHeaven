class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        tDict = collections.defaultdict(int)
        for c in t:
            tDict[c]+=1
        print(tDict)
        m,n=len(s),len(t)
        need=len(tDict)
        have=0
        l,r=0,0
        mS=""
        ma=float('inf')
        sDict=collections.defaultdict(int)
        for r in range(m):
            # print(sDict)
            sDict[s[r]]+=1
            if tDict.get(s[r],-1) == sDict[s[r]]:
                have+=1
                # print(have)
            while have==need and l<=r:
                if r-l+1<ma:
                    ma=r-l+1
                    mS=s[l:r+1]
                if sDict[s[l]]==tDict.get(s[l],-1):
                    have-=1
                sDict[s[l]]-=1
                l+=1
        return mS
         