# Решение систем уравнений методом Гаусса

def gauss_solve(n, m):

    # прямой ход метода Гаусса
    for i in range(n):

        # проверка на обнулившиеся уравнения
        for eq in range(n - 1, -1, -1):
            # если в предыдущем уравнении обнулились сразу несколько элементов
            nonzerocount = m
            for elem in range(m):
                if abs(system[eq][elem]) < 0.0000001:
                    nonzerocount -= 1
                    if nonzerocount == 0:
                        system.pop(eq)
                        n -= 1
                else:
                    nonzero_index = elem
                # если получили уравнение типа 0 = 0
            if nonzerocount == 1 and nonzero_index == m - 1:
                return 'NO'

        # проверка на нулевой элемент: меняем местами с последующими уравнениями
        p = i + 1
        try:
            while abs(system[i][i]) < 0.0000001:
                if p < n:
                    system[i], system[p] = system[p], system[i]
                    p += 1
                else:
                    break
            # else:
            #     continue
        except IndexError:
            break


        if i == 0:  # оставляем первое уравнение неизменным
            continue

        for j in range(i, n):
            # print(i)

            if abs(system[i - 1][i - 1]) < 0.0000001:
                p = i
                while abs(system[i - 1][i - 1]) < 0.0000001:
                    if p < n:
                        system[i - 1], system[p] = system[p], system[i - 1]
                        p += 1
                    else:
                        break

            # print(system)
            coef = system[j][i - 1] / system[i - 1][i - 1]

            if abs(system[j][i - 1]) > 0.0000001:
                for k in range(m + 1):
                    system[j][k] -= system[i - 1][k] * coef

    print(system)

    # for i in range(n - 1, -1, -1):
    #     # проверка на обнулившиеся уравнения
    #     if abs(system[i][m - 1]) < 0.0000001 and abs(system[i][m]) > 0.0000001:
    #         # если получили уравнение типа 0 = а
    #         return 'NO'
    #         break

    #     elif abs(system[i][m - 1]) < 0.0000001 and abs(system[i - 1][m]) < 0.0000001:
    #         # если получили уравнение типа 0 = 0
    #         system.pop(i)
    #         n -= 1

    # проверка на обнулившиеся уравнения
    for eq in range(n - 1, -1, -1):
        # если в предыдущем уравнении обнулились сразу несколько элементов
        nonzerocount = m
        for elem in range(m):
            if abs(system[eq][elem]) < 0.0000001:
                nonzerocount -= 1
                if nonzerocount == 0:
                    system.pop(eq)
                    n -= 1
            else:
                nonzero_index = elem
            # если получили уравнение типа 0 = 0
        if nonzerocount == 1 and nonzero_index == m - 1:
            return 'NO'

    # todo: сделать проверку на бесконечное количество решений

    # обратный ход метода Гаусса

    answer = []

    for i in range(n):

        x = (system[n - i - 1][m] - sum(list(map(lambda x, y: x * y, system[n - i - 1][m - 1: m - i - 1 : -1], answer)))) / system[n - i - 1][m - i - 1] # домножать на х

        answer.append(x)

    return answer



n, m = map(int, input().split())

system = []

for i in range(n):
    system.append([int(j) for j in input().split()])

print(system)

print(gauss_solve(n, m))