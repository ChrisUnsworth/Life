import unittest
from state.LifeState import LifeState, blank_state


class MyTestCase(unittest.TestCase):

    def test_blank_slate(self):
        size = 4
        life_state = LifeState(blank_state(size))
        for x in range(size):
            for y in range(size):
                self.assertEqual(life_state.value(x, y), 0)

    def test_blank_slate_evolved(self):
        size = 4
        life_state_origin = LifeState(blank_state(4))
        life_state = life_state_origin.evolve()
        for x in range(size):
            for y in range(size):
                self.assertEqual(life_state.value(x, y), 0)

    def test_cell_death(self):
        size = 4
        state = blank_state(size)
        state[0][0] = 1
        life_state_origin = LifeState(state)
        for x in range(size):
            for y in range(size):
                if x == 0 and y == 0:
                    self.assertEqual(life_state_origin.value(x, y), 1)
                else:
                    self.assertEqual(life_state_origin.value(x, y), 0)
        life_state = life_state_origin.evolve()
        for x in range(size):
            for y in range(size):
                self.assertEqual(life_state.value(x, y), 0)

    def test_count(self):
        state = blank_state(4)
        state[0][0] = 1
        state[1][2] = 1
        state[2][0] = 1
        life_state = LifeState(state)
        self.assertEqual(life_state.neighbour_sum(1, 1), 3)
        self.assertEqual(life_state.neighbour_sum(1, 0), 2)
        self.assertEqual(life_state.neighbour_sum(0, 0), 0)

    def test_birth(self):
        size = 4
        state = blank_state(size)
        state[0][0] = 1
        state[1][2] = 1
        state[2][0] = 1
        life_state = LifeState(state)
        evolved = life_state.evolve()
        for x in range(size):
            for y in range(size):
                if (x == 1 and y == 1) or (x == 1 and y == 3):
                    self.assertEqual(evolved.value(x, y), 1)
                else:
                    self.assertEqual(evolved.value(x, y), 0)


if __name__ == '__main__':
    unittest.main()
