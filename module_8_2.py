


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for i in numbers:
            try:
                result += i
            except TypeError:
                incorrect_data += 1
                print(f"Некорректный тип данных для подсчёта суммы {i}")
    except:
        print("В numbers записан некорректный тип данных")
    a = (result, incorrect_data)
    return a

def calculate_average(numbers):
    kol = []
    try:
        for i in numbers:
            if type(i) == int:
                kol.append(i)
    except TypeError:
            print("В numbers записан некорректный тип данных")
            
    try:
        average = personal_sum(numbers)[0] / len(kol)
    except ZeroDivisionError:
        average = 0
    return average

# print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
# print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
# print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

