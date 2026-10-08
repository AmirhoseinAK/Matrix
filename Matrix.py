# valuables and inputs

def Getting_Input():
    my_matrix = list()
    for i in range(3):
        my_input = (input(f"write numbers in {i+1} row: ")).split()
        my_matrix.append(my_input)
    return my_matrix

# Row sums

def Row_Sums(my_matrix):
    row = 0
    row_sum = list()
    for i in range(3):
        for g in range(3):
            row += int(my_matrix[i][g])
        row_sum.append(row)
        row = 0
    return row_sum

# Column sums

def Column_Sums(my_matrix):
    column = 0
    column_sum = list()
    for i in range(3):
        for g in range(3):
            column += int(my_matrix[g][i])
        column_sum.append(column)
        column = 0
    return column_sum

#setting valuables

my_matrix = Getting_Input()
R = Row_Sums(my_matrix)
C = Column_Sums(my_matrix)
print(f" row 1 is: {R[0]} \n row 2 is: {R[1]} \n row 3 is: {R[2]}")
print(f"column 1 is: {C[0]} \ncolumn 2 is: {C[1]} \ncolumn 3 is: {C[2]}")