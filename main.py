from solver import Solver

if __name__ == "__main__":
    solver = Solver(
        matrix=[
            [100, 100],
            [100, 100],
            [100, 100],
        ]
    )
    solver.solve()
    solver = Solver(
        matrix=[
            [120, 130],
            [80, 100],
            [70, 105],
        ]
    )
    solver.solve()
    solver = Solver(
        matrix=[
            [140, 100],
            [120, 100],
            [100, 80],
        ]
    )
    solver.solve()
