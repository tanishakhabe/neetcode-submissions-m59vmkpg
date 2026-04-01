class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, elem in enumerate(nums):
            hash_map[elem] = i
    
        for i, elem in enumerate(nums):
            diff = target - elem
            if diff in hash_map and i != hash_map[diff]:
                return [i, hash_map[diff]]
