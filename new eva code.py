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
def find(y,x,dy,dx,n,turn=False): #n is pointer (index)
    global c
    if x>=maxx or y>=maxy or x<0 or y<0 or word[n] != grid[y][x]:
        return
    if n == len(word)-1:
        print(y, x, n)
        c+=1
        return


    hor = [(0,1),(1,0),(-1,0),(0,-1)] #posibilities for dx and dy if the thing is horizontal
    dia = [(1,1),(-1,-1),(-1,1),(1,-1)] #posibilities for dx and dy if the thing is diagonal

    if n == 0:
        for i,m in hor+dia:
            find(y + i, x + m, i, m, n + 1, False)

    #check if the cordinates turned.
    if turn == True:
        find(y+dy,x+dx,dy,dx,n+1,turn)
    else:
        if dy*dx == 0:
            opt = hor # then the word is going horizontally or vertically
        else:
            opt = dia
        for i,m in opt:
            if dy+i == 0 and dx+m==0:
                pass
            else:
                # not sure: update the value of dy, dx to i,m
                if dy!=i and dx!=m:
                    turn = True
                else:
                    turn=False
                find(y + i, x + m, i, m, n + 1, turn)
#find index of every letter that is the first letter of the word
for row in range(maxy):
    for column in range(maxx):
        if grid[row][column] == word[0]:
            print('r and c:', row,column)
            find(row,column,0,0,0)


print(c)
