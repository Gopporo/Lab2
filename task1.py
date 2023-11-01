# Написать функцию is_prime, принимающую 1 аргумент — число от 0
# до 1000, и возвращающую True, если оно простое, и False - иначе.

try:
    n = int(input("Введите число от 0 до 1000: "))
except ValueError:
    print("Ввод не является числом. Введите положительное число от 0 до 1000.")
    exit()

def is_prime(n):
    if n <= 0:
        print("Введеное число равно 0 или меньше и не является простым")
        return False

    if n == 1:
        print("Число 1 не является простым")
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    print("Введеное число является простым")
    return True

print(is_prime(n))