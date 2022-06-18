from BFSdemo import BFS
from DFSdemo import DFS
from aStardemo import aStar
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

m=maze(20,30)
#m.CreateMaze(1,30,loopPercent=100)
m.CreateMaze(1, 30, loadMaze='maze1.csv')
searchPath,dfsPath,fwdDFSPath=DFS(m)
#bSearch,bfsPath,fwdBFSPath=BFS(m)
#searchAPath, aPath, fwdPath = aStar(m)

textLabel(m,'DFS Path Length',len(fwdDFSPath)+1)
textLabel(m,'DFS Search Length',len(searchPath)+1)
#textLabel(m,'BFS Path Length',len(fwdBFSPath)+1)
#textLabel(m,'BFS Search Length',len(bSearch)+1)
#textLabel(m,'A Path Length',len(fwdPath)+1)
#textLabel(m,'A Search Length',len(searchAPath)+1)


#a=agent(m,footprints=True,color=COLOR.red,filled=True)
b=agent(m,footprints=True,color=COLOR.yellow)
#c = agent(m, footprints=True, color=COLOR.green)
#m.tracePath({a:fwdBFSPath},delay=30)
m.tracePath({b:fwdDFSPath},delay=30)
#m.tracePath({c: fwdPath}, delay=30)

t1=timeit(stmt='DFS(m)',number=1000,globals=globals())
#t2=timeit(stmt='BFS(m)',number=1000,globals=globals())
#t3 = timeit(stmt='aStar(m)', number=1000, globals=globals())

textLabel(m,'DFS Time',t1)
#textLabel(m,'BFS Time',t2)
#textLabel(m,'Astar Time',t3)

m.run()