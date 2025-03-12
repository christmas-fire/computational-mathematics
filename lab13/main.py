import numpy as np
from tabulate import tabulate

def runge_kutta_4(f, y0, a, b, h):
    """
    Метод Рунге-Кутты 4-го порядка для решения ДУ.
    f - функция правой части ДУ (dy/dx = f(x, y))
    y0 - начальное условие y(a) = y0
    a, b - интервал интегрирования
    h - шаг
    """
    n = int((b - a) / h)  # Количество шагов
    x = np.linspace(a, b, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0

    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return x, y

def double_counting_rk4(f, y0, a, b, epsilon):
    """
    Метод двойного пересчета с использованием метода Рунге-Кутты 4-го порядка.
    """
    h = (b - a) / 10  # Начальный шаг
    while True:
        # Решение с шагом h
        x_h, y_h = runge_kutta_4(f, y0, a, b, h)
        # Решение с шагом h/2
        x_h2, y_h2 = runge_kutta_4(f, y0, a, b, h / 2)

        # Проверка условия остановки
        max_diff = max(abs(y_h[i] - y_h2[2 * i]) for i in range(len(y_h)))
        if max_diff < 15 * epsilon:
            break

        # Уменьшаем шаг
        h /= 2

    # Коррекция решения
    y_corr = [y_h2[2 * i] - (y_h[i] - y_h2[2 * i]) / 15 for i in range(len(y_h))]

    return x_h, y_corr, h

# Пример функции для решения ДУ: dy/dx = f(x, y)
def f(x, y):
    return x + y  # Пример: dy/dx = x + y

# Параметры задачи
a = 0  # Начало интервала
b = 1  # Конец интервала
y0 = 1  # Начальное условие y(0) = 1
epsilon = 1e-5  # Требуемая точность

# Решение ДУ методом двойного пересчета
x, y_corr, final_h = double_counting_rk4(f, y0, a, b, epsilon)

# Вывод результатов в виде таблицы
data = [[f"{xi:.2f}", f"{yi:.8f}"] for xi, yi in zip(x, y_corr)]
headers = ["x", "y_corr"]
print(tabulate(data, headers=headers, tablefmt="grid"))
print(f"\nШаг h: {final_h}")