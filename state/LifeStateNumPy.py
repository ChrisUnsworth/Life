import random
import numpy as np

from state.LifeState import LifeState


def blank_state(n: int = 4):
    return LifeStateNumPy(np.array([[0 for _ in range(n)] for _ in range(n)]))


def random_state(n: int = 4, p: float = 0.3):
    return LifeStateNumPy(np.array([[0 if random.random() > p else 1 for _ in range(n)] for _ in range(n)]))


def _three_to_one(x):
    return 1 if x == 3 else 0


_v_func = np.vectorize(_three_to_one)


class LifeStateNumPy(LifeState):
    def __init__(self, matrix):
        self.matrix = matrix
        self._size = np.size(matrix, 0)
        self._t1 = [i for i in range(self._size)]
        self._t2 = [i for i in range(1, self._size)]
        self._t2.append(0)

    def size(self) -> int:
        return self._size

    def value(self, x: int, y: int) -> int:
        return self.matrix[x][y]

    def evolve(self) -> 'LifeState':
        back = self._shift_back(self.matrix)
        forward = self._shift_forward(self.matrix)
        neighbour_sum = back +  \
            forward +  \
            self._shift_up(self.matrix) +  \
            self._shift_down(self.matrix) +  \
            self._shift_up(back) +  \
            self._shift_down(back) +  \
            self._shift_up(forward) +  \
            self._shift_down(forward)
        new_state = np.maximum(_v_func(neighbour_sum), _v_func(neighbour_sum + self.matrix))
        return LifeStateNumPy(new_state)

    def _shift_forward(self, m):
        result = m.copy()
        result[:, self._t1] = m[:, self._t2]
        return result

    def _shift_back(self, m):
        result = m.copy()
        result[:, self._t2] = m[:, self._t1]
        return result

    def _shift_down(self, m):
        result = m.copy()
        result[self._t2] = m[self._t1]
        return result

    def _shift_up(self, m):
        result = m.copy()
        result[self._t1] = m[self._t2]
        return result
