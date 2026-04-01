class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_words = dict()
        big_list = []
        for word in strs:
            if tuple(sorted(word)) not in my_words:
                my_words[tuple(sorted(word))] = [word]
            else: 
                my_words[tuple(sorted(word))].append(word)
                
            big_list = list(my_words.values())
        return big_list 

# brute force solution: 
    # see a new_word --> 
    # check if sorted(word) is already in dict
        # if yes, add new_word to the key_value pair list
        # if no, create new_key_value pair with sorted(new_word) as the key
    # combine all mini lists from the dictionary at the end

    # store all mini lists in a dictionary structure
    # "word": [list of its anagrams]

# edge cases: 
## list with one word --> list within a list
## list with empty quotations --> list within a list
## empty list? --> list within a list


# time complexity: 



# space complexity 