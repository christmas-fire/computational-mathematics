import math

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    return integral * h

def simpson_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Number of intervals must be even for Simpson's rule.")
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * f(a + i * h)
        else:
            integral += 4 * f(a + i * h)
    return integral * h / 3

def double_counting_trapezoidal(f, a, b, epsilon):
    n = 1
    while True:
        Ih = trapezoidal_rule(f, a, b, n)
        I_h2 = trapezoidal_rule(f, a, b, 2 * n)
        if abs(Ih - I_h2) < 3 * epsilon:
            break
        n *= 2
    I_corr = I_h2 - (Ih - I_h2) / 3
    return I_corr, n

def double_counting_simpson(f, a, b, epsilon):
    n = 2
    while True:
        Ih = simpson_rule(f, a, b, n)
        I_h2 = simpson_rule(f, a, b, 2 * n)
        if abs(Ih - I_h2) < 15 * epsilon:
            break
        n *= 2
    I_corr = I_h2 - (Ih - I_h2) / 15
    return I_corr, n

# Функции для интегрирования
def f(x):
    return 1 / x

# Параметры интегрирования
a = int(input("Введите параметр a: "))
b = int(input("Введите параметр b: "))
epsilon = 1e-5

# Интегрирование методом трапеций с двойным пересчетом
print()
result_trapezoidal, n_trapezoidal = double_counting_trapezoidal(f, a, b, epsilon)
print(f"Результат методом трапеций с двойным пересчетом: {result_trapezoidal}")
print(f"Количество интервалов для метода трапеций: {n_trapezoidal}")

# Интегрирование методом Симпсона с двойным пересчетом
print()
result_simpson, n_simpson = double_counting_simpson(f, a, b, epsilon)
print(f"Результат методом Симпсона с двойным пересчетом: {result_simpson}")
print(f"Количество интервалов для метода Симпсона: {n_simpson}")