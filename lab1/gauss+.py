import random
import sys

def SwapRow(matrix, start):
    row_number = start
    pred = abs(matrix[start][start])
    for i in range(start + 1, len(matrix)):
        if(pred < abs(matrix[i][start])):
            pred = abs(matrix[i][start])
            row_number = i
    if(row_number != start):
        matrix[start], matrix[row_number] = matrix[row_number], matrix[start]
    return matrix

def Gaus(matrix, start):
    matrix = SwapRow(matrix, start)
    
    if(matrix[start][start] == 0):
        for i in range(start + 1, len(matrix)):
            if(matrix[i][start] != 0):
                matrix[i], matrix[start] = matrix[start], matrix[i]
    
    for i in range(start + 1, len(matrix)):
        if(matrix[i][start] != 0):
            koef = matrix[i][start] / matrix[start][start]
            for j in range(start, len(matrix[i])):
                matrix[i][j] = matrix[i][j] - koef * matrix[start][j]

    return matrix

def input_matrix(rows, columns):
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Строка {i + 1}: ").split()))
                if len(row) != columns:
                    print("Ошибка: неверное количество элементов в строке.")
                else:
                    matrix.append(row)
                    break
            except ValueError:
                print("Ошибка: некорректный ввод. Пожалуйста, введите числа.")
    return matrix

print("Введите кол-во уравнений и неизвестных: ")
rows = int(input("Кол-во уравнений: "))
column = int(input("Кол-во переменных: "))

if(rows != column):
    print("Error: неравное количество уравнений и неизвестных")
    sys.exit()

# matrix = [[random.randint(-10, 10) for _ in range(column + 1)] for _ in range(rows)]
matrix = input_matrix(rows, column+1)
print("\nМатрица:")
for i in range(rows):
    print(*matrix[i])

for k in range(rows - 1):
    matrix = Gaus(matrix, k)

print("\nМетод Гауса:")
for i in range(rows):
    print(*matrix[i])

solution = [1 for _ in range(rows)]

if(matrix[rows - 1][column] == 0 and matrix[rows - 1][column - 1] == 0):
    print("Бесконечно много решений")
    sys.exit()
elif(matrix[rows - 1][column - 1] == 0):
    print("Нет решений")   
    sys.exit()
else:
    solution[column - 1] = matrix[rows - 1][column] / matrix[rows - 1][column - 1]


for i in range(rows - 2, -1, -1):
    sum = matrix[i][column]
    for j in range(column - 1, i, -1):
        sum -= matrix[i][j] * solution[j]
    if(sum == 0 and matrix[i][j - 1] == 0):
        print("Бесконечно много решений")
        sys.exit()
    elif(matrix[i][j - 1] == 0):
        print("Нет решений")
        sys.exit()
    else:
        solution[j - 1] = sum / matrix[i][j - 1]

print()
print("Ответ:")
for i in range(rows):
    print(f'x{i+1} = {solution[i]}')