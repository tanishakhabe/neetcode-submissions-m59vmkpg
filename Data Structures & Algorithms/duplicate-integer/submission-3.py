class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash map
        from collections import Counter

        map = Counter(nums)
        for val in map.values():
            if val > 1:
                return True
        return False
        