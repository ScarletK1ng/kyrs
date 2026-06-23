def find_positive_sum_and_count(arr):
    """
    Функция находит сумму положительных элементов массива
    и количество положительных элементов.
    """
    sum_pos = 0
    count_pos = 0

    for x in arr:
        if x > 0:
            sum_pos += x
            count_pos += 1

    return sum_pos, count_pos


def main():
    try:
        n = int(input("Введите размер массива N: "))

        if n <= 0:
            print("Ошибка: N должно быть положительным числом.")
            return

        arr = []

        print(f"Введите {n} элементов массива:")
        for i in range(n):
            value = int(input(f"A[{i}] = "))
            arr.append(value)

        sum_pos, count_pos = find_positive_sum_and_count(arr)

        print("Сумма положительных элементов:", sum_pos)
        print("Количество положительных элементов:", count_pos)

    except ValueError:
        print("Ошибка: необходимо вводить целые числа.")


if __name__ == "__main__":
    main()