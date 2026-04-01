class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # idea is to maintain prev sum or start fresh with curr sum
        prev_sum = nums[0]
        curr_sum = 0
        
        for elem in nums:
            if curr_sum < 0: curr_sum = 0
            curr_sum += elem
            prev_sum = max(prev_sum, curr_sum)
        return prev_sum
        