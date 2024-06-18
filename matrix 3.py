def sum_diagonals(matrix):
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("Matrix must be square")
    primary_diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
    secondary_diagonal_sum = sum(matrix[i][len(matrix) - i - 1] for i in range(len(matrix)))
    n = len(matrix)
    print(" " * 20)
    for i in range(n):
        print(" " * 10, end="")
        for j in range(n):
            if i == j:
                print(f"\033[92m[{matrix[i][j]:>2}]\033[0m", end="")
            elif i + j == n - 1:
                print(f"\033[94m[{matrix[i][j]:>2}]\033[0m", end="")
            else:
                print(f"[{matrix[i][j]:<3}]", end="")
        print()
    print(" " * 20)
    print(f"{'Sum of primary diagonal elements:':^40}")
    print(f"{primary_diagonal_sum:^40}")
    print(f"{'Sum of secondary diagonal elements:':^40}")
    print(f"{secondary_diagonal_sum:^40}")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_diagonals(matrix)