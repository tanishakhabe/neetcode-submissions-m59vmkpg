class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for elem in strs:
            
            sorted_elem = "".join(sorted(elem))
            
            if sorted_elem in my_dict.keys():
                my_dict[sorted_elem].append(elem)
            
            else:
                my_dict[sorted_elem] = [elem]
            
    
        
        return list(my_dict.values())