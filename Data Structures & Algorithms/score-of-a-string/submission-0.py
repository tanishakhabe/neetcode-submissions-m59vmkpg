class Solution:
    def scoreOfString(self, s: str) -> int:
        # convert string s --> list of chars 
        my_list = list(s)
        print(my_list)
        
        my_sum = 0

        for i in range(1, len(my_list)):
        # loop throuhg the my_list
            prev = ord(my_list[i - 1])
            cur = ord(my_list[i])
            abs_diff = abs(cur - prev) 
            print(abs_diff)

            my_sum += abs_diff

        return my_sum