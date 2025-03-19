import math

def f(x):
    return x**2 - 6*x

def golden_section_search(f, a, b, iterations):
    phi = (math.sqrt(5) - 1) / 2
    c = b - phi * (b - a)
    d = a + phi * (b - a)

    for _ in range(iterations):
        if f(c) < f(d):
            b = d
        else:
            a = c

        # Обновляем точки c и d
        if b - a > 1e-10:  # Проверка на малую разницу для избежания деления на ноль
            c = b - phi * (b - a)
            d = a + phi * (b - a)

        print(f"Итерация {_+1}: a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, d = {d:.6f}, f(c) = {f(c):.6f}, f(d) = {f(d):.6f}")

    return (a + b) / 2

# Параметры
a = 0
b = 5
iterations = 4

# Выполнение метода золотого сечения
result = golden_section_search(f, a, b, iterations)
print(f"Минимум найдем в x = {result:.6f}")
print(f"f(x) = {f(result):.6f}")