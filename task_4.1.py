class Student:

    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        student_info = print("{} {} поступил в {}г. на факультет: {}".format(self.lastname, self.name, self.year_of_entrance, self.department))


st = Student('Niiaz', 'Sharshembekov', 'Makers', '2019')
st.get_student_info()
