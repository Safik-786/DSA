class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"  # for nice printing

people = [
    Person("John", 25),
    Person("Alice", 30),
    Person("Bob", 20)
]

# Sort by age
sorted_people = sorted(people, key=lambda p: p.age)
print(sorted_people)
# [Person(name='Bob', age=20), Person(name='John', age=25), Person(name='Alice', age=30)]


# 2. Sorting in reverse


sorted_people_desc = sorted(people, key=lambda p: p.age, reverse=True)
print(sorted_people_desc)
# [Person(name='Alice', age=30), Person(name='John', age=25), Person(name='Bob', age=20)]
