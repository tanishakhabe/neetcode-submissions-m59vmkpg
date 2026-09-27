class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        from collections import deque

        rows, cols = len(grid), len(grid[0])
        fresh = 0
        time = 0
        queue = deque()


        # initialize bfs starting points
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0: 
            for i in range(len(queue)):
                curr_row, curr_col = queue.popleft()
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    new_row = curr_row + dr
                    new_col = curr_col + dc

                    # check if neighbor is valid
                    if ((new_row in range(rows)) and 
                    (new_col in range(cols)) and 
                    ((grid[new_row][new_col]) == 1)): # still fresh
                        # make it rotten
                        grid[new_row][new_col] = 2

                        # decrement fresh
                        fresh -= 1

                        # add it to the queue so we can rot its neighbors
                        queue.append((new_row, new_col))
            time += 1
        return time if fresh == 0 else -1


                
        
        
        
        
        