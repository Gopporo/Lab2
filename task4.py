#Напишите программу, демонстрирующую работу try\except\finally

def obrabotka_isklucheniy():
    try:
        x = float(input("Введите делимое: "))
        y = float(input("Введите делитель: "))
        return x / y
    except ZeroDivisionError:
        return "Деление на ноль нвозможно"
    except ValueError:
        return "Ввод не является числом"
    finally:
        print("Завершение работы функции obrabotka_isklucheniy()")

print(obrabotka_isklucheniy())