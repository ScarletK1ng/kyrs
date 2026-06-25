def count_greater_than_b_and_product(arr, b):
    """
    Функция находит количество элементов массива,
    которые больше заданного числа B, и их произведение.
    """
    count = 0
    product = 1

    for x in arr:
        if x > b:
            count += 1
            product *= x

    if count == 0:
        product = 0

    return count, product


def main():
    try:
        n = int(input("Введите размер массива N: "))

        if n <= 0:
            print("Ошибка: N должно быть положительным числом.")
            return

        b = int(input("Введите число B: "))

        arr = []

        print(f"Введите {n} элементов массива:")
        for i in range(n):
            value = int(input(f"A[{i}] = "))
            arr.append(value)

        count, product = count_greater_than_b_and_product(arr, b)

        print("Количество элементов, больших B:", count)
        print("Произведение элементов, больших B:", product)

    except ValueError:
        print("Ошибка: необходимо вводить целые числа.")


if __name__ == "__main__":
    main()