class Solution:
    def wordSearch(self, word, grid):
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.count = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def backtrack(row, col, index, path, dir=None):
            
            if index == len(word):
                self.count += 1
                return
            
            if dir is not None:
                nr = row + dir[0]
                nc = col + dir[1]
                if 0 <= nr < self.rows and 0 <= nc < self.cols and grid[nr][nc] == word[index]:
                    if (nr, nc) not in path:
                        path[(nr, nc)] = grid[nr][nc]
                        backtrack(nr, nc, index + 1, path, dir)
                        del path[(nr, nc)]
            else:
                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols and grid[nr][nc] == word[index]:
                        if (nr, nc) not in path:
                            path[(nr, nc)] = grid[nr][nc]
                            backtrack(nr, nc, index + 1, path, (dr, dc))
                            del path[(nr, nc)]
        
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == word[0]:
                    backtrack(i, j, 1, {(i, j): grid[i][j]})
        return self.count

    def wordSearch2(self, word, grid):
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.count = 0
        
        def checkXMAS(row, col):
            if row == 0 or row == self.rows - 1 or col == 0 or col == self.cols - 1:
                return False
            ms = {"m": [], "s": []}

            x_dir = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
            for dr, dc in x_dir:
                nr = row + dr
                nc = col + dc
                if grid[nr][nc] == 'M':
                    ms['m'].append((nr, nc))
                elif grid[nr][nc] == 'S':
                    ms['s'].append((nr, nc))
                else:
                    print("invalid char")
                    return False
                
            if len(ms['m']) != len(ms['s']):
                print('unbalanced')
                return False
            
            if (ms['m'][0][0] == ms['m'][1][0] and ms['s'][0][0] == ms['s'][1][0]) or\
            (ms['m'][0][1] == ms['m'][1][1] and ms['s'][0][1] == ms['s'][1][1]):
                return True
            print("finally")
            return False

        count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 'A':
                    if checkXMAS(i, j):
                        count += 1
        return count

        

grid = []
while True:
    line = input()
    if line == '':
        break
    grid.append(line)
sol = Solution()
print(sol.wordSearch2("XMAS", grid))