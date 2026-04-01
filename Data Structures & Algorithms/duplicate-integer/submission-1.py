class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = []
        for item in nums:
            if item in new: return True
            new.append(item)
        return False
        