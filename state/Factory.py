from state.LifeStateNumPy import blank_state as bs, random_state as rs


def blank_state(n: int = 4) -> 'LifeState':
    return bs(n)


def random_state(n: int = 4, p: float = 0.3) -> 'LifeState':
    return rs(n, p)
