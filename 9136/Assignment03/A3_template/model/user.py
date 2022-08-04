from lib.helper import user_data_path
from lib.helper import get_day_from_timestamp
import random
import re


class User:
    current_login_user = None
    """
    3.2.1 User class
    1. constructor.Five positional arguments: uid(int, default value is -1),
     username(str, default value is “”), password(str, default value is “”), 
     register_time(str, default value is “yyyy-MM-dd_HH:mm:ss.SSS”), 
     role(str, default value is “”). The role can only be value “admin”, 
     “instructor” and “student”.
    """

    def __init__(self, uid=-1, username="", password="", register_time="yyyy-MM-dd_HH:mm:ss.SSS", role=""):
        self.uid = uid
        self.username = username
        self.password = password
        self.register_time = register_time
        self.role = role

    """
    2. __str__()->str.  Return string format example:
    “uid;;;username;;;password;;;register_time;;;role”
    """

    def __str__(self):
        text = ';;;'.join([self.uid, self.username, self.password,
                           self.register_time, self.role])
        return text

    """
    3. authenticate_user()->(bool, str)   Two positional arguments - username and password. 
    This method is used to  check whether username and password can be matched with users 
    saved in user.txt data file. If matched, this method will retrieve the user information
    from user.txt file and return a tuple (True, user_info_string), otherwise return
    (False, “”).
    """

    def authenticate_user(self, input_username, input_password):
        encrypt_password = self.encrypt_password(input_password)
        user_info_string = ""

        # read user date file and generate user list
        with open(user_data_path, encoding='utf-8') as user_file:
            user_list = [line.strip().split(';;;') for line in user_file.readlines()]

        # login_user = None  # a User object
        #     user_info = login_user_str.strip('\n').split(";;;")
        #     # ( uid, username, password, register_time, role)
        #     if user_info[4] == 'admin':
        #         login_user = Admin(user_info[0], user_info[1], user_info[2],
        #                            user_info[3], user_info[4])

        # compare user username, password
        for user_info in user_list:
            if input_username == user_info[1] and encrypt_password == user_info[2]:
                user_info_string = ';;;'.join(user_info)
                return (True, user_info_string)

        return (False, user_info_string)

    """
    4. check_username_exist()->bool.    One positional argument - username. 
    This method is to check whether the given username exists in the user.txt data file. 
    If it exists, return True,otherwise return False.
    """

    def check_username_exist(self, input_username):
        username_exist = False
        file1 = open("data/temp_admin.txt", 'a+', encoding='utf-8').close()
        file2 = open("data/temp_ins.txt", 'a+', encoding='utf-8').close()
        file3 = open("data/temp_stu.txt", 'a+', encoding='utf-8').close()
        file4 = open("data/course.txt", 'a+', encoding='utf-8').close()
        file5 = open("data/user.txt", 'a+', encoding='utf-8').close()
        # read user date file and generate user list
        with open(user_data_path, encoding='utf-8') as user_file:
            user_list = [line.strip().split(';;;') for line in user_file.readlines()]

        # compare user username, password
        for user in user_list:
            if input_username == user[1]:
                username_exist = True
        return username_exist

    """
    5. generate_unique_user_id()->str. This method is used to generate and return a 6 
    digit unique user id which is not in the user.txt file.
    """

    def generate_unique_user_id(self):
        # read user date file and generate user list
        with open(user_data_path, encoding='utf-8') as user_file:
            user_list = user_file.read()

        # generate random user id
        uid = random.choices(range(10), k=6)
        for i in range(len(uid)):
            uid[i] = str(uid[i])
        # change generate number into string type
        uid_str = ''.join(uid)
        # put generate number into list type

        # check whether number same with given list
        while uid_str in user_list:
            uid = random.choices(range(10), k=6)
            for i in range(len(uid)):
                uid[i] = str(uid[i])
            uid_str = ''.join(uid)

        return int(uid_str)

    """
    6. encrypt_password()->str.     One positional argument - password. 
    For a given password, you are required to encrypt the string. 
    """

    def encrypt_password(self, input_password):
        all_punctuation = """!"#$%&'()*+,-./:;<>?@\^_`|~"""
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
    7.  register_user()->bool.
    Four positional arguments - username, password, email, register_time, role.
    o If the username exists in the user.txt file, return False.
    o A unique user id is required when registering a new user.
    o If the user registers successfully, return True.
    o Register_time will be a unix epoch timestamp (milli seconds) which
    needs to be converted using date_conversion() method.
    o The new user needs to be written into the user.txt file. All the attributes
    are separated by three semicolons - “;;;”. The registration of different
    roles could generate different strings.
    self.uid = uid
        self.username = username
        self.password = password
        self.register_time = register_time
        self.role = role
    example:
    285108;;;aaaaa;;;**a****a****a****a****a**;;;2021-11-29 32:32:28.590;;;admin
    """

    def register_user(self, username, password, email, register_time, role):
        register_result = False

        # If the username exists in the user.txt file, return False
        if self.check_username_exist(username):
            return register_result

        # A unique user id is required when registering a new user.
        uid = str(self.generate_unique_user_id())

        # encrypt_password()
        password = self.encrypt_password(password)

        # Register_time will be a unix epoch timestamp (milli seconds) which
        #     needs to be converted using date_conversion() method.
        register_date = self.date_conversion(register_time)

        # The new user needs to be written into the user.txt file

        text = ""
        if role == 'admin':
            text = ';;;'.join([uid, username, password, register_date, role])
        elif role == 'student':
            text = ';;;'.join([uid, username, password, register_date, role, email])

        # The 9 semi-colons here indicate there are no values for
        # display_name(str, default value is “”), job_title(str, default value is “”)
        # and course_id_list(list, default value is []).
        elif role == 'instructor':
            display_name = ""
            job_title = ""
            course_id_list = ""
            text = ';;;'.join([uid, username, password, register_date, role,
                               email, display_name, job_title, course_id_list])
        with open("data/user.txt", "a", encoding='utf-8') as user_file:
            user_file.write(text + '\n')

        # If the user registers successfully, return True.
        register_result = True
        return register_result

    """
    8. date_conversion()-> str. One positional argument - register_time. 
    The given register_time will be a unix epoch timestamp (milli seconds) 
    and it needs to be converted to format
    “year-month-day_hour:minute:second.milliseconds”. 
    For example, a  timestamp 1637549590753 will be converted to str
    “2021-11-22_13:53:10.753” and returned. The time should be GMT+11
    Melbourne timezone. Refer this link https://www.unixtimestamp.com/index.php 
    to check how to convert unix epoch time to human readable format. A method 
    called get_day_from_timestamp(timestamp) is provided in the lib.helper file. 
    By using this method, you can convert the timestamp to the day of month. 
    You can import and use this method in the user.py file. It is not allowed to 
    use any time-related libraries or functions here. You are required to implement 
    the conversion by yourself.
    """

    def date_conversion(self, register_time):

        """
        This count starts at the Unix Epoch on January 1st, 1970 at UTC
        Human Readable Time	    Seconds
        1 Hour	                3600 Seconds
        1 Day	                86400 Seconds
        1 Week	                604800 Seconds
        1 Month (30.44 days)	2629743 Seconds
        1 Year (365.24 days)	31556926 Seconds
        """
        register_time = int(register_time)
        register_data = ""
        timestamp = register_time / 1000
        timestamp = timestamp + 11 * 60 * 60
        # timestamp = time  / 1000

        total_days = int(timestamp // (24 * 60 * 60)) + 1
        current_year = 1970

        # calculate current_year
        while (total_days >= 365):
            if current_year % 4 != 0 or (current_year % 100 == 0 and current_year % 400 != 0):
                total_days -= 365
            else:
                total_days -= 366
            current_year = current_year + 1

        # calculate current_day
        current_day = get_day_from_timestamp(timestamp)

        # calculate current_month
        current_month = total_days - current_day + 1
        if current_month == 0:
            current_month = 1
        elif current_month == 31:
            current_month = 2
        elif current_month == 59 or current_month == 60:
            current_month = 3
        elif current_month == 90 or current_month == 91:
            current_month = 4
        elif current_month == 120 or current_month == 121:
            current_month = 5
        elif current_month == 151 or current_month == 152:
            current_month = 6
        elif current_month == 181 or current_month == 182:
            current_month = 7
        elif current_month == 212 or current_month == 213:
            current_month = 8
        elif current_month == 243 or current_month == 244:
            current_month = 9
        elif current_month == 273 or current_month == 274:
            current_month = 10
        elif current_month == 304 or current_month == 305:
            current_month = 11
        elif current_month == 334 or current_month == 335:
            current_month = 12

        remain_time = timestamp % 86400
        current_hour = int(remain_time // (60 * 60))
        remain_min = remain_time - current_hour * 60 * 60
        current_min = int(remain_min // 60)
        remain_second = remain_min - current_min * 60
        current_second = int(remain_second)
        remain_ms = remain_second % 1
        current_ms = round(remain_ms, 3)
        display_second = current_second + current_ms

        register_date = f'{current_year}-{current_month}-{current_day}_' \
                        f'{current_hour}:{current_min}:{display_second}'

        return register_date

    """
    9. validate_username()-> bool.  One positional argument - username. 
    The username can only be letters or underscore. If not, return False.
    """

    def validate_username(self, username):
        validate_result = False
        if re.match("^[A-Za-z_-]*$", username):
            validate_result = True
        return validate_result

    """
    10.validate_password()-> bool. One positional argument - password. 
    The length of password must be greater than or equal to 8. If not, return False.
    """

    def validate_password(self, password):
        validate_result = False
        if len(password) >= 5:
            validate_result = True
        return validate_result

    """
    11.validate_email()-> bool. One positional argument - email. Use regex 
    expressions to check whether the email address is valid or not. The email 
    should end with “.com”, contain “@”, and have length greater than 8. 
    If not, return False.
    """

    def validate_email(self, email):
        validate_result = False
        if len(email) >= 8:
            if re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.com$", email):
                validate_result = True
        return validate_result

    """
    12.clear_user_data() no return.remove all the data in the user.txt file.
    """

    def clear_user_data(self):
        # delete all the data in course.txt files
        open(user_data_path, "w", encoding='utf-8').close()

    """
    13.txt_merge() merge all temp txt files into user.txt.
    """

    def txt_merge(self):
        file1 = open("data/temp_admin.txt", 'a+', encoding='utf-8').close()
        file2 = open("data/temp_ins.txt", 'a+', encoding='utf-8').close()
        file3 = open("data/temp_stu.txt", 'a+', encoding='utf-8').close()
        file4 = open("data/course.txt", 'a+', encoding='utf-8').close()
        file5 = open("data/user.txt", 'a+', encoding='utf-8').close()

        with open("data/temp_admin.txt", encoding='utf-8') as admin_file:
            admin_list = admin_file.read()
        # print(admin_list[0])
        with open("data/temp_ins.txt", encoding='utf-8') as ins_file:
            ins_list = ins_file.read()
        # print(ins_list[0])
        with open("data/temp_stu.txt", encoding='utf-8') as stu_file:
            stu_list = stu_file.read()
        # print(stu_list[0])
        user_list = admin_list + ins_list + stu_list
        # print(user_list[0])
        with open("data/user.txt", "w", encoding='utf-8') as user_file:
            user_file.write(user_list)
