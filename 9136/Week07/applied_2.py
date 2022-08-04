import math
from applied_1 import PhoneBook
# defining the PasscodePhoneBook class inherited from PhoneBook class
class ExtendedPhoneBook(PhoneBook):
    def __init__(self, passcode):
        self.passcode = passcode
        super().__init__()

    def validate_passcode(self):
        user_input = input("enter passcode")
        if user_input == self.passcode :
            return True
        else:
            return False

    def remove_entry(self, input_name, input_organisation):
        if self.validate_passcode == True:
            return super().remove_entry(input_name, input_organisation)
        else:
            return False

    def search_byname(self, input_name):
        if self.validate_passcode():
            return super().search_byname(input_name)

    def __str__(self):
        if self.validate_passcode():
            return super().__str__()
        else:
            return False






from contact import ExtendedContact
# creating two Contact instances
c1 = ExtendedContact('Tom','Melbourne',['0425685212','0464545464'], "tom@gmail.com", 'MELBOURNE')
c2 = ExtendedContact('Jerry','Monash',['042568524'], "jerry@hotmail.com", 'GEELONG')
c3 = ExtendedContact('Terry','Monash',['042532524'], "teerry@hotmail.com", 'CASTLEMAINE')
c4 = ExtendedContact('John','Monash Health',['042577524'], "johnmh@hotmail.com", 'FAWKNER')
c5 = ExtendedContact('Tommy','Monash Health',['046457524'], "mh_tommy@hotmail.com", 'HEALESVILLE')


print("Adding entry to Phonebook\n")
# Adding entry to Phonebook
pass_phone_book = ExtendedPhoneBook('1234567')
pass_phone_book.add_entry(c1)
pass_phone_book.add_entry(c2)
pass_phone_book.add_entry(c3)
pass_phone_book.add_entry(c4)
pass_phone_book.add_entry(c5)
print(pass_phone_book)

print("Removing phone book entries\n")
# Removing phone book entries
pass_phone_book.remove_entry('Tom','Melbourne')
print(pass_phone_book)

print("Removing phone book entries which is not exist\n")
# Removing phone book entries which is not exist
pass_phone_book.remove_entry('Aaron','Bupa')
print(pass_phone_book)

print("search by name\n")
# search by name
pass_phone_book.search_byname('Jerry')