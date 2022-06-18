from pyamaze import maze, agent, COLOR, textLabel
from timeit import timeit

def RCW():
    global direction
    k = list(direction.keys())
    v = list(direction.values())
    v_rotated = [v[-1]] + v[:-1]
    direction = dict(zip(k, v_rotated))


def RCCW():
    global direction
    k = list(direction.keys())
    v = list(direction.values())
    v_rotated = v[1:] + [v[0]]
    direction = dict(zip(k, v_rotated))


def moveForward(cell):
    if direction['forward'] == 'E':
        return (cell[0], cell[1] + 1), 'E'
    if direction['forward'] == 'W':
        return (cell[0], cell[1] - 1), 'W'
    if direction['forward'] == 'N':
        return (cell[0] - 1, cell[1]), 'N'
    if direction['forward'] == 'S':
        return (cell[0] + 1, cell[1]), 'S'


def wallFollower(m):
    global direction
    direction = {'forward': 'N', 'left': 'W', 'back': 'S', 'right': 'E'}
    currCell = (m.rows, m.cols)
    path = ''
    while True:

        if currCell == (1, 1):
            break
        if m.maze_map[currCell][direction['left']] == 0:
            if m.maze_map[currCell][direction['forward']] == 0:
                RCW()
            else:
                currCell, d = moveForward(currCell)
                path += d
        else:
            RCCW()
            currCell, d = moveForward(currCell)
            path += d
    path2 = path
    while 'EW' in path2 or 'WE' in path2 or 'NS' in path2 or 'SN' in path2:
        path2 = path2.replace('EW', '')
        path2 = path2.replace('WE', '')
        path2 = path2.replace('NS', '')
        path2 = path2.replace('SN', '')
    return path, path2


if __name__ == '__main__':
    myMaze = maze(5, 5)
#    myMaze.CreateMaze()
    myMaze.CreateMaze(loadMaze='maze3.csv')

    path, path2 = wallFollower(myMaze)
    b = agent(myMaze, footprints=True, color=COLOR.red)
    myMaze.tracePath({b: path2}, delay=30)


    textLabel(myMaze, 'Wall fallower - długość ścieżki końcowej', len(path2) + 1)
    textLabel(myMaze, 'Wall fallower - liczba przeszukań', len(path) + 1)

    t1 = timeit(stmt='wallFollower(myMaze)', number=1000, globals=globals())
    textLabel(myMaze, 'Wall fallower - czas przejścia (s)', t1)
    myMaze.run()