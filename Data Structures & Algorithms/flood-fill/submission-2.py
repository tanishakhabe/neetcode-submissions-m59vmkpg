class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image
        # basically running BFS from image[sr][sc]
    
        nrow, ncol = len(image), len(image[0])
        orig_color = image[sr][sc]
        image[sr][sc] = color

        q = collections.deque([(sr, sc)])
        visit = {(sr, sc)}
        
        while q:
            curr_row, curr_col = q.popleft()
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                r = curr_row + dr
                c = curr_col + dc 
                if (r in range(nrow)) and (c in range(ncol)) and (image[r][c] == orig_color) and ((r, c) not in visit):
                    image[r][c] = color
                    visit.add((r, c))
                    q.append((r, c))
        return image

                

