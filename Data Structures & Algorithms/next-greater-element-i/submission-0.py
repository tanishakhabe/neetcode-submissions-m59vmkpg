class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def build_next_greater(nums2):
            stack = []
            next_greater = {}

            for num in reversed(nums2):
                next_greater[num] = -1

                while stack and stack[-1] <= num:
                    stack.pop()

                # Record the answer, if one exists
                if stack and stack[-1] > num: next_greater[num] = stack[-1]

                # Preserve num for future iterations
                stack.append(num)

            return next_greater

        next_greater = build_next_greater(nums2)

        result = []

        for num in nums1:
            result.append(next_greater[num])

        return result