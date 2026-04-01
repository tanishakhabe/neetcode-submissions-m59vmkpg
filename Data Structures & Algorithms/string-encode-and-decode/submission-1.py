class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for word in strs:
            length = len(word)
            final_str += f"{length}" + "#" + word
            print(final_str)
        return final_str

    def decode(self, s: str) -> List[str]:
        result = []
        slow_ptr = 0
        fast_ptr = 0

        while slow_ptr < len(s):
            while s[fast_ptr] != '#':
                fast_ptr += 1
            length = int(s[slow_ptr:fast_ptr])
            print(length)
            slow_ptr = fast_ptr + 1 # Move the slow pointer to the beginning of the next new word
            fast_ptr = slow_ptr + length # Move the fast pointer to the end of the word
            result.append(s[slow_ptr:fast_ptr])
            slow_ptr = fast_ptr

        return result







            # if its a hashtag


            # if its a char

# idea
#"4#neet5#c0des" 

