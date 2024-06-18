import numpy as np

array = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])

row_sums = array.sum(axis=1)
col_sums = array.sum(axis=0)

print("\n".join(" ".join(map(str, row)) + " | " + str(sum(row)) for row in array))
print("- " * array.shape[1])
print(" ".join(map(str, col_sums)))