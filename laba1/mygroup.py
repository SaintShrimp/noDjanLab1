groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Петр",
        "surname": "Александров",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 3, 5]
    },
    {
        "name": "Ивана",
        "surname": "Петрова",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Мифодевич",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [3, 5, 3]
    }
]
a = int(input('Enter average '))

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(15), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        if (sum(student['marks']) / len(student['marks'])) >= a:
            print(student["name"].ljust(15), student["surname"].ljust(15), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

print_students(groupmates)


