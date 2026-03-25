from collections.abc import Iterable, Iterator

# ===== Décorateur pour ajouter grade4 =====
def add_subject4(default_grade=15):
    def decorator(cls):
        original_init = cls.__init__
        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            self.grade4 = default_grade
        cls.__init__ = new_init
        return cls
    return decorator

# ===== Classe Student décorée =====
@add_subject4(default_grade=15)
class Student:
    def __init__(self, name, grade1, grade2, grade3):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def average(self):
        return (self.grade1 + self.grade2 + self.grade3 + self.grade4) / 4

    def __repr__(self):
        return f"{self.name} - Notes: ({self.grade1}, {self.grade2}, {self.grade3}, {self.grade4}) - Moyenne: {self.average():.2f}"


# ===== Itérateur générique =====
class SchoolClassIterator(Iterator):
    def __init__(self, students, subject):
        self.subject = subject
        if subject == 1:
            self.students = sorted(students, key=lambda s: s.grade1, reverse=True)
        elif subject == 2:
            self.students = sorted(students, key=lambda s: s.grade2, reverse=True)
        elif subject == 3:
            self.students = sorted(students, key=lambda s: s.grade3, reverse=True)
        elif subject == 4:
            self.students = sorted(students, key=lambda s: s.grade4, reverse=True)
        else:
            raise ValueError("Matière invalide")
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


# ===== Métaclasse Singleton =====
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# ===== SchoolClass Singleton =====
class SchoolClass(Iterable, metaclass=SingletonMeta):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return SchoolClassIterator(self.students, subject=1)

    def iter_matter_2(self):
        return SchoolClassIterator(self.students, subject=2)

    def iter_matter_3(self):
        return SchoolClassIterator(self.students, subject=3)

    def iter_matter_4(self):
        return SchoolClassIterator(self.students, subject=4)


# ===== TEST =====
if __name__ == "__main__":
    # Création de deux instances
    class1 = SchoolClass()
    class2 = SchoolClass()

    # Vérification que ce sont bien la même instance
    print(f"class1 is class2 ? {class1 is class2}")

    # Ajouter des étudiants via class1
    class1.add_student(Student('J', 10, 12, 13))
    class1.add_student(Student('A', 8, 2, 17))
    class1.add_student(Student('V', 9, 14, 14))

    print("\n=== Iteration matière 4 (Singleton) ===")
    for student in class2.iter_matter_4():  # on utilise class2, même instance
        print(student)