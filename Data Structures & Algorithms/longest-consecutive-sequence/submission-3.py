class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        for elem in my_set:
            if (elem - 1) in my_set:
                continue
            
            else: # its the start of a sequence
                curr = 1
                temp = elem
                while (temp + 1) in my_set:
                    curr += 1
                    temp += 1
                longest = max(longest, curr)
        return longest
            
                    



        