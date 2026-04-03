class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # nums = [1,2,2,3,3,3], k = 2
        # 1: 1
        # 2: 2 
        # 3: 3        


        # nums = [7,7], k = 1
        # 7: 2

        # edge cases: 
        # nums = [4], k=4
        # return 4
        res = []

        # count frequency of each element
        from collections import Counter
        freq = Counter(nums)
        print(freq)

        # return top k by using the most_common(k)
        top_k = freq.most_common(k)
        print(top_k)
        for elem, freq in top_k:
            res.append(elem)

        return res
            
