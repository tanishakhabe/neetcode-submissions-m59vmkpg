class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r: 
            if nums[l] != val: 
                l += 1
            else:
                nums[l] = nums[r]
                r -= 1
        return r+1





        