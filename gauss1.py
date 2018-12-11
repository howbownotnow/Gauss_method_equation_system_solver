# Решение систем уравнений методом Гаусса


def gauss_solve(n, m):
    # n - количество уравнений
    # m - количество неизвестных
    # прямой ход метода Гаусса
    for i in range(n):

        # проверка на обнулившиеся уравнения типа 0 = 0 или 0 = a
        for eq in range(n - 1, -1, -1):
            # если в предыдущем уравнении обнулились сразу несколько элементов
            nonzerocount = m + 1
            for elem in range(m + 1):
                if abs(system[eq][elem]) < 0.0000001:
                    nonzerocount -= 1
                    if nonzerocount == 0:
                        # если получили уравнение типа 0 = 0
                        system.pop(eq)
                        n -= 1
                else:
                    nonzero_index = elem
            # если получили уравнение типа 0 = a
            if nonzerocount == 1 and nonzero_index == m:
                return 'NO'

        # проверка на нулевой множитель: меняем местами с последующими уравнениями
        p = i + 1  # индекс уравнения, с которым будем менять местами текущее
        try:
            while abs(system[i][i]) < 0.0000001:
                if p < n:
                    system[i], system[p] = system[p], system[i]
                    p += 1
                else:
                    break
        except IndexError:
            break

        if i == 0:  # оставляем первое уравнение системы неизменным
            continue

        for j in range(i, n):

            if abs(system[i - 1][i - 1]) < 0.0000001:  # аналог a = 0 для float
                p = i
                while abs(system[i - 1][i - 1]) < 0.0000001:
                    if p < n:
                        system[i - 1], system[p] = system[p], system[i - 1]
                        p += 1
                    else:
                        break

            coef = system[j][i - 1] / system[i - 1][i - 1]

            if abs(system[j][i - 1]) > 0.0000001:
                for k in range(m + 1):
                    system[j][k] -= system[i - 1][k] * coef

    # проверка на обнулившиеся уравнения
    # проверяем с конца системы
    for eq in range(n - 1, -1, -1):
        # если в предыдущем уравнении обнулились сразу несколько элементов
        nonzerocount = m + 1
        for elem in range(m + 1):
            if abs(system[eq][elem]) < 0.0000001:
                nonzerocount -= 1
                if nonzerocount == 0:
                    # если получили уравнение типа 0 = 0
                    system.pop(eq)
                    n -= 1
            else:
                nonzero_index = elem
            # если получили уравнение типа 0 = a
        if nonzerocount == 1 and nonzero_index == m:
            return 'NO'

    if n < m:
        return 'INF'

    # обратный ход метода Гаусса

    answer = []

    for i in range(n):

        x = (system[n - i - 1][m] - sum(list(map(lambda x, y: x * y, system[n - i - 1][m - 1 : m - i - 1 : -1], answer)))) / system[n - i - 1][m - i - 1]

        answer.append(x)

    answer.reverse()

    str_answer = list(map(str, answer))

    return f"YES\n{' '.join(str_answer)}"

n, m = map(int, input().split())

system = []

for i in range(n):
    system.append([int(j) for j in input().split()])

print(gauss_solve(n, m))