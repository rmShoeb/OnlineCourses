def calculate_trace(square_matrix, dimension):
    trace = 0
    for i in range(dimension):
        trace += square_matrix[i][i]
    return trace

# construct a matrix
NUM_ROWS = 25
NUM_COLS = 25
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)
 
# print the matrix
for row in my_matrix:
    print(row)
#print(my_matrix[1][4])
print(calculate_trace(my_matrix, NUM_ROWS))
