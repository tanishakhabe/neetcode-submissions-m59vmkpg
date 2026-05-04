class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r: 

            # if subarray already sorted: 
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # need to set m and res
            m = (l + r) // 2
            res = min(res, nums[m])

            # is mid value a part of the left sorted portion
            if nums[m] >= nums[l]: 
                l = m + 1

            else:
                r = m - 1
        return res



        
    



# run binary search 

# nums[m] >= nums[l]: 
    # search right
# else: 
    # search left 
