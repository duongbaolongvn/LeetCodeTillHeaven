class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        res = min(height[i], height[j])*(j-i)
        
        while i != j:  
            if height[i] < height[j]: 
                i += 1
                if min(height[i], height[j])*(j-i) > res: res = min(height[i], height[j])*(j-i)
                    
            else: 
                j -= 1
                if min(height[i], height[j])*(j-i) > res: res = min(height[i], height[j])*(j-i)
                    
        return res
    
            