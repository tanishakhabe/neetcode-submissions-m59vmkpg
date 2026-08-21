class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left = 0 
        right = 0 
        diff = 0

        while right < len(t):
            if left >= len(s): 
                diff += len(t) - right
                return diff

            if s[left] == t[right]:
                left += 1
                right += 1

            else:
                left += 1

        return diff
            
