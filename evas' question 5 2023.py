word = "NATURE"
maxy = 6
maxx = 9
grid = [
"N A T S F E G Q N",
"S A I B M R H F A",
"C F T J C U C L T",
"K B H U P T A N U",
"D P R R R J D I R",
"I E E K M E G B E"]
while :
for x in range(len(grid)):
    for y in range(len(grid)):
        if grid[x][y]==word[0]:
            print(x,y)