class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
# input: an array of nums, an integer k 
# output: k most frequent elements within the array 
        num_map = {}
        freq_array = [[] for i in range(len(nums) + 1)]

        # implementing bucket sort
        for elem in nums:
            num_map[elem] = 1 + num_map.get(elem, 0)

        # populating the freq_array
        for elem, count in num_map.items():
            freq_array[count].append(elem)
            
        res_array = []
        for i in range(len(freq_array) - 1, 0, -1):
            for elem in freq_array[i]:
                res_array.append(elem)
                if len(res_array) == k:
                    return res_array

# edge cases: 
## nums has length 1 --> just return nums

# time complexity: 
# space complexity: O(n) 