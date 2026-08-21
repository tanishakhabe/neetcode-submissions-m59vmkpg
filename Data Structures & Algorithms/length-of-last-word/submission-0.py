class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(" ")
        print(s)
        last_word = s[-1]
        return len(last_word)
        