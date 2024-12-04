class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        maxr = len(grid)
        maxc = len(grid[0])
        for row in range(maxr):
            for element in range(maxc):
                if grid[row][element] == 1:
                    break
            else:
                continue
            break


        q = []
        q.append((row,element))
        p = 0
        while q:
            cur = q.pop(0)
            print(cur)
            grid[cur[0]][cur[1]] = 2

            if (cur[1]+1<maxc and grid[cur[0]][cur[1]+1] == 0) or (cur[1]+1 >= maxc):
                p = p + 1
            if (element-1>=0 and grid[cur[0]][cur[1]-1] == 0) or (cur[1]-1 < 0):
                p = p + 1
            if (cur[0] + 1 < maxr and grid[cur[0] + 1][cur[1]] == 0) or (cur[0] + 1 >= maxr):
                p = p + 1
            if (cur[0] - 1 >= 0 and grid[cur[0] - 1][cur[1]] == 0) or (cur[0] - 1 < 0):
                p = p + 1

            neighbours = [(cur[0]+1,cur[1]), (cur[0]-1, cur[1]), (cur[0],cur[1]+1), (cur[0], cur[1]-1)]

            for n in neighbours:
                if (n[0]<maxr) and (n[1]<maxc) and (n[0]>=0) and (n[1]>=0) and (grid[n[0]][n[1]] != 0) and (grid[n[0]][n[1]] != 2):
                    q.append(n)
        return p






        # [[1,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
if __name__ == "__main__":
    print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))