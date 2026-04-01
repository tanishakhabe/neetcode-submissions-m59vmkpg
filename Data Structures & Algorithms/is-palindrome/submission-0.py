class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first, remove all spaces from the string
        # race car --> racecar
        # 1 pointer at front
        # 1 pointer at back
        # if not the same, return False
        
        s = s.replace(" ", "")
        s = s.lower()

        print(s)
        left = 0
        right = len(s) - 1

        while left < right:
            print(s[left])
            print(s[right])
            if not s[left].isalnum(): 
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1 
                continue
            if s[left] != s[right]: return False
            else:
                left += 1
                right -= 1
        return True

        