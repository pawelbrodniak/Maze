# from pyMaze import maze,agent,COLOR,textLabel
from timeit import timeit

from pyamaze import maze,agent,textLabel,COLOR

def DFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSeacrh=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        dSeacrh.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dSeacrh,dfsPath,fwdPath

if __name__=='__main__':
    m=maze(5,5)
    #m.CreateMaze(1,1)
    m.CreateMaze(loadMaze='maze5.csv')

    dSeacrh,dfsPath,fwdPath=DFS(m)
    c = agent(m, footprints=True, color=COLOR.red)
    m.tracePath({c: fwdPath}, delay=30)

    l = textLabel(m, 'DFS - długość ścieżki końcowej', len(fwdPath) + 1)
    l = textLabel(m, 'DFS - liczba przeszukań', len(dSeacrh))

  #  t1 = timeit(stmt='m', number=1000, globals=globals())
    t1 = timeit(stmt='DFS(m)', number=1000, globals= globals())
    textLabel(m, 'DFS - czas przejścia (s)', t1)
    m.run()
