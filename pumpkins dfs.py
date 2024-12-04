# grid = ["**LMLS",
# "S*LMMS",
# "S*SMSM",
# "******",
# "LLM*MS",
# "SSL*SS"]

grid = ["**LMLS",
"S*LMMS",
"S*SMSM",
"***SLL",
"LLM*MS",
"SSL*SS"]
y = 2
x = 4
rows = 6
columns = 6
visited = []
rez = 0
def sizes(s):
    if s == "L":
        return 10
    if s == "M":
        return 5
    if s == "S":
        return 1
def pumpkins(y,x):
    global rez
    if y>=rows or x >= columns or y<0 or x<0 or grid[y][x] == "*" or (y,x) in visited:
        return 0
    visited.append((y,x))
    rez = rez + sizes(grid[y][x])
    pumpkins(y+1,x)
    pumpkins(y-1,x)
    pumpkins(y,x+1)
    pumpkins(y,x-1)
    return rez
rez = pumpkins(y,x)
print(rez)

