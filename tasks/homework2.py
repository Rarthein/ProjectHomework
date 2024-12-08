# Выводим приветствие
print("""Привет!
Предлагаю проверить свои знания английского!""")
user_input = input("Наберите 'ready', чтобы начать! \n")

#Списки вопрсов и ответов
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

if user_input == 'ready':
    print("\nLet's begin!")

    total_questions = 0
    correct_answers = 0

    #Задаём вопросы
    for i in range(len(questions)):
        print(questions[i])
        total_questions += 1
        user_answer = input()
        if user_answer == answers[i]:
            print("Ответ верный!\n")
            correct_answers += 1
        else:
            print(f"Неправильно. Верный ответ: {answers[i]}\n")

    # Выводим процент от правильных ответов
    answers_percent = round(correct_answers / total_questions * 100, 2)

    # Вывод правильных окончаний для слов в зависимости от числа.
    last_digit = answers_percent % 10
    if 2 <= last_digit <= 4:
        ending = "процента"
    else:
        ending = "процентов"

    # Итоговое сообщение пользователю
    print(f'''Вот и всё!
Вы ответили на {correct_answers} вопросов из {total_questions} верно, это {answers_percent} {ending}.
    ''')
else:
    print("Кажется, вы не хотите играть. Очень жаль.")
