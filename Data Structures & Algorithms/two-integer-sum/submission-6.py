class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()

        for i, elem in enumerate(nums):
            my_dict[elem] = i
        
        for i, elem in enumerate(nums):
            diff = target - elem
            
            if diff in my_dict and my_dict[diff] != i:
                return [i, my_dict[diff]]