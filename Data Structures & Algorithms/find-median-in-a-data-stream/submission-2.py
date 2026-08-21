class MedianFinder:

    import heapq
    def __init__(self):
        
        self.smaller = []
        self.larger = []
        
    def addNum(self, num: int) -> None:
        # add the new number 
        if not self.larger: 
            heapq.heappush(self.larger, num)
            return

        # if its less or greater than the median
        if num < self.larger[0]:
            heapq.heappush(self.smaller, -num)
        else:
            heapq.heappush(self.larger, num)

        # check sizes of the heaps
        # even:
        # smaller = larger
        if len(self.smaller) > len(self.larger): 
            to_move = -heapq.heappop(self.smaller)
            heapq.heappush(self.larger, to_move)

        # odd:
        # larger = smaller + 1
        elif len(self.larger) - len(self.smaller) > 1: 
            to_move = heapq.heappop(self.larger)
            heapq.heappush(self.smaller, -to_move)

    def findMedian(self) -> float:
        # if even num of elements
        if len(self.smaller) == len(self.larger):
            first = -self.smaller[0]
            second = self.larger[0]
            median = (first + second) / 2

        # if odd num of elements
        else:
            median = self.larger[0]
        return median
            
        
       

        
        