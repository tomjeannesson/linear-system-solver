from solver import Solver

GRANULARITY = 100000
if __name__ == "__main__":
    solver = Solver(
        matrix=[
            [100, 100],
            [100, 100],
            [100, 100],
        ],
        granularity=GRANULARITY,
    )
    solver.solve()
    solver = Solver(
        matrix=[
            [120, 130],
            [80, 100],
            [70, 105],
        ],
        granularity=GRANULARITY,
    )
    solver.solve()
    solver = Solver(
        matrix=[
            [140, 100],
            [120, 100],
            [100, 80],
        ],
        granularity=GRANULARITY,
    )
    solver.solve()
