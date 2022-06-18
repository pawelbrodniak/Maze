from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue
from timeit import timeit

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))


def aStar(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    open = PriorityQueue()
    open.put((h(start, m._goal), h(start, m._goal), start))
    aPath = {}
    g_score = {row: float("inf") for row in m.grid}
    g_score[start] = 0
    f_score = {row: float("inf") for row in m.grid}
    f_score[start] = h(start, m._goal)
    searchAPath = [start]
    while not open.empty():
        currCell = open.get()[2]
        searchAPath.append(currCell)
        if currCell == m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, m._goal)

                if temp_f_score < f_score[childCell]:
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_g_score + h(childCell, m._goal)
                    open.put((f_score[childCell], h(childCell, m._goal), childCell))

    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return searchAPath, aPath, fwdPath


if __name__ == '__main__':
    m = maze(3, 3)
    #m.CreateMaze(1,1)
    m.CreateMaze(loadMaze='maze2.csv')

    searchAPath, aPath, fwdPath = aStar(m)
    c = agent(m, footprints=True, color=COLOR.red)
    m.tracePath({c: fwdPath}, delay=30)

    l = textLabel(m, 'A Star - długość ścieżki końcowej', len(fwdPath) + 1)
    l = textLabel(m, 'A Star - liczba przeszukań', len(searchAPath))

    t1 = timeit(stmt='aStar(m)', number=1000, globals=globals())
    textLabel(m, 'A-Star - czas przejścia (s)', t1)
    m.run()

