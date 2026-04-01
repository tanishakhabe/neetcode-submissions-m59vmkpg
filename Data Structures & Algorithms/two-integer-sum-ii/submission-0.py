class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # input - array of numbers sorted in ascending order
        # output - [index1, index2] st nums[index1]+ nums[index2] = target

        left = 0 
        right = len(numbers) - 1
        while left < right: 
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target: 
                left += 1
            else: 
                return [left + 1, right + 1]


        # USE THE FACT THAT THE ARRAY IS SORTED TO YOUR ADVANTAGE!

    
        # time complexity
        # space complexity - O(1)