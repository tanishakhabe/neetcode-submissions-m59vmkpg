class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
    # [3,4,5,6,1,2] 
    # run binary search on the sorted components
        l = 0 
        r = len(nums) - 1

        while l <= r:
            if target == nums[l]: 
                return l
            if target == nums[r]:
                return r
            
            m = (l + r) // 2
            if target == nums[m]: return m

            # first move component boundary 
            # then check if target in range
            
            if nums[m] >= nums[l]:
                if target > nums[m] or  target < nums[l]: # target not in l->m window
                    l = m + 1
                else:
                    r = m - 1

            else: # nums[m] < nums[l]
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
                
        return -1


        # if nums[l] <= target <= nums[m]: 
        # do binary search on left half

        # else: 
        # do binary search on the right half
