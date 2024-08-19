# Программа для измерения мощности компьютерного процессора / The program, which can check streight computer's processor

import time

def program_in_russian_language():
    """Русский язык программы."""
    user_number = int(input("Введите Ваше конечное число: "))

    start_count = 0

    print("Подождите, пожалуйста, идёт счёт..")

    # Основная программа (основной цикл)
    while True:
        start_count += 1
        if start_count == user_number:
            print(f"Счёт окончен. Время, затраченное на выполнение этого действия: {time.process_time()}.")
            print("Программа завершена. Нажмите 'Enter', чтобы выйти из неё.")
            break

def program_in_english_language():
    """Program in english language."""
    user_number = int(input("Type your the last number: "))

    start_count = 0

    print("Please, wait, it is counting..")

    while True:
        start_count += 1
        if start_count == user_number:
            print(f"The count is finished. Time, which was used on it: {time.process_time()}.")
            print("The program is finihed. Press 'Enter' to exit.")
            break



# Выбор языка и запуск программы. / Choice of language and program's start
choose_user_language = input("""Здравствуйте! Выберите Ваш язык (напишите число Вашего языка). / Hello! Please, choose your language (type number of your language). 
Список доступных языков (и их цифр). / The list of avalable languages (and it's numbers): 1 - русский, 2 - english: """)

if choose_user_language == '1':
    program_in_russian_language()
if choose_user_language == '2':
    program_in_english_language()


# Завершение и цикл программы после основного / The program's finish and loop it after main
input()

