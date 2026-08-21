class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # reduce space complexity
        # by no sorting 
        from collections import Counter
        s_map = Counter(s)
        t_map = Counter(t)
        return s_map == t_map
        
        # return sorted(s) == sorted(t)


 

        