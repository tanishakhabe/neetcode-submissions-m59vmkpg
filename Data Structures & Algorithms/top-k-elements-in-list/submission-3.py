class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        freq_map = Counter(nums)
        # convert the dictionary into a list
        freq_items = [(count, num) for num, count in freq_map.items()]


        # heapify the list
        heapq.heapify(freq_items)

        while len(freq_items) > k: 
            heapq.heappop(freq_items)
        
        return [num for (count, num) in freq_items]

        