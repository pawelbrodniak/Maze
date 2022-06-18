from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue
from timeit import timeit




def dijkstra(m, *h, start=None):
    if start is None:
        start = (m.rows, m.cols)

    hurdles = [(i.position, i.cost) for i in h]

    unvisited = {n: float('inf') for n in m.grid}
    unvisited[start] = 0
    visited = {}
    revPath = {}
    searchDPath = [start]
    while unvisited:
        currCell = min(unvisited, key=unvisited.get)
        visited[currCell] = unvisited[currCell]
        searchDPath.append(currCell)
        if currCell == m._goal:
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if childCell in visited:
                    continue
                tempDist = unvisited[currCell] + 1
                for hurdle in hurdles:
                    if hurdle[0] == currCell:
                        tempDist += hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell] = tempDist
                    revPath[childCell] = currCell
        unvisited.pop(currCell)

    fwdDPath = {}
    cell = m._goal
    while cell != start:
        fwdDPath[revPath[cell]] = cell
        cell = revPath[cell]
    return searchDPath, fwdDPath, visited[m._goal]


if __name__ == '__main__':
    myMaze = maze(40, 40)
    myMaze.CreateMaze(loadMaze='maze2.csv')

    searchDPath, path, c = dijkstra(myMaze)
    a = agent(myMaze, color=COLOR.red, footprints=True)
    myMaze.tracePath({a: path}, delay=30)

    textLabel(myMaze, 'Dijkstra - długość ścieżki końcowej', c + 1)
    textLabel(myMaze, 'Dijkstra - liczba przeszukań', len(searchDPath))

    t1 = timeit(stmt='dijkstra(myMaze)', number=1000, globals=globals())
    textLabel(myMaze, 'Dijkstra - czas przejścia (s)', t1)
    myMaze.run()
