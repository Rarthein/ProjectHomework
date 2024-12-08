#создаём словари с разными уровнями сложности
words_easy = {
    "family":"семья",
    "hand" : "рука",
    "people" : "люди",
    "evening" : "вечер",
    "minute" : "минута",
}

words_medium = {
    "believe" : "верить",
    "feel" : "чувствовать",
    "make" : "делать",
    "open" : "открывать",
    "think" : "думать",
}

words_hard = {
    "rural" : "деревенский",
    "fortune" : "удача",
    "exercise" : "упражнение",
    "suggest" : "предлагать",
    "except" : "кроме",
}

#словарь с уровнями рангов по итогу теста
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

words = {}

def choose_difficulty():
    """Запрашивает уровень сложности и возвращает словарь из соотвествующих слов после ввода"""
    difficulty = input("""\nВыберете уровень сложности:
легкий, средний, сложный.\n""").lower()

    if difficulty == "легкий":
        words_level = words_easy
    elif difficulty == "средний":
        words_level = words_medium
    elif difficulty == "сложный":
        words_level = words_hard
    else:
        words_level = words_medium
    return words_level

words = choose_difficulty()
print("\nВыбран уровень сложности. Мы предложим 5 слов, подберите перевод:\n")


def play_game(words_guess):
    """Принимает словарь с нужными словами. Запускает угадывание перевода слов и возвращает словарь с ответами"""
    answers = {}

    for eng_word, translation in words_guess.items():
        print(f"{eng_word}, {len(translation)} букв, начинается на {translation[0]}...")

        user_answer = input().lower()

        if user_answer == translation:
            print(f"\nВерно. {eng_word.capitalize()} - это {translation}\n")
            answers[eng_word] = True
        else:
            print(f"\nНеверно. {eng_word.capitalize()} - это {translation}\n")
            answers[eng_word] = False
    return answers

user_answers = play_game(words)



def display_results(user_results):
    """Принимает словарь с ответами и выводит правильные и неправильные слова"""
    correct_answers = []
    incorrect_answers = []

    for answer, translation in user_results.items():
        if translation == True:
            correct_answers.append(answer)
        else:
            incorrect_answers.append(answer)

    if correct_answers:
        print("\nПравильно отвечены слова:\n"+"\n".join(correct_answers))
    if incorrect_answers:
        print(f"\nНеправильно отвечены слова:\n"+"\n".join(incorrect_answers))

results = display_results(user_answers)


def calculate_rank(user_answers):
    """Принимает словарь с ответами и возвращает ранг пользователя на их основании"""
    correct_answer_count = 0

    for translation in user_answers.values():
        if translation == True:
            correct_answer_count += 1
        else:
            continue

    user_rank = levels[correct_answer_count]
    return user_rank

user_rank = calculate_rank(user_answers)
print("\nВаш ранг:\n" + user_rank)
