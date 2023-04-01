class Base:
    def __init__(self):
        self._base = [['0', '0', '0'],
                      ['0', '0', '0'],
                      ['0', '0', '0']]

    def put(self, x, y, player):
        if 0 <= x <= 2 and 0 <= y <= 2:
            if self._base[y][x] == 'X' or self._base[y][x] == 'O':
                return False
            self._base[y][x] = player
            return True
        return False

    def get_mark(self, x, y):
        return self._base[y][x]

    def is_full(self):
        for row in self._base:
            for case in row:
                if case == '0':
                    return False
        return True

    def get_won_coordinate(self):
        possibles = [[(0, 0), (0, 1), (0, 2)],
                     [(1, 0), (1, 1), (1, 2)],
                     [(2, 0), (2, 1), (2, 2)],
                     [(0, 0), (1, 0), (2, 0)],
                     [(0, 1), (1, 1), (2, 1)],
                     [(0, 2), (1, 2), (2, 2)],
                     [(0, 0), (1, 1), (2, 2)],
                     [(0, 2), (1, 1), (2, 0)]]
        for possible in possibles:
            if self._base[possible[0][0]][possible[0][1]] == \
                    self._base[possible[1][0]][possible[1][1]] == \
                    self._base[possible[2][0]][possible[2][1]] and \
                    self._base[possible[0][0]][possible[0][1]] != '0':
                return [possible[0], possible[2]]
        return [(-1, -1), (-1, -1)]

    def get_won_player(self):
        won_coordinate = self.get_won_coordinate()
        if won_coordinate[0][0] == -1:
            return None
        return self._base[won_coordinate[0][0]][won_coordinate[0][1]]

    def get_base(self):
        return self._base
