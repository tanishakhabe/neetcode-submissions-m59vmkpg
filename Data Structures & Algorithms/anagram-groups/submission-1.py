class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for string in strs:
            sorted_chars = sorted(string)
            sorted_s = "".join(sorted_chars)
            print(sorted_s)
            if sorted_s not in dict.keys():
                dict[sorted_s] = [string]
            else:
                dict[sorted_s].append(string)

        return list(dict.values())
