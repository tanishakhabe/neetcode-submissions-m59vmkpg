class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # build prefix array
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        # build postfix array 
        postfix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix[i] * postfix[i]
        
        return output




        