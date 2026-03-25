from collections.abc import Iterable, Iterator

class Student:
    def __init__(self, name, grade1, grade2, grade3):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def average(self):
        return (self.grade1 + self.grade2 + self.grade3) / 3

    def __repr__(self):
        return f"{self.name} - Notes: ({self.grade1}, {self.grade2}, {self.grade3}) - Moyenne: {self.average():.2f}"


class SchoolClassIterator(Iterator):
    def __init__(self, students, subject):
        self.subject = subject  # 1, 2 ou 3
        # On trie dynamiquement selon la matière
        if subject == 1:
            self.students = sorted(students, key=lambda s: s.grade1, reverse=True)
        elif subject == 2:
            self.students = sorted(students, key=lambda s: s.grade2, reverse=True)
        elif subject == 3:
            self.students = sorted(students, key=lambda s: s.grade3, reverse=True)
        else:
            raise ValueError("Matière invalide")
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    # on garde les anciennes méthodes si besoin
    def rank_matter_1(self):
        return sorted(self.students, key=lambda s: s.grade1, reverse=True)

    # Implémentation de Iterable pour matière 1 par défaut
    def __iter__(self):
        return SchoolClassIterator(self.students, subject=1)

    # Nouveaux itérateurs pour matière 2 et 3
    def iter_matter_2(self):
        return SchoolClassIterator(self.students, subject=2)

    def iter_matter_3(self):
        return SchoolClassIterator(self.students, subject=3)


# ===== TEST =====
if __name__ == "__main__":
    school_class = SchoolClass()

    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print("=== Iteration matière 1 (par défaut) ===")
    for student in school_class:
        print(student)

    print("\n=== Iteration matière 2 ===")
    for student in school_class.iter_matter_2():
        print(student)

    print("\n=== Iteration matière 3 ===")
    for student in school_class.iter_matter_3():
        print(student)