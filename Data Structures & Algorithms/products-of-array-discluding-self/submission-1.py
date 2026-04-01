class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


# brute force idea:
# loop through list
# first, figure out total product (multiplying each elem)
# for each elem: 
    # if elem is 0: return total product without the 0

    # calculate total product / elem
    # append to the output

# edge cases:
# every elem is the same: 
# [5, 5, 5]  #total prod = 25

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res


    
