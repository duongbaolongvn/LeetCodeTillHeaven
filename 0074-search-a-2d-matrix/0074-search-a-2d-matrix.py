class Solution:
    def bisect_left(a, x, lo=0, key=None):
        
        # If key is provided, adjust the target and sequence accordingly
        if key:
            get_key = lambda index: key(a[index])
        else:
            get_key = lambda index: a[index]

        while lo < hi:
            mid = (lo + hi) // 2
            if get_key(mid) < x:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if target > matrix[-1][-1]: return False
            
        row = matrix[bisect_left(matrix, target, key = lambda x : x[-1])]
        
        index = bisect_left(row, target)

        return row[index] == target