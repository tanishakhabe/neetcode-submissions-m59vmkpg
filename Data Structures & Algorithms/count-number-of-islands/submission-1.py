class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        # we're doing bfs from each land cell
        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visit.add((r, c))

            while queue:
                curr_row, curr_col = queue.popleft()    # getting the current node
                # logic to get its neigbors
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for dr, dc in directions:
                    new_row = curr_row + dr
                    new_col = curr_col + dc

                    # if neighbor not in visit: 
                    if ((new_row, new_col) not in visit) and (new_row in range(rows)) and (new_col in range(cols)) and (grid[new_row][new_col] == "1"):
                        visit.add((new_row, new_col))
                        queue.append((new_row, new_col))


        for r in range(rows):
            for c in range(cols):
                # if land cell and not in visit --> do bfs
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1 
        return islands
                    
                
    
        
            


        
        

         