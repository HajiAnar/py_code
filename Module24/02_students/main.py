class Student:
    def __init__(self, full_name, group, progress):
        self.full_name = full_name
        self.group = group
        self.progress = progress
    def gpa(self):
        gpa_scores = sum(self.progress) / len(self.progress)
        return gpa_scores

    def __str__(self):
        return f'{self.full_name} {self.group}'

students = []
for i_student in range(10):
    print(f'Студент {i_student +1}:')
    full_name = input('Введите фамилию и имя: ')
    group = int(input('Введите номер группы: '))
    progress = list(map(int, input('Введите оценки через пробел: ').split()))
    students.append(Student(full_name, group, progress))

gpa_sorted = sorted(students, key=lambda student: student.gpa())
print(*gpa_sorted, sep='\n')
