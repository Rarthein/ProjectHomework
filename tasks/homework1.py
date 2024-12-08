# Выводим приветствие и просим ввести имя
user_name = input("""Привет! Предлагаю проверить свои знания английского!
Напиши, как тебя зовут: """)

print(f"\nПривет, {user_name}, начинаем тренировку!\n")

# Задаём необходимые переменные.
total_questions = 3
answers_counter = 0
scores_counter = 0

# Задаём вопросы
print("My name ___ Vova. ")
answer_1 = input()
if answer_1 == "is":
    answers_counter += 1
    scores_counter += 10
    print("""Ответ верный!
Вы получаете 10 баллов!\n""")
else:
    print("""Неправильно.
Правильный ответ 'is'\n""")

print("I ___ a coder. ")
answer_2 = input()
if answer_2 == "am":
    answers_counter += 1
    scores_counter += 10
    print("""Ответ верный!
Вы получаете 10 баллов!\n""")
else:
    print("""Неправильно.
Правильный ответ 'am'\n""")

print("I live ___ Moscow. ")
answer_3 = input()
if answer_3 == "in":
    answers_counter += 1
    scores_counter += 10
    print("""Ответ верный!
Вы получаете 10 баллов!\n""")
else:
    print("""Неправильно.
Правильный ответ 'in'\n""")

# Выводим процент от правильных ответов
answers_percent = round(answers_counter / total_questions * 100, 2)

# Вывод правильных окончаний для слов в зависимости от числа. В задании нет, но чтобы и в глаза не бросалось.
last_digit1 = answers_counter % 10
if last_digit1 == 1:
    ending_1 = "вопрос"
elif 2 <= last_digit1 <= 4:
    ending_1 = "вопроса"
else:
    ending_1 = "вопросов"

last_digit2 = answers_percent % 10
if 2 <= last_digit2 <= 4:
    ending_2 = "процента"
else:
    ending_2 = "процентов"

# Итоговое сообщение пользователю
print(f"""Вот и всё, {user_name}!
Вы ответили на {answers_counter} {ending_1} из 3 верно.\n""")
print(f"""Вы заработали {scores_counter} баллов.
Это {answers_percent} {ending_2}.""")
