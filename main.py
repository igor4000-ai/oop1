"""Исходя из квиза к предыдущему занятию, у нас уже есть класс
преподавателей и класс студентов (вы можете взять этот код за основу или написать свой).
Студентов пока оставим без изменения, а вот преподаватели бывают разные, поэтому теперь
класс Mentor должен стать родительским классом, а от него нужно реализовать наследование
классов Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания). Очевидно,
имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса.
А чем же будут специфичны дочерние классы? Об этом в следующих заданиях. А пока можете
проверить, что успешно реализовали дочерние классы
"""


class Student:
    """Класс, описывающий студента.

    Атрибуты:
        name (str): Имя студента.
        surname (str): Фамилия студента.
        gender (str): Пол студента.
        finished_courses (list): Список завершенных курсов.
        courses_in_progress (list): Список курсов в процессе изучения.
        grades (dict): Словарь с оценками за домашние задания.
    """

    def __init__(self, name, surname, gender):
        """Инициализация объекта Student.

        Args:
            name (str): Имя студента.
            surname (str): Фамилия студента.
            gender (str): Пол студента.

        Note:
            При инициализации создаются следующие атрибуты:
            - finished_courses: Список завершенных курсов (по умолчанию содержит "Введение в программирование").
            - courses_in_progress: Пустой список курсов в процессе изучения.
            - grades: Пустой словарь для хранения оценок за домашние задания.
        """
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['Введение в программирование']
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        """Оценить лекцию лектора.

        Args:
            lecturer (Lecturer): Объект лектора.
            course (str): Название курса.
            grade (int): Оценка от 1 до 10.

        Returns:
            str: 'Ошибка', если лектор не ведет курс или студент не изучает курс.
            None: Если оценка успешно добавлена.
        """
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_hw(self):
        """Вычислить среднюю оценку за домашние задания.

        Returns:
            float: Средняя оценка за все домашние задания.
        """
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return total / count if count else 0

    def __str__(self):
        """Возвращает строковое представление студента.

        Returns:
            str: Информация о студенте в формате: имя, фамилия, средняя оценка,
                 курсы в процессе изучения и завершенные курсы.
        """
        return (
            f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_average_hw()}"
            f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}")


class Mentor:
    """Родительский класс для преподавателей.

    Атрибуты:
        name (str): Имя преподавателя.
        surname (str): Фамилия преподавателя.
        courses_attached (list): Список закрепленных курсов.
    """

    def __init__(self, name, surname):
        """Инициализация объекта Mentor.

        Args:
            name (str): Имя преподавателя.
            surname (str): Фамилия преподавателя.

        Note:
            При инициализации создается следующий атрибут:
            - courses_attached: Пустой список закрепленных курсов.
        """
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс лектора, наследуемый от класса Mentor.

    Атрибуты:
        name (str): Имя лектора.
        surname (str): Фамилия лектора.
        courses_attached (list): Список закрепленных курсов.
        grades (dict): Словарь с оценками за лекции.
    """

    def __init__(self, name, surname):
        """Инициализация объекта Lecturer.

        Args:
            name (str): Имя лектора.
            surname (str): Фамилия лектора.

        Note:
            При инициализации создается следующий атрибут:
            - grades: Пустой словарь для хранения оценок за лекции.
        """
        super().__init__(name, surname)
        self.grades = {}

    def get_lecture_average(self):
        """Вычислить среднюю оценку за лекции.

        Returns:
            float: Средняя оценка за все лекции.
        """
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return total / count if count else 0

    def comparison(self, student):
        """Сравнить среднюю оценку лектора со средней оценкой студента.

        Args:
            student (Student): Объект студента для сравнения.

        Returns:
            str: 'Лектор лучше', если средняя оценка лектора выше.
                 'Студент лучше', если средняя оценка студента выше.
                 'Равные результаты', если оценки равны.
        """
        if self.get_lecture_average() > student.get_average_hw():
            return 'Лектор лучше'
        elif self.get_lecture_average() < student.get_average_hw():
            return 'Студент лучше'
        else:
            return 'Равные результаты'

    def __str__(self):
        """Возвращает строковое представление лектора.

        Returns:
            str: Информация о лекторе в формате: имя, фамилия, средняя оценка за лекции.
        """
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_lecture_average()}"


class Reviewer(Mentor):
    """Класс эксперта, проверяющего домашние задания, наследуемый от класса Mentor.

    Атрибуты:
        name (str): Имя эксперта.
        surname (str): Фамилия эксперта.
        courses_attached (list): Список закрепленных курсов.
    """

    def __init__(self, name, surname):
        """Инициализация объекта Reviewer.

        Args:
            name (str): Имя эксперта.
            surname (str): Фамилия эксперта.

        Note:
            При инициализации наследуются все атрибуты от родительского класса Mentor,
            включая courses_attached для хранения списка закрепленных курсов.
        """
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Оценить домашнее задание студента.

        Args:
            student (Student): Объект студента.
            course (str): Название курса.
            grade (int): Оценка от 1 до 10.

        Returns:
            str: 'Ошибка', если эксперт не закреплен за курсом или студент не изучает курс.
            None: Если оценка успешно добавлена.
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Возвращает строковое представление эксперта.

        Returns:
            str: Информация об эксперте в формате: имя, фамилия.
        """
        return f"Имя: {self.name}\nФамилия: {self.surname}"


""" Задание 1 """

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor))  # True
print(isinstance(reviewer, Mentor))  # True
print(lecturer.courses_attached)  # []
print(reviewer.courses_attached)  # []

""" Задание 2 """

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Ольга', 'Алёхина', 'Ж')

lecturer_1 = Lecturer('Иосиф', 'Иванов')
reviewer_1 = Reviewer('Панкрат', 'Петров')
student_1 = Student('Алина', 'Игнатова', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

student_1.courses_in_progress += ['Python', 'C++']
lecturer_1.courses_attached += ['Python', 'C++']
reviewer_1.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

print(lecturer.grades)  # {'Python': [7]}

print(student.rate_lecture(lecturer_1, 'Python', 6))  # None
print(student.rate_lecture(lecturer_1, 'Java', 2))  # Ошибка
print(student.rate_lecture(lecturer_1, 'С++', 1))  # Ошибка
print(student.rate_lecture(reviewer_1, 'Python', 2))  # Ошибка

print(reviewer.rate_hw(student, 'Python', 8))
print(reviewer_1.rate_hw(student_1, 'Python', 4))

""" Задание 3 """

print(reviewer)
print(lecturer)
print(student)

print(reviewer_1)
print(lecturer_1)
print(student_1)

print(Lecturer.comparison(lecturer, student))
print(Lecturer.comparison(lecturer_1, student_1))