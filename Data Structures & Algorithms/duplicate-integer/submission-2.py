class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set(nums)
        print(new)
        if len(new) != len(nums): return True
        return False

    # time complexity: 
    # space complexity:     