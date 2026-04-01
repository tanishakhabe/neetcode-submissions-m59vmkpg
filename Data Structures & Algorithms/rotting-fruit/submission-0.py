class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        fresh = 0
        minutes = 0
        q = collections.deque()

        # add all rotten fruits first like all the starting points for BFS
        for r in range(nrow):
            for c in range(ncol):
                # if rotten --> add it to the queue to visit its neighbors
                if grid[r][c] == 2: 
                    q.append((r, c))
                # if fresh --> add it to the fresh count
                elif grid[r][c] == 1:
                    fresh += 1

        # while there are still rotten oranges left in the queue  
        # and while still fresh oranges 
              
        while q and fresh > 0: 
            for i in range (len(q)):
                r, c = q.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions: 
                    curr_row = r + dr
                    curr_col = c + dc
                    if ((curr_row in range(nrow)) and 
                    (curr_col in range(ncol)) and 
                    (grid[curr_row][curr_col] == 1)): 
                        grid[curr_row][curr_col] = 2
                        # this fruit turned from fresh to rotten
                        fresh -= 1 
                        # turn its neighbors rotten so we add it to the queue
                        q.append((curr_row, curr_col))
            # after one level, update minutes
            minutes += 1 
        return minutes if fresh == 0 else -1
    



