class House:  # Создали новый класс
    numberOfFloors = 10   # Задали ему новый атрибут


house = House()

for house.numberOfFloors in range(1, 11):  # В цикле проходим по атрибуту numberOfFloors
    print('Текущий этаж равен:', house.numberOfFloors)  # Распечатываем значение "Текущий этаж равен"
