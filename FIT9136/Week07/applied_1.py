# defining the PhoneBook class
class PhoneBook:

    def __init__(self):
        self.contact_list = []

    def __len__(self):
        return len(self.contact_list)

    def add_entry(self, contact):
        if contact in self.contact_list:
            print("contact exist")
            return False
        else:
            self.contact_list.append(contact)
            print("contact added")
            return True

    def remove_entry(self, input_name, input_organisation):
        for each_contact_pos in range(len(self)):
            if self.contact_list[each_contact_pos].name == input_name:
                if self.contact_list[each_contact_pos].organisation == input_organisation:
                    del self.contact_list[each_contact_pos]
                    print("delete record")
                    return True
        print("record not exist")
        return False

    def search_byname(self, input_name):
        for each_contact in self.contact_list:
            if each_contact.match_name(input_name):
                print(each_contact)

    def __str__(self):
        formatted_contact = ""
        for each_contact in self.contact_list:
            formatted_contact = formatted_contact + str(each_contact) + "\n"
        return formatted_contact


from contact import ExtendedContact
# creating two ExtendedContact instances
c1 = ExtendedContact('Tom','Melbourne',['0425685212','0464545464'], "tom@gmail.com", 'Chadstone')
c2 = ExtendedContact('Jerry','Monash',['042568524'], "jerry@hotmail.com")

# Adding entry to Phonebook
phone_book = PhoneBook()
phone_book.add_entry(c1)
phone_book.add_entry(c2)
print(phone_book)

# Removing phone book entries
phone_book.remove_entry('Tom','Melbourne')
print(phone_book)

# Removing phone book entries which is not exist
phone_book.remove_entry('Aaron','Bupa')
print(phone_book)

# search by name
phone_book.search_byname('Jerry')