class Student:

    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    # def get_info(self):
        print('Name {} has {}, he(she) learn {}.'.format(self.name, self.age, self.subject))

Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")
print(Steve)
print(Johnny)
print(Penny)
