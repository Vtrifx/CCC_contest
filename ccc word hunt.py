word = "NATURE"
maxy = 6
maxx = 9
grid = [
"NATSFEGQN",
"SAIBMRHFA",
"CFTJCUCLT",
"KBHUPTANU",
"DPRRRJDIR",
"IEEKMEGBE"]

l = []

c = 0
def find(y,x,dx,dy,n,t):
    global c
    if x>=maxx or y>=maxy or x<0 or y<0 or word[n] != grid[y][x]:
        return
    if n == len(word)-1:
        c = c + 1
        return

    print(y, x, n, grid[y][x])
    if n == 0:
        find(y-1, x-1, n+1,"up left", 0)
        find(y+1, x,n + 1, "down", 0)
        find(y-1, x,n + 1, "up",0)
        find(y, x+1,n + 1, "right",0)
        find(y, x-1,n + 1,"left",0)
        find(y + 1, x+1,n + 1,"down right", 0)
        find(y - 1, x+1,n + 1,"up right", 0)
        find(y + 1, x - 1,n + 1, "down left",0)

    if d == "up":
        find(y - 1, x, n + 1, "up", 0)
        if t == 0:
            find(y, x+1,n + 1, "right", 1)
            find(y, x - 1, n + 1, "left", 1)

    if d == "right":
        find(y, x + 1, n + 1, "right", 0)
        if t == 0:
            find(y + 1, x, n + 1, "down", 1)
            find(y-1, x,n + 1, "up", 1)

    if d == "down":
        find(y + 1, x, n + 1, "down", 0)
        if t == 0:
            find(y, x+1,n + 1, "right", 1)
            find(y, x - 1, n + 1, "left", 1)

    if d == "left":
        find(y, x - 1, n + 1, "left", 0)
        if t == 0:
            find(y + 1, x, n + 1, "down", 1)
            find(y-1, x,n + 1, "up", 1)

    if d == "down right":
        find(y + 1, x+1, n + 1, "down right", 0)
        if t == 0:
            find(y-1, x+1,n + 1, "up right", 1)
            find(y+1, x - 1, n + 1, "down left", 1)

    if d == "up right":
        find(y - 1, x+1, n + 1, "up right", 0)
        if t == 0:
            find(y-1, x-1,n + 1, "up left", 1)
            find(y+1, x + 1, n + 1, "down right",1)
    if d == "down left":
        find(y + 1, x-1, n + 1, "down left", 0)
        if t == 0:
            find(y+1, x+1,n + 1, "down right", 1)
            find(y-1, x - 1, n + 1, "up left", 1)
    if d == "up left":
        find(y - 1, x, n - 1, "up left", 0)
        if t == 0:
            find(y-1, x+1,n + 1, "up right", 1)
            find(y+1, x - 1, n + 1, "down left", 1)
# find(0,8,0,"",0)

for row in range(maxy):
    for column in range(maxx):
        find(row,column,0,"",0)


print(c)
