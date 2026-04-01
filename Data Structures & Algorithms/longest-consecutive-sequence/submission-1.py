class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums: return 0
        nums_set = set(nums)

        max_len = curr_len = 1
        for elem in nums_set: 
            while elem - 1 in nums_set: 
                curr_len += 1
                elem = elem - 1
                
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1
                continue
        return max_len
                

