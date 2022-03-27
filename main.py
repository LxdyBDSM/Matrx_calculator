import numpy as np
import random as r

n = int(input("Введите количество строк n матрицы - "))
m = int(input("Введите количество столбцов m матрицы - "))
a = np.zeros((n, m))
print("Выберите вариант заполнения матрицы:")
print("1) Заполнить матрицу с клавиатуры")
print("2) Заполнить матрицу случайными числами")
choice = int(input("Ваш выбор - "))
if choice == 1:
    for i in range(0, n):
        for j in range(0, m):
            a[i][j] = int(input("Введите элемент матрицы - "))
else:
    for i in range(0, n):
        for j in range(0, m):
            a[i][j] = r.randint(1, 10)

print("Заполненная матрица:")
for i in range(0, n):
    for j in range(0, m):
        print(int(a[i][j]), end=" ")
    print()

print("Список команд:")
print("1) Сложение двух матриц")
print("2) Вычитание двух матриц")
print("3) Умножение двух матриц")
print("4) Умножение матрицы на число")
print("5) Транспонирование матрицы")
print("6) Нахождение определителя матрицы")
print("7) Нахождение обратной матрицы")
print("8) Нахождение ранга матрицы")
print("9) Список команд")
print("0) Закончить работу")
action = 50

while action != 0:
    action = int(input("Выберите команду - "))

    if action == 1:
        print("Выбрана операция сложения матриц")
        n2 = int(input("Введите количество строк n второй матрицы - "))
        m2 = int(input("Введите количество столбцов m второй матрицы - "))
        b = np.zeros((n2, m2))
        print("Выберите вариант заполнения матрицы:")
        print("1) Заполнить матрицу с клавиатуры")
        print("2) Заполнить матрицу случайными числами")
        choice = int(input("Ваш выбор - "))
        if choice == 1:
            for i in range(0, n2):
                for j in range(0, m2):
                    b[i][j] = int(input("Введите элемент матрицы - "))
        else:
            for i in range(0, n2):
                for j in range(0, m2):
                    b[i][j] = r.randint(1, 10)

        print("Вторая матрица:")
        for i in range(0, n2):
            for j in range(0, m2):
                print(int(b[i][j]), end=" ")
            print()

        print("Результат:")
        c = a + b
        print(c)

    elif action == 2:
        print("Выбрана операция вычитания матриц")
        n2 = int(input("Введите количество строк n второй матрицы - "))
        m2 = int(input("Введите количество столбцов m второй матрицы - "))
        b = np.zeros((n2, m2))
        print("Выберите вариант заполнения матрицы:")
        print("1) Заполнить матрицу с клавиатуры")
        print("2) Заполнить матрицу случайными числами")
        choice = int(input("Ваш выбор - "))
        if choice == 1:
            for i in range(0, n2):
                for j in range(0, m2):
                    b[i][j] = int(input("Введите элемент матрицы - "))
        else:
            for i in range(0, n2):
                for j in range(0, m2):
                    b[i][j] = r.randint(1, 10)

        print("Вторая матрица:")
        for i in range(0, n2):
            for j in range(0, m2):
                print(int(b[i][j]), end=" ")
            print()

        print("Выберите порядок вычитания:")
        print("1) Вычитание из первой матрицы второй")
        print("2) Вычитание из второй матрицы первой")
        counter = int(input("Ваш выбор - "))
        if counter == 1:
            c = a - b
            print(c)
        else:
            c = b - a
            print(c)

    elif action == 3:

        print("Выбрана операция умножения матриц")
        n2 = int(input("Введите количество строк n второй матрицы - "))
        m2 = int(input("Введите количество столбцов m второй матрицы - "))
        b = np.zeros((n2, m2))
        print("Выберите вариант заполнения матрицы:")
        print("1) Заполнить матрицу с клавиатуры")
        print("2) Заполнить матрицу случайными числами")
        choice = int(input("Ваш выбор - "))
        if choice == 1:
            for i in range(0, n2):
                for j in range(0, m2):
                    b[i][j] = int(input("Введите элемент матрицы - "))
        else:
            for i in range(0, n2):
                for j in range(0, m2):
                    b[i][j] = r.randint(1, 10)
        print("Вторая матрица:")
        for i in range(0, n2):
            for j in range(0, m2):
                print(int(b[i][j]), end=" ")
            print()

        print("Выберите в какой последовательности умножить матрицы:")
        print("1) Умножить первую матрицу на вторую")
        print("2) Умножить вторую матрицу на первую")
        move = int(input("Ваш выбор - "))
        if move == 1:
            if n == m2:
                print("Результат:")
                c = a.dot(b)
                print(c)
                action = int(input("Выберите команду - "))
            else:
                print("Данная операция не может быть выполнена")
        else:
            if n2 == m:
                print("Результат:")
                c = b.dot(a)
                print(c)
                action = int(input("Выберите команду - "))
            else:
                print("Данная операция не может быть выполнена")

    elif action == 4:
        print("Выбрана операция умножения матрицы на число")
        numb = int(input("Введите число на которое нужно умножить матрицу - "))
        c = np.zeros((n, m))
        for i in range(0, n):
            for j in range(0, m):
                c[i][j] = a[i][j] * numb

        print("Умноженная матрица:")
        for i in range(0, n):
            for j in range(0, m):
                print(int(c[i][j]), end=" ")
            print()

    elif action == 5:
        print("Выбрана операция транспонирования матрицы")
        print("Транспонированная матрица:")
        print(a.transpose())

    elif action == 6:
        print("Выбрана операция поиска определителя матрицы")
        print("Определитель матрицы - ", int(np.linalg.det(a)))

    elif action == 7:
        print("Выбрана операция поиска обратной матрицы")
        print("Обратная матрицы - \n", np.linalg.inv(a))

    elif action == 8:
        print("Выбрана операция поиска ранга матрицы")
        print("Ранг матрицы - ", int(np.linalg.matrix_rank(a)))

    elif action == 9:
        print("Список команд:")
        print("1) Сложение двух матриц")
        print("2) Вычитание двух матриц")
        print("3) Умножение двух матриц")
        print("4) Умножение матрицы на число")
        print("5) Транспонирование матрицы")
        print("6) Нахождение определителя матрицы")
        print("7) Нахождение обратной матрицы")
        print("8) Нахождение ранга матрицы")
        print("9) Список команд")
        print("0) Закончить работу")

    elif action == 0:
        print("Завершение работы...")
