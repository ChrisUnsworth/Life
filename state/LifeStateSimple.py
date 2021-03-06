import random

from state.LifeState import LifeState


def blank_state(n: int = 4):
    return LifeStateSimple([[0 for _ in range(n)] for _ in range(n)])


def random_state(n: int = 4, p: float = 0.3):
    return LifeStateSimple([[0 if random.random() > p else 1 for _ in range(n)] for _ in range(n)])


class LifeStateSimple(LifeState):
    def __init__(self, state: list):
        self.state = state
        self._size = len(state)

    state: list
    _size: int

    def size(self) -> int:
        return self._size

    def value(self, x: int, y: int) -> int:
        return self.state[x][y]

    def neighbour_sum(self, x: int, y: int) -> int:
        x_m = x - 1 if x > 0 else self._size - 1
        x_p = x + 1 if x < self._size - 1 else 0
        y_m = y - 1 if y > 0 else self._size - 1
        y_p = y + 1 if y < self._size - 1 else 0
        result = self.value(x_m, y_m) + \
            self.value(x_m, y) + \
            self.value(x_m, y_p) + \
            self.value(x_p, y_m) + \
            self.value(x_p, y) + \
            self.value(x_p, y_p) + \
            self.value(x, y_m) + \
            self.value(x, y_p)
        return result

    def evolve_cell(self, x: int, y: int) -> int:
        _sum = self.neighbour_sum(x, y)
        if self.value(x, y) == 0:
            return 1 if _sum == 3 else 0
        if _sum < 2 or _sum > 3:
            return 0
        return 1

    def evolve(self):
        new_state = []
        for x in range(self._size):
            new_state.append([])
            for y in range(self._size):
                new_state[x].append(self.evolve_cell(x, y))
        return LifeStateSimple(new_state)
