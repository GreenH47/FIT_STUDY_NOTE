import random


class User:
    """
    3.1.1 constructor A user must have id(int, default value -1),
    username(str, default value “”),password(str, default value “”).
    """

    def __init__(self, _id=-1, username="", password=""):
        self._id = str(_id)
        self.username = username
        self.password = password

    """
    3.1.2 generate_unique_user_id()This method checks the files 
    user_admin.txt, user_instructor.txt and user_student.txt
    to generate an unique user id. The return result is a 10 
    digits integer.
    """

    def generate_unique_user_id(self):
        # input user id from txt files
        admin_file = open("./data/result/user_admin.txt", "a+", encoding='utf-8')
        admin_list = admin_file.read()
        instructor_file = open("./data/result/user_instructor.txt", "a+", encoding='utf-8')
        instructor_list = instructor_file.read()
        student_file = open("./data/result/user_student.txt", "a+", encoding='utf-8')
        student_list = student_file.read()

        # closing files
        admin_file.close()
        instructor_file.close()
        student_file.close()

        # combine all user id
        user_list = admin_list + instructor_list + student_list

        # generate random user id
        uid = random.choices(range(10), k=10)
        for i in range(len(uid)):
            uid[i] = str(uid[i])
        # change generate number into string type
        uid_str = ''.join(uid)
        # put generate number into list type

        # check whether number same with given list
        while uid_str in user_list:
            uid = random.choices(range(10), k=8)
            for i in range(len(uid)):
                uid[i] = str(uid[i])
            uid_str = ''.join(uid)

        self._id = uid_str
        return int(uid_str)

    """
    3.1.3 encryption(input_password) This method encrypts the input_password 
    to a string that is difficult to read by humans. Reuse the encryption 
    algorithm that was in A1 to encode the input password. The encrypted 
    password will be returned and the type is string
    """

    def encryption(self,input_password):
        all_punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        encrypted_result = '^^^'  # Start character “^^^”
        for i in range(len(input_password)):  # loop to select character position
            if i % 3 == 0:
                # character of all_punctuation at
                # input string length module all_punctuation length as the first_character.
                character_position = len(input_password) % len(all_punctuation)
                character = all_punctuation[character_position]
                encrypted_result = encrypted_result + character + input_password[i] + character

            elif i % 3 == 1:
                # The second_character position in all_punctuation
                # is the input string length module 5.
                character_position = len(input_password) % 5
                character = all_punctuation[character_position]
                encrypted_result = encrypted_result + character * 2 + input_password[i] + character * 2

            else:
                # The third_character position in all_punctuation is the
                # input string length module 10.
                character_position = len(input_password) % 10
                character = all_punctuation[character_position]
                encrypted_result = encrypted_result + character * 3 + input_password[i] + character * 3

        encrypted_result = encrypted_result + '$$$'  # End character “$$$”
        return encrypted_result

    """
    3.1.4 login()Each user can call the login method to perform authentication. 
    In this login() method,it is required to call the encryption() method defined 
    before to encode the password.The encoded password can be used to compare with 
    the password extracted from files. You are required to to check the user_admin.txt, 
    user_instructor.txt and user_student.txt file according to the username and password
    and return a tuple which contains the login_result(bool type), 
    login_user_role(str type, the values can only be “Admin”, “Instructor”, “Student”),
    login_user_info(any type e.g. list or tuple 8 or str, this value can be used to create 
    different types of user object (Admin, Student or Instructor)).
    """

    def login(self):
        # input user id from txt files
        admin_file = open("./data/result/user_admin.txt",encoding='utf-8')
        admin_list = admin_file.read()
        instructor_file = open("./data/result/user_instructor.txt",encoding='utf-8')
        instructor_list = instructor_file.read()
        student_file = open("./data/result/user_student.txt",encoding='utf-8')
        student_list = student_file.read()

        # closing files
        admin_file.close()
        instructor_file.close()
        student_file.close()

        # return a tuple which contains the login_result(bool type),
        # login_user_role(str type, the values can only be “Admin”, “Instructor”, “Student”),
        # login_user_info(any type e.g. list or tuple 8 or str, this value can be used to create
        # different types of user object (Admin, Student or Instructor))
        login_result = False
        login_user_role = ''
        login_user_info = ''
        encrypt_password = self.encryption(self.password)
        # encrypt_password = self.password

        # print(self.username,encrypt_password)
        # check whether input username in admin list
        if self.username in admin_list:
            for i in admin_list.split('\n'):
                if self.username in i and encrypt_password in i:
                    login_result = True
                    login_user_role = 'Admin'
                    login_user_info = i
                    break

        # check whether input username in instructor list
        elif self.username in instructor_list:
            for i in instructor_list.split('\n'):
                if self.username in i and encrypt_password in i:
                    login_result = True
                    login_user_role = 'Instructor'
                    login_user_info = i
                    break

        # check whether input username in instructor list
        elif self.username in student_list:
            for i in student_list.split('\n'):
                if self.username in i and encrypt_password in i:
                    login_result = True
                    login_user_role = 'Student'
                    login_user_info = i
                    break

        # not have this account information or wrong input
        else:
            login_result = False
            login_user_role = ''

        return (login_result, login_user_role, login_user_info)

    """
    3.1.5 extract_info() This method prints out a message 
    “You have no permission to extract information”.
    """

    def extract_info(self):
        return 'You have no permission to extract information'

    """
    3.1.6 view_courses(args=[]) This method prints out a message 
    “You have no permission to view courses”.
    """

    def view_courses(self, args=[]):
        return 'You have no permission to view courses'

    """
    3.1.7 view_users()This method prints out a message
     “You have no permission to view users”.
    """

    def view_users(self):
        return 'You have no permission to view users'

    """
    3.1.8 view_reviews(args=[])This method prints out a message 
    “You have no permission to view reviews”.
    """

    def view_reviews(self,args=[]):
        return 'You have no permission to view reviews'

    """
    3.1.9 remove_data()This method prints out a message 
    “You have no permission to remove data”.
    """

    def remove_data(self):
        return 'You have no permission to remove data'

    """
    3.1.10 __str__()This method returns a formatted user string: 
    “user_id;;;username;;;password”. 
    All the attributes are concatenated using “;;;”.
    """

    def __str__(self):
        return f'{self._id};;;{self.username};;;{self.password}'
