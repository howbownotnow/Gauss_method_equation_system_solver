# Решение систем уравнений методом Гаусса

n, m = map(int, input().split())

system = []

for i in range(n):
    system.append([int(j) for j in input().split()])

print(system)

# прямой ход метода Гаусса
for i in range(n):
    # проверка на нулевой элемент: меняем местами с последующими уравнениями
    p = i + 1
    while abs(system[i][i]) < 0.0000001:
        if p < n:
            system[i], system[p] = system[p], system[i]
            p += 1
        else:
            break
    # else:
    #     continue

    if i == 0:  # оставляем первое уравнение неизменным
        continue

    for j in range(i, n):
        coef = system[j][i - 1] / system[i - 1][i - 1]

        if abs(system[j][i - 1]) > 0.0000001:
            for k in range(m + 1):
                system[j][k] -= system[i - 1][k] * coef

print(system)

