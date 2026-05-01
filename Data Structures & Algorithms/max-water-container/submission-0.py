class Solution:
    def maxArea(self, heights: List[int]) -> int:
    

    # brute force: try every combination of bars
    # O(n^2)

# left pointer at start
# right pointer at end

        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r: 
            length = r - l
            height = min(heights[r], heights[l])
            area = length * height
            max_area = max(max_area, area)
            # move the pointer of the shorter bar
            # move left forward
            if heights[l] <= heights[r]:
                l += 1
            # move right backwards
            else:
                r -= 1
        return max_area