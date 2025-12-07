# 3. Making objects sortable without passing key


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    def __lt__(self, other):
        return self.age < other.age  # now "less than" means younger


people = [
    Person("John", 25),
    Person("Alice", 30),
    Person("Bob", 20)
]

sorted_people = sorted(people)  # no key needed
print(sorted_people)
# [Person(name='Bob', age=20), Person(name='John', age=25), Person(name='Alice', age=30)]




# Sorting by multiple attributes
sorted_multi = sorted(people, key=lambda p: (p.age, p.name))
print(sorted_multi)
# Sorts by age first, then by name if ages are equal
