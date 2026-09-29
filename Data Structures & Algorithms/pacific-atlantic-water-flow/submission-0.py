class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atl = set()
        pac = set()


        def dfs(r, c, visit, height):
            if ((r, c) in visit or 
            r not in range(rows) or
            c not in range(cols) or 
            heights[r][c] < height):
                return 
            visit.add((r, c))
            # neighbors
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc
                dfs(new_row, new_col, visit, heights[r][c])


        for r in range(rows):
            # first col == pac
            # last col == atl
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        for c in range(cols):
            # first row == pac
            # last row == atl
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1,c, atl, heights[rows-1][c])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res





