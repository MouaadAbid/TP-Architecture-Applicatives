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
    def __init__(self, students):
        # On trie directement par matière 1 décroissante
        self.students = sorted(students, key=lambda s: s.grade1, reverse=True)
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

    # ancienne méthode de tri pour référence (pas obligatoire maintenant)
    def rank_matter_1(self):
        return sorted(self.students, key=lambda s: s.grade1, reverse=True)

    # Implémentation de Iterable
    def __iter__(self):
        return SchoolClassIterator(self.students)


# ===== TEST =====
if __name__ == "__main__":
    school_class = SchoolClass()

    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print("=== Iteration sur les étudiants (matière 1 décroissante) ===")
    for student in school_class:
        print(student)