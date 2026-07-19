class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # [2, 4, 5, 3, 1, 2]

        # [5, 5, 3, 2, 2, -1]

        # [7, 4, 5, 6, 1]
        
        # [6, 6, 6, 1, -1]
        
        # two pointers approach
        # one pointer stays at the maximum value
        # another pointer moves through the list


        # traverse through the array backwards

        # new max = max(oldmax, arr[i])

        old_max = -1

        for i in range((len(arr) - 1), -1, -1):

            new_max = max(old_max, arr[i])
            arr[i] = old_max
            old_max = new_max

        return arr
