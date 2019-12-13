class List():

    def __init__(self, *args):
        self.all_contacts = ['Aijan', 'Burul', 'Asel', 'Aziza', 'Aijarkin', 'Nuriza', 'Adelina', 'Aikumush']
        self.all_contacts1 = []
    def search_by_name(self, all_contacts1):
        for x in self.all_contacts:
            if x in all_contacts1:
                self.all_contacts1.append(x)

        print(self.all_contacts1)

class ContactList(List):

    pass

my_list = ContactList("")
my_list.search_by_name(['Aigerim', 'Adelina', 'Aziza'])
