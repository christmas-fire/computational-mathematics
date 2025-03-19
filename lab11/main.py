import numpy as np
import matplotlib.pyplot as plt

# Функция для вычисления коэффициентов полинома методом наименьших квадратов
def least_squares_approximation(x, y, degree):
    # Создаем матрицу системы для полинома степени degree
    A = np.vander(x, degree + 1, increasing=True)
    
    # Решаем систему уравнений A.T @ A @ coeffs = A.T @ y
    coeffs = np.linalg.lstsq(A, y, rcond=None)[0]
    
    return coeffs

# Функция для вычисления значений полинома
def polynomial_value(coeffs, x):
    return np.polyval(np.flip(coeffs), x)

# Основная программа
if __name__ == "__main__":
    # Исходные данные (замените их на свои данные)
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([1, 1.8, 1.3, 2.5, 6.3, 9.2])
    
    # Степень полинома для аппроксимации
    degree = 2
    
    # Находим коэффициенты полинома
    coeffs = least_squares_approximation(x, y, degree)
    print(f"Коэффициенты полинома: {coeffs}")
    
    # Генерация точек для графика
    x_fit = np.linspace(min(x), max(x), 500)
    y_fit = polynomial_value(coeffs, x_fit)
    
    # Построение графиков
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='red', label='Исходные данные')  # Точки исходных данных
    plt.plot(x_fit, y_fit, color='blue', label=f'Аппроксимация (степень {degree})')  # Аппроксимирующий полином
    plt.title("Аппроксимация методом наименьших квадратов")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()