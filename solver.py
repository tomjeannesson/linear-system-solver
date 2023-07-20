from ortools.sat.python import cp_model


class Solver:
    def __init__(self, matrix, granularity=100):
        for row in matrix:
            if len(row) != len(matrix) - 1:
                raise ValueError("Matrix must be x by x-1")
        self.matrix = matrix
        self.granularity = granularity
        self.model = self.create_model()
        self.model.Minimize(self.maximize())

    def create_model(self):
        model = cp_model.CpModel()
        self.users = {}
        for index, row in enumerate(self.matrix):
            self.users[f"user_{index}"] = model.NewIntVar(1, self.granularity, f"user_{index}")
        return model

    def maximize(self):
        error_list = []
        for index, user1 in enumerate(self.users):
            index2 = 0
            total = 0
            for user2 in self.users:
                if user1 != user2:
                    total += self.matrix[index][index2] * self.users[user2]
                    index2 += 1
            error = self.model.NewIntVar(0, 1_000_000_000, f"error_{index}")
            self.model.AddAbsEquality(error, self.users[user1] * 100 * (len(self.matrix) - 1) - total)
            error_list.append(error)

        total_error = self.model.NewIntVar(0, 1_000_000_000, "total_error")
        self.model.AddAbsEquality(total_error, self.granularity - sum(self.users.values()))
        error_list.append(total_error * self.granularity * 10)
        self.error_list = error_list
        return sum(error_list)

    def solve(self, verbose=True) -> dict:
        solver = cp_model.CpSolver()
        status = solver.Solve(self.model)
        print(f"\nModel is {solver.StatusName(status)}.\nMaximum of objective function: {solver.ObjectiveValue()}\n")
        for user, value in self.users.items():
            print(f"{user}: {solver.Value(value) / self.granularity *100}")
        for error in self.error_list:
            print(f"Error: {solver.Value(error)}")
