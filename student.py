class Student:
    name = ''
    group = ''
    age = 0
    grades = []
    gpa = 0
class Student:
    def __init__(self, name, group, age, grades):
        self.name = name
        self.group = group
        self.age = age
        self.grades = grades
        self.gpa = round(sum(self.grades) / len(grades), 2)

    def show_info(self):
        print(f'{self.name} ({self.age} років), група {self.group}')
        print(f'Середній бал: {self.gpa} ({self.grades})')

student1 = Student(name='Dave', group='B2121', age=14, grades=[8, 7, 9, 10, 8, 8, 6])
# student2 = Student()
# student2.name = 'John'
# student2.group = 'B2121'
# student2.age = 15
# student2.grades = [6, 6, 5, 7, 6, 6, 8]

student1.show_info()
# student2.show_info()