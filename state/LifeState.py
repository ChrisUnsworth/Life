class LifeState:

    def size(self) -> int:
        pass

    def value(self, x: int, y: int) -> int:
        pass

    def evolve(self) -> 'LifeState':
        pass
