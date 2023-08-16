class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxR = height[0]
        maxL = height[len(height) -1]
        i, j = 0, len(height)-1
        
        while i != j:
            if maxR <= maxL:
                i += 1
                if maxR-height[i] > 0: res += maxR-height[i]
                else: maxR = height[i]
                    
            else: 
                j -= 1
                if maxL-height[j] > 0: res += maxL - height[j]
                else: maxL = height[j]
                    
        return res
    
        