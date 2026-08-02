class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1Counter, s2Counter = {}, {}
        for right in range(len(s1)):
            s1Counter[s1[right]] = s1Counter.get(s1[right], 0) + 1
            s2Counter[s2[right]] = s2Counter.get(s2[right], 0) + 1
        if s1Counter == s2Counter:
            return True
        left = 0
        for i in range(len(s1), len(s2)):
            s2Counter[s2[i]] = s2Counter.get(s2[i], 0) + 1
            s2Counter[s2[left]] -= 1
            if s2Counter[s2[left]] == 0:
                s2Counter.pop(s2[left])
            left += 1
          
            if s1Counter == s2Counter:
                return True
        return False
        
    

        """
        
        """