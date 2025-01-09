def names():
    all_names = []

    def inner(name):
        all_names.append(name)
        return all_names

    return inner

if __name__ == '__main__':
    students = names()
    print(students('Vasya'))
    print(students('Petya'))
    print(students('Dima'))