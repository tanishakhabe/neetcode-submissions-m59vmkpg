class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        if not grid:
            return -1
    
        if (grid[0][0] == 1) or (grid[rows-1][cols-1] == 1):
            return -1

        from collections import deque
        queue = deque([(0, 0, 1)])
        visit.add((0, 0))
    
        while queue:
                curr_row, curr_col, curr_length = queue.popleft()
                if (curr_row, curr_col) == (rows-1, cols-1): return curr_length
                
                # check its neighbors to find the next valid neighbor (must be 0) to visit
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
                for dr, dc in directions:
                    new_row, new_col = curr_row + dr, curr_col + dc

                    # check if valid neighbor to add to path
                    # must be in bounds
                    # must not be in visit
                    # must be 0

                    if ((new_row, new_col) not in visit) and (new_row in range(rows)) and (new_col in range(cols)) and (grid[new_row][new_col] == 0):

                # add the valid neighbor to visit set and to the queue
                        new_length = curr_length + 1
                        visit.add((new_row, new_col))
                        queue.append((new_row, new_col, new_length))

        return -1
