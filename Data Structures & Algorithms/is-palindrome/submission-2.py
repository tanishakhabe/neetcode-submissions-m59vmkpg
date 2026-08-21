class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = s.lower()
        cleaned_text = " ".join(char for char in s if char.isalnum())
        cleaned_list = cleaned_text.split(" ")
        print(cleaned_list)
        
        l = 0
        r = len(cleaned_list) - 1

        while l < r: 
            if cleaned_list[l] == cleaned_list[r]: 
                l += 1
                r -= 1
            else: 
                return False
        return True