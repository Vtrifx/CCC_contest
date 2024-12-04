class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        c = 0
        maxrow=len(grid)
        maxelement=len(grid[0])

        for row in range(maxrow):
            for element in range(maxelement):
                if grid[row][element] == 1:
                    break
            else:
                continue
            break



        def step(row,element):
            p = 0
            if (element>=maxelement) or (row>=maxrow) or (element<0) or (row<0) or (grid[row][element] == 0) or (grid[row][element] == 2):
                return 0

            grid[row][element] = 2

            if (element+1<maxelement and grid[row][element+1] == 0) or (element+1 >= maxelement):
                p = p + 1
            if (element-1>=0 and grid[row][element-1] == 0) or (element-1 < 0):
                p = p + 1
            if (row + 1 < maxrow and grid[row + 1][element] == 0) or (row + 1 >= maxrow):
                p = p + 1
            if (row - 1 >= 0 and grid[row - 1][element] == 0) or (row - 1 < 0):
                p = p + 1

            p += step(row,element + 1)
            p += step(row + 1, element)
            p += step(row, element - 1)
            p += step(row - 1, element)



            return p

        rez=step(row, element)

        return rez


if __name__ == "__main__":
    print(Solution().islandPerimeter([[1],[0]]))