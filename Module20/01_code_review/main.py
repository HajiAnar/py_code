def get_interests_and_surname_length(students_dict):
    interests = set()
    surnames = [student['surname'] for student in students_dict.values()]
    surname_length = sum(len(surname) for surname in surnames)


    for student in students_dict.values():
        interests.update(student['interests'])
    return interests, surname_length


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

id_pairs = [(id, student['age']) for id, student in students.items()]
interests, surname_length = get_interests_and_surname_length(students)

print("Список пар \"ID студента — возраст\":", id_pairs)
print("Полный список интересов всех студентов:", interests)
print("Общая длина всех фамилий студентов:", surname_length)

