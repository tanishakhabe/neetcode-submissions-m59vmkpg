class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res


#         max_len = 0
#         l = 0 
#         r = 1
#         while l <= r and r < len(s) - 1:
#             curr_substr = s[l: r + 1]
#             curr_len = len(curr_substr)
#             max_len = max(curr_len, max_len)

#             # expand the substring
#             # while the next character is not in the curr substr
#             # expand the right pointer
#             # curr_len(s[l:r])
#             if s[r + 1] not in curr_substr:
#                 # O(len of the substr, O(n))
#                 r += 1

#             # curr_set = set(curr_substr)
#             # if next_char not in curr_set: 
#             # set lookup is O(1)
            
#             else: # start new substring 
#                 l = r
#                 r = l + 1
#                 curr_len = 0

#         return max_len

# abcd    xyz d

# # "zxyzxyz"
# # max_len = 2
# # l = 0
# # r = 3
# # curr = zxy

# # #     # start building new substr 
# # #     # move left and right pointers to the next char







# # # "zxyzxyz"
# # # substr = zxyzxy

# # # "abcdsdabcde"

# # # # brute force: loop through each possible substring, calculate length,
# # # # return longest 
# # # # O(n^2)

# # # # two pointers approach: 
# # # "zxyzxyz"
# # # # keep track of max_length
# # # # left at the beginning 
# # # # right at the beginning 
# # # # curr-substr  = zxy
# # # # if the next char is diff :
# # #     # r += 1
# # # # else: 
# # #     # start building new substr 
# # #     # move left and right pointers to the next char
# # # # return max(curr_len, max_len)


