from random import choice

print("LUNAR GUIDE")
print("Добро пожаловать в справочник фаз Луны!")
print()
menu=[
    "Новолуние",
    "Растущая Луна",
    "Полнолуние",
    "Убывающая Луна",
    "Выход"
]
new_moon= [
    "НОВОЛУНИЕ"
    "Освещенность:около 0%",
    "Луна находится между Землей и Солнцем.",
    "Именно с новолуния начинается новый лунный цикл."
]
waxing_moon= [
    "РАСТУЩАЯ ЛУНА",
    "Освещенность:от 1% до почти 100%",
    "Эта фаза длится от новолуния до полнолуния. ",
]
full_moon= [
    "ПОЛНОЛУНИЕ",
    "Освещенность постепенно уменьшается.",
    "Фаза продолжается до следущего новолуния."
]
while True:
    print("\n---Доступные варианты---")
    for item in menu:
        print(f"{item}")
    choice= input("\nВыбери фазу Луны: ")
    if choice == "Выход":
        print("Программа завершена.Пока!")
        break
    elif choice == "Новолуние":
        print()
        for line in new_moon:
            print(line)
    elif choice == "Растущая Луна":
        print()
        for line in waxing_moon:
            print(line)
    elif choice =="Полнолуние":
        print()
        for line in full_moon:
            print(line)
    elif choice == "Убывающая Луна":
        print()
        for line in waxing_moon:
            print(line)
    else:
        print("Такой фазы нет. Проверь заглавные буквы!")
