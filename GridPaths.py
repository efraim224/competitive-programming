def count_path(row, column, length, matrix):
    if row == length and column == length and matrix[length][length] == '.':
        return 1
    if row > length or column > length:
        return 0
    if matrix[row][column] == '.':
        return count_path(row,column+1,length, matrix) + count_path(row+1,column,length, matrix)
    return 0


length = int(input())
matrix = []
for i in range(0,length):
    row = input()
    matrix.insert(i, [x for x in row])

print(count_path(0,0,length -1, matrix))