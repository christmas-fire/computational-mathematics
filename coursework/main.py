import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Определение функции для системы дифференциальных уравнений
def system(t, Y):
    """
    Y[0] = y
    Y[1] = y'
    """
    y, y_prime = Y
    dydt = y_prime
    dy_prime_dt = np.exp(2 * t) + (y + y_prime) / 2 - y_prime
    return [dydt, dy_prime_dt]

# Метод Рунге-Кутта 2-го порядка
def runge_kutta_2nd_order(f, t0, y0, h, n):
    t = np.linspace(t0, t0 + n * h, n + 1)
    y = np.zeros((n + 1, len(y0)))
    y[0] = y0
    for i in range(n):
        k1 = np.array(f(t[i], y[i]))  # Производная в текущей точке
        k2 = np.array(f(t[i] + h / 2, y[i] + h / 2 * k1))  # Производная в середине шага
        y[i + 1] = y[i] + h * k2  # Обновление решения
    return t, y

# Метод Рунге-Кутта 4-го порядка
def runge_kutta_4th_order(f, t0, y0, h, n):
    t = np.linspace(t0, t0 + n * h, n + 1)
    y = np.zeros((n + 1, len(y0)))
    y[0] = y0
    for i in range(n):
        k1 = np.array(f(t[i], y[i]))  # Производная в текущей точке
        k2 = np.array(f(t[i] + h / 2, y[i] + h / 2 * k1))  # Производная в середине шага (первый раз)
        k3 = np.array(f(t[i] + h / 2, y[i] + h / 2 * k2))  # Производная в середине шага (второй раз)
        k4 = np.array(f(t[i] + h, y[i] + h * k3))  # Производная в конце шага
        y[i + 1] = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)  # Обновление решения
    return t, y

# Основная программа
if __name__ == "__main__":
    # Параметры
    t0 = 0
    tf = 1
    y0 = [1, 0]  # y(0) = 1, y'(0) = 0
    h = 0.1
    tol = 1e-6

    # Количество шагов
    n = int((tf - t0) / h)

    # Решение методом Рунге-Кутта 2-го порядка
    t_rk2, y_rk2 = runge_kutta_2nd_order(system, t0, y0, h, n)
    y_values_rk2 = y_rk2[:, 0]  # Только значения y

    # Решение методом Рунге-Кутта 4-го порядка
    t_rk4, y_rk4 = runge_kutta_4th_order(system, t0, y0, h, n)
    y_values_rk4 = y_rk4[:, 0]  # Только значения y

    # Интерполяция кубическим сплайном
    interpolation_points = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    cs_rk2 = CubicSpline(t_rk2, y_values_rk2)
    cs_rk4 = CubicSpline(t_rk4, y_values_rk4)

    # Значения сплайна в точках интерполяции
    interpolated_values_rk2 = cs_rk2(interpolation_points)
    interpolated_values_rk4 = cs_rk4(interpolation_points)

    # Вывод результатов в консоль
    print("Метод Рунге-Кутта 2-го порядка:")
    for i, point in enumerate(interpolation_points):
        print(f"x = {point:.1f}, y = {interpolated_values_rk2[i]:.6f}")

    print("\nМетод Рунге-Кутта 4-го порядка:")
    for i, point in enumerate(interpolation_points):
        print(f"x = {point:.1f}, y = {interpolated_values_rk4[i]:.6f}")

    # Графики
    plt.figure(figsize=(12, 8))

    # Решение Рунге-Кутта 2-го порядка
    plt.plot(t_rk2, y_values_rk2, label="Рунге-Кутта 2-го порядка", linestyle='-', color='blue')
    plt.scatter(interpolation_points, interpolated_values_rk2, label="Сплайн (RK2)", color='red', marker='o')

    # Решение Рунге-Кутта 4-го порядка
    plt.plot(t_rk4, y_values_rk4, label="Рунге-Кутта 4-го порядка", linestyle='--', color='green')
    plt.scatter(interpolation_points, interpolated_values_rk4, label="Сплайн (RK4)", color='orange', marker='x')

    # Настройки графика
    plt.title("Решение ДУ и интерполяция кубическим сплайном")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()