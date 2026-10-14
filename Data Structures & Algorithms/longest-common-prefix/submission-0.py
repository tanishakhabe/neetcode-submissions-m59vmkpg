class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        lcp = ""
        
        for i in range(len(first_word)):
            for word in strs[1:]:
                if i > (len(word) - 1): return lcp
                if first_word[i] != word[i]:
                    return lcp
            lcp += first_word[i]
        return lcp
    


        



        
        