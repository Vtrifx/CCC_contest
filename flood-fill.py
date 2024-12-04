class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        v = image[sr][sc]
        row = len(image)
        element = len(image[0])

        def step(y, x):
            if (x >= element) or (y >= row) or (x < 0) or (y < 0) or (image[y][x] != v) or (image[y][x] == color):
                return image

            image[y][x] = color

            step(y, x - 1)
            step(y, x + 1)
            step(y + 1, x)
            step(y - 1, x)

            return image

        return step(sr,sc)

if __name__ == "__main__":
    print(Solution().floodFill([[000],[000]],0,0,0))