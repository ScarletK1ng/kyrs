import random

nums = []

while True:
    choose = int(input("Введите 0 для остановки или любое другое число для генерации: "))

    if choose == 0:
        break

    number = random.randint(1, 100)
    nums.append(number)

print("Сгенерированные числа, кроме последнего:")

if len(nums) > 1:
    print(nums[:-1])
else:
    print("Нет чисел для вывода")