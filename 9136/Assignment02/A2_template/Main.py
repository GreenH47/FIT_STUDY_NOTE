import re
import os
import random
from User import User
from Admin import Admin
from Course import Course
from Review import Review
from Student import Student
from Instructor import Instructor

def __init__():
    pass
"""
3.7.1 show_menu()This method prints out the available options that the user
can choose. You can add positional arguments if you need.
"""
def show_menu(login_user_role):
    text = (f"""
{login_user_role} login successfully
Welcome {login_user_role} ,Your role is {login_user_role}.
Please enter {login_user_role} command for further service:
1. EXTRACT_DATA
2. VIEW_COURSES
3. VIEW_USERS
4. VIEW_REVIEWS
5. REMOVE_DATA
""")
    return text

"""
3.7.2 process_operations(user_object) This method has one positional argument 
user_object.Admin can take commands “1”, “2”, “3”, “4”, “5”. 
For command “2” and “4”, the end user needs to enter 
“TITLE_KEYWORD/ID/INSTRUCTOR_ID” and “ID/KEYWORD/COURSE_ID” as a second command, 
followed by a value. For example,if the login user is admin, he can input 
“2 TITLE_KEYWORD web”(the value after the second command can only be one word). 
The system will call corresponding view course methods and print out all the 
courses whose title contains “web” (case insensitive). If the user does not 
enter any other arguments for command “2” and “4”, a default overview output 
will be displayed. Instructor and Student can take command “2”, “4” and no other 
arguments are allowed. If the logged user is instructor or student and the command 
is “1”, “3”, “5”, the inherited methods in User class will be executed. When a 
user input “logout”, logout the user but the system keeps running.In this method, 
it is not allowed to create an object of Admin/Instructor/Student class. It is 
assumed that a User class object user_object is passed into this method and 
you are not sure about the exact type.
"""
def process_operations(user_object):
    # Admin can take commands “1”, “2”, “3”, “4”, “5”.
    if isinstance(user_object,Admin):
        # service = input(show_menu('Admin'))
        while True:
            service = input(show_menu('Admin'))
            if service == 'logout':
                break
            elif service.startswith('1'):
                user_object.extract_info()
                print('EXTRACT_DATA completed')
            elif service.startswith('2'):
                if len(service.split()) == 3:
                    user_object.view_courses([service.split()[1],service.split()[2]])
                else:
                    user_object.view_courses()
            elif service.startswith('3'):
                user_object.view_users()
            elif service.startswith('4'):
                if len(service.split()) == 3:
                    user_object.view_reviews([service.split()[1],service.split()[2]])
                else:
                    user_object.view_reviews()
            elif service.startswith('5'):
                user_object.remove_data()
                print('REMOVE_DATA completed')
            else:
                print('input  arguments for command invalid! please follow the pattern!')
                continue

    # instructor or student can take command “2”, “4” and no other
    #     arguments are allowed
    elif isinstance(user_object,Instructor):

        while True:
            service = input(show_menu('Instructor'))
            if service == 'logout':
                break
            elif service.startswith('1'):
                print('You have no permission to extract information')
            elif service.startswith('2'):
                user_object.view_courses()
            elif service.startswith('3'):
                print('You have no permission to view users')
            elif service.startswith('4'):
                user_object.view_reviews()
            elif service.startswith('5'):
                print('You have no permission to remove data')
            else:
                print('input invalid! please follow the pattern!')
                continue

    # instructor or student can take command “2”, “4” and no other
    #     arguments are allowed
    elif isinstance(user_object,Student):

        while True:
            service = input(show_menu('Student'))
            if service == 'logout':
                break
            elif service.startswith('1'):
                print('You have no permission to extract information')
            elif service.startswith('2'):
                user_object.view_courses()
            elif service.startswith('3'):
                print('You have no permission to view users')
            elif service.startswith('4'):
                user_object.view_reviews()
            elif service.startswith('5'):
                print('You have no permission to remove data')
            else:
                print('input invalid! please follow the pattern!')
                continue

"""
3.7.2 main() This method handles the main logic of your system. 
No positional arguments here. It should keep running until the user input “exit”. 
At the beginning, this method asks the user to enter username and password in 
format “username password”. Next,create a temp_user object and only assign the 
username and password to this object. Then you can use temp_user to call the 
login() method. Based on the login result, a corresponding user object can be 
created (Admin(), Instructor() or Student()). For different user objects, 
call the same process_operations(user_object) method to process all the logics. 
If the logged user is “Admin”, 1) create an Admin object, 2) call 
show_menu() method, 3) call process_operations() method. If the login fails, 
printout an error message. If the username password format is incorrect, 
print out a different error message.
"""

def main():
    while True:
        #  asks the user to enter username and password
        user_input = input('Please enter username and password format “username password”: \n')
        # quit the program
        if user_input == 'exit':
            print('Thanks using! Program shut down')
            break

        # user input not follow the format
        elif len(user_input.split()) != 2:
            print('input format “username password”')
            continue

        else:
            user = User(-1,user_input.split()[0],user_input.split()[1])
            login_result, login_user_role, login_user_info = user.login()


            if not login_result:
                # user not login
                print('Please check password or account')
                continue
            else:
                login_user_info = login_user_info.split(';;;')

                # admin(_id=-1, username="", password="")
                if login_user_role == 'Admin':
                    admin = Admin(login_user_info[0],login_user_info[1],login_user_info[2])
                    process_operations(admin)

                # Instructor(_id = -1,username = "", password = "",display_name="",
                #   job_title="",image_100x100="",course_id_list=[])
                elif login_user_role == 'Instructor':
                    instructor = Instructor(login_user_info[0],login_user_info[1],login_user_info[2],
                                            login_user_info[3],login_user_info[4],login_user_info[5],
                                            login_user_info[6].split('-'))
                    process_operations(instructor)

                # student(_id = -1,username = "", password = "",user_title="",
                # user_image_50x50="",user_initials="",review_id=-1)
                elif login_user_role == 'Student':
                    student = Student(login_user_info[0],login_user_info[1],login_user_info[2],
                                            login_user_info[3],login_user_info[4],login_user_info[5],
                                            login_user_info[6])
                    process_operations(student)

"""
3.7.3 if __name__ == “__main__”: This part is the entry point of the whole program. 
In code part, 1. output a message to indicate the program start. 
2. Manually register an admin account(call register_admin() method). 
In your "_ _ main _ _" function, create an
Admin object and give this object the username and password
3. Call the main() method. When marking your assignment, we will run this file only
"""
if __name__ == "__main__":
    # print a welcome message
    print('Welcome to our system!')

    # manually register admin
    admin = Admin(-1, 'ccc', 'password')
    admin.register_admin()


    # https://edstem.org/au/courses/7429/discussion/782697
    main()







