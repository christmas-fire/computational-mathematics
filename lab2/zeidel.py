import sys

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

def input_vector(size):
    vector = []
    print("Введите элементы вектора свободных членов:")
    while True:
        try:
            vector = list(map(float, input("Элементы через пробел: ").split()))
            if len(vector) != size:
                print("Ошибка: неверное количество элементов.")
            else:
                break
        except ValueError:
            print("Ошибка: некорректный ввод. Пожалуйста, введите числа.")
    return vector

def decompose_matrix(A):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                C[i][j] = A[i][j]
    
    return C

def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def vector_subtraction(v1, v2):
    return [x - y for x, y in zip(v1, v2)]

def vector_norm(v):
    return sum(x ** 2 for x in v) ** 0.5

def is_strictly_diagonally_dominant(A):
    n = len(A)
    for i in range(n):
        diag = abs(A[i][i])
        row_sum = sum(abs(A[i][j]) for j in range(n) if j != i)
        if diag <= row_sum:
            return False
    return True

def seidel_method(A, B, max_iterations=1000, tolerance=1e-4):
    n = len(A)
    
    # Проверка на строгую диагональную преобладаемость
    if not is_strictly_diagonally_dominant(A):
        print("Ошибка: матрица не удовлетворяет условию сходимости.")
        return None
    
    # Приводим матрицу к виду с единичными диагональными элементами
    for i in range(n):
        if A[i][i] == 0:
            print("Ошибка: диагональный элемент равен нулю.")
            return None
        diag = A[i][i]
        for j in range(n):
            A[i][j] /= diag
        B[i] /= diag
    
    C = decompose_matrix(A)
    x = [0] * n  # Стартовый вектор
    iteration_count = 0  # Переменная для подсчета количества итераций
    
    for k in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            x_new[i] = B[i] - dot_product(C[i], x_new[:i] + x[i+1:])
        
        # Проверка на сходимость
        if vector_norm(vector_subtraction(x_new, x)) < tolerance:
            print(f"Количество итераций: {k + 1}")
            return x_new
        
        x = x_new
        iteration_count += 1
    
    print(f"Предупреждение: достигнуто максимальное количество итераций ({max_iterations}).")
    return x

def main():
    print("Введите кол-во уравнений и неизвестных:")
    n = int(input("Кол-во уравнений: "))
    A = input_matrix(n, n)
    B = input_vector(n)
    solution = seidel_method(A, B)
    if solution is not None:
        print("\nОтвет:")
        for i in range(n):
            print(f'x{i + 1} = {solution[i]}')

if __name__ == "__main__":
    main()