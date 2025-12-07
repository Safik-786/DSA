class Student:
    def __init__(self, name, score):
        self.name= name
        self.score= score

students = [
    # {"name": "Alice", "score": 88},
    # {"name": "Bob", "score": 95},
    # {"name": "Charlie", "score": 95},
    # {"name": "David", "score": 82}
    Student("Alice", 88),
    Student("Bob", 95),
    Student("Charlie", 94),
    Student("david", 82),
]
k = 2;

answer= sorted(students, key= lambda obj:( -obj.score, obj.name))

# answer = sorted(students, key=lambda obj: (-obj["score"], -ord(obj["name"][0])))

""" obj["name"][0]- Takes the first character of the student's name.
ord(character) Converts a character into its Unicode (ASCII) code point — basically a number
"""

count=0
ans=[]
for obj in answer :
    if count == 2 :
        break;
    ans.append(obj)
    count+=1
print(ans)