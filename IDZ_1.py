with open('IDZ_1.txt', 'r') as file:
    for line in file:
        numbers = line.split()  # разделение строки на отдельные слова
        for number in numbers:
            if len(number) == 2 and number.isdigit():  # проверка наличия двузначного числа
                print(line)  # вывод строки
                break  # прекращение проверки, если уже найдено двузначное число