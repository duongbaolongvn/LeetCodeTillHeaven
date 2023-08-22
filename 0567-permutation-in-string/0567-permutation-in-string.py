class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
    
        k  = len(s1)
        cur_str = s2[:k]
        for i in range(len(s2) - k):
            if sorted(s1) == sorted(cur_str):
                return True
            else:
                cur_str = cur_str[1:k]
                cur_str+=s2[i+k]

        if sorted(s1) == sorted(cur_str):
            return True

        return False