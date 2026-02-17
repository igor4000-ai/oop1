"""
Исходя из квиза к предыдущему занятию, у нас уже есть класс
преподавателей и класс студентов (вы можете взять этот код за основу или написать свой).
Студентов пока оставим без изменения, а вот преподаватели бывают разные, поэтому теперь
класс Mentor должен стать родительским классом, а от него нужно реализовать наследование
классов Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания). Очевидно,
имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса.
А чем же будут специфичны дочерние классы? Об этом в следующих заданиях. А пока можете
проверить, что успешно реализовали дочерние классы
"""


class Student:
    """
    Класс, Класс, описывающий студента.
    """
    def __init__(self, name, surname, gender):
        """
        Инициализация объекта Student.

        Параметры:
            name (str): Имя студента.
            surname (str): Фамилия студента.
            gender (str): Пол студента.
        """
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        """
        Выставляет оценку лектору за курс.

        Параметры:
            lecturer (Lecturer): Объект лектора.
            course (str): Название курса.
            grade (int): Оценка от 1 до 10.

        Возвращает:
            str: 'Ошибка', если лектор не ведет курс или студент не изучает курс.
            None: Если оценка успешно добавлена.
        """
        if (isinstance(lecturer, Lecturer) and
                course in lecturer.courses_attached and
                course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        """
        Вычисляет среднюю оценку за домашние задания по всем курсам.

        Возвращает:
            float: Средняя оценка за все домашние задания.
        """
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        """
        Возвращает строковое представление студента.

        Возвращает:
            str: Информация о студенте в формате: имя, фамилия, средняя оценка,
                 курсы в процессе изучения и завершенные курсы.
        """
        avg = self.average_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __eq__(self, other):
        """
        Сравнение студентов по средней оценке.

        Параметры:
            other: Объект для сравнения.

        Возвращает:
            bool: True, если объекты являются студентами с равными средними оценками,
                  False в противном случае.
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        """
        Сравнение студентов по средней оценке (меньше).

        Параметры:
            other: Объект для сравнения.

        Возвращает:
            bool: True, если средняя оценка текущего студента меньше, чем у другого,
                  False в противном случае.
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        """
        Сравнение студентов по средней оценке (меньше или равно).

        Параметры:
            other: Объект для сравнения.

        Возвращает:
            bool: True, если средняя оценка текущего студента меньше или равна оценке другого,
                  False в противном случае.
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        """
        Сравнение студентов по средней оценке (больше).

        Параметры:
            other: Объект для сравнения.

        Возвращает:
            bool: True, если средняя оценка текущего студента больше, чем у другого,
                  False в противном случае.
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        """
        Сравнение студентов по средней оценке (больше или равно).

        Параметры:
            other: Объект для сравнения.

        Возвращает:
            bool: True, если средняя оценка текущего студента больше или равна оценке другого,
                  False в противном случае.
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() >= other.average_grade()


class Mentor:
    """
    Базовый класс для преподавателей.
    """
    def __init__(self, name, surname):
        """
        Инициализация объекта Mentor.

        Параметры:
            name (str): Имя преподавателя.
            surname (str): Фамилия преподавателя.
        """
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """
    Класс лектора. Наследует от Mentor и хранит оценки от студентов.
    """
    def __init__(self, name, surname):
        """
        Инициализация объекта Lecturer.

        Параметры:
            name (str): Имя лектора.
            surname (str): Фамилия лектора.
        """
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        """
        Вычисляет среднюю оценку за лекции.

        Возвращает:
            float: Средняя оценка за все лекции.
        """
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        """
        Возвращает строковое представление лектора.

        Возвращает:
            str: Информация о лекторе в формате: имя, фамилия, средняя оценка за лекции.
        """
        avg = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg}")

    def __eq__(self, other):
        """
        Сравнение лекторов по средней оценке.

        Параметры:
            other: Объект для сравнения.

        Возвращает:
            bool: True, если объекты являются лекторами с равными средними оценками,
                  False в противном случае.
        """
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        """
        Сравнение лекторов по средней оценке (меньше).

        Параметры:
            other: Объект для сравнения.

        Возвращает:
            bool: True, если средняя оценка текущего лектора меньше, чем у другого,
                  False в противном случае.
        """
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        """
        Сравнение лекторов по средней оценке (меньше или равно).

        Параметры:
            other: Объект для сравнения.

        Возвращает:
            bool: True, если средняя оценка текущего лектора меньше или равна оценке другого,
                  False в противном случае.
        """
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        """
        Сравнение лекторов по средней оценке (больше).

        Параметры:
            other: Объект для сравнения.

        Возвращает:
            bool: True, если средняя оценка текущего лектора больше, чем у другого,
                  False в противном случае.
        """
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        """
        Сравнение лекторов по средней оценке (больше или равно).

        Параметры:
            other: Объект для сравнения.

        Возвращает:
            bool: True, если средняя оценка текущего лектора больше или равна оценке другого,
                  False в противном случае.
        """
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() >= other.average_grade()


class Reviewer(Mentor):
    """
    Класс проверяющего (эксперта). Может выставлять оценки студентам за домашние задания.
    """
    def __init__(self, name, surname):
        """
        Инициализация объекта Reviewer.

        Параметры:
            name (str): Имя проверяющего.
            surname (str): Фамилия проверяющего.
        """
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """
        Выставляет оценку студенту за домашнее задание по курсу.

        Параметры:
            student (Student): Объект студента.
            course (str): Название курса.
            grade (int): Оценка от 1 до 10.

        Возвращает:
            str: 'Ошибка', если проверяющий не закреплен за курсом или студент не изучает курс.
            None: Если оценка успешно добавлена.
        """
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """
        Возвращает строковое представление проверяющего.

        Возвращает:
            str: Информация о проверяющем в формате: имя, фамилия.
        """
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


# Вспомогательные функции для подсчёта средних оценок
def average_student_grade(students, course_name):
    """
    Вычисляет среднюю оценку за домашние задания по указанному курсу для группы студентов.

    Параметры:
        students (list): Список студентов.
        course_name (str): Название курса.

    Возвращает:
        float: Средняя оценка за домашние задания по указанному курсу.
               Возвращает 0, если нет оценок по указанному курсу.
    """
    all_grades = []
    for student in students:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    return sum(all_grades) / len(all_grades) if all_grades else 0


def average_lecturer_grade(lecturers, course_name):
    """
    Вычисляет среднюю оценку за лекции по указанному курсу для группы лекторов.

    Параметры:
        lecturers (list): Список лекторов.
        course_name (str): Название курса.

    Возвращает:
        float: Средняя оценка за лекции по указанному курсу.
               Возвращает 0, если нет оценок по указанному курсу.
    """
    all_grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    return sum(all_grades) / len(all_grades) if all_grades else 0


# --- Тестирование ---
if __name__ == '__main__':
    # Создание экземпляров
    student1 = Student('Иван', 'Иванов', 'мужской')
    student1.courses_in_progress += ['Python', 'Git']
    student1.finished_courses += ['Введение в программирование']

    student2 = Student('Мария', 'Петрова', 'женский')
    student2.courses_in_progress += ['Python', 'SQL']
    student2.finished_courses += ['Основы баз данных']

    lecturer1 = Lecturer('Александр', 'Сидоров')
    lecturer1.courses_attached += ['Python', 'Git']

    lecturer2 = Lecturer('Елена', 'Козлова')
    lecturer2.courses_attached += ['Python', 'SQL']

    reviewer1 = Reviewer('Дмитрий', 'Смирнов')
    reviewer1.courses_attached += ['Python', 'Git']

    reviewer2 = Reviewer('Ольга', 'Волкова')
    reviewer2.courses_attached += ['Python', 'SQL']

    # Выставление оценок студентам (Reviewer)
    reviewer1.rate_hw(student1, 'Python', 10)
    reviewer1.rate_hw(student1, 'Python', 9)
    reviewer1.rate_hw(student1, 'Git', 8)
    reviewer1.rate_hw(student1, 'Git', 10)

    reviewer2.rate_hw(student2, 'Python', 7)
    reviewer2.rate_hw(student2, 'Python', 8)
    reviewer2.rate_hw(student2, 'SQL', 9)
    reviewer2.rate_hw(student2, 'SQL', 10)

    # Выставление оценок лекторам (Student) – используется rate_lecture
    student1.rate_lecture(lecturer1, 'Python', 9)
    student1.rate_lecture(lecturer1, 'Python', 10)
    student1.rate_lecture(lecturer1, 'Git', 8)

    student2.rate_lecture(lecturer2, 'Python', 10)
    student2.rate_lecture(lecturer2, 'Python', 9)
    student2.rate_lecture(lecturer2, 'SQL', 8)
    student2.rate_lecture(lecturer2, 'SQL', 7)

    # Демонстрация __str__
    print("Студенты:")
    print(student1)
    print()
    print(student2)
    print()

    print("Лекторы:")
    print(lecturer1)
    print()
    print(lecturer2)
    print()

    print("Ревьюеры:")
    print(reviewer1)
    print()
    print(reviewer2)
    print()

    # Сравнение студентов
    print(f"student1 == student2: {student1 == student2}")
    print(f"student1 > student2: {student1 > student2}")
    print()

    # Сравнение лекторов
    print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")
    print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
    print()

    # Вызов функций подсчёта средних оценок
    print("Средние оценки за домашние задания по курсу Python:")
    avg_python_students = average_student_grade([student1, student2], 'Python')
    print(f"Студенты: {avg_python_students}")

    print("Средние оценки за лекции по курсу Python:")
    avg_python_lecturers = average_lecturer_grade([lecturer1, lecturer2], 'Python')
    print(f"Лекторы: {avg_python_lecturers}")

    print("Средние оценки за лекции по курсу Git:")
    avg_git_lecturers = average_lecturer_grade([lecturer1, lecturer2], 'Git')
    print(f"Лекторы: {avg_git_lecturers}")