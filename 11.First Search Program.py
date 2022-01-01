grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],[0, -1],[1, 0],[0, 1]]
#delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    closed = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0

    open_list = [[g, x, y]]
    path = []
    finish,fail = 0,0

    while finish == 0 and fail == 0:
        if len(open_list) == 0:
            fail == 1
            print('fail')
            return 'fail'

        open_list.sort()
        open_list.reverse()
        g, x, y = open_list.pop()

        if goal == [x, y]:
            finish == 1
            print([g, x, y])
            return ([g, x, y])

        for m_x, m_y in delta:
            x2 = x + m_x
            y2 = y + m_y
            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                if grid[x2][y2] == 0 and closed[x2][y2] == 0:
                    g2 = g + cost
                    open_list.append([g2, x2, y2])
                    closed[x2][y2] = 1

    return path

search(grid, init, goal, cost)