from flask import Blueprint, render_template, request, redirect, url_for
from lib.helper import render_result, render_err_result, course_data_path, user_data_path
from model.course import Course
from model.user import User
from model.user_admin import Admin
from model.user_instructor import Instructor
from model.user_student import Student

user_page = Blueprint("user_page", __name__)

model_user = User()
model_course = Course()
model_student = Student()

"""
2. login() in user_controller. GET request, route is “/login”.
Return the “00login.html” page.
"""


@user_page.route("/login")
def login():
    return render_template("00login.html")


"""
3. login_post() in user_controller. POST request, route is “/login”.
Get “username”, “password” values from the request.values. Use the user
validation methods to check the username and password. If all valid, call the
authentication method. If username and password belong to a valid user,
return the string info of this user. Then, generate a corresponding user object
using the generate_user() method and assign this user to the
User.current_login_user class variable.
"""


@user_page.route("/login", methods=["POST"])
def login_post():
    # Get “username”, “password” values from the request.values
    req = request.values
    username = req["username"] if "username" in req else ""
    password = req["password"] if "password" in req else ""
    # check the username and password. If valid,
    if (model_user.validate_username(username)) and (model_user.validate_password(password)):
        login_result, user_info = model_user.authenticate_user(username, password)
    else:
        return render_err_result(msg="Plz input valid username or password! ")

    # authentication method. If username and password belong to a valid user,
    # return the string info of this user.
    if login_result:
        user_object = generate_user(user_info)
        User.current_login_user = user_object
        return render_result(msg="Login success! ")
    else:
        return render_err_result(msg="username or password not correct plz check! ")


"""
5. logout() in user_controller. GET request, route is “/logout”.
Reset the User.current_login_user to None and return the “01index.html”
page.
"""


@user_page.route("/logout")
def logout():
    User.current_login_user = None
    return render_template("01index.html")


"""
6. generate_user(login_user_str) in user_controller.
This method is defined and used only in user_controller for login_post()
method. Because after login, it is required to generate a user object(could be
Admin, Instructor or Student). Since using child class in parent class will cause
exceptions, the User.authenticate_user() method cannot return an
Admin/Instructor/Student object directly. So,you need to return a user string
in User.authenticate_user() and convert the user string to an object in this
generate_user() method. The return object could be
Admin()/Instructor()/Student().
"""


def generate_user(login_user_str):
    login_user = None  # a User object
    user_info = login_user_str.strip('\n').split(";;;")
    # ( uid, username, password, register_time, role)
    if user_info[4] == 'admin':
        login_user = Admin(user_info[0], user_info[1], user_info[2],
                           user_info[3], user_info[4])

    # ([self.uid, self.username, self.password, self.register_time,
    # self.role, self.email, self.display_name, self.job_title,
    #  self.course_id_list])
    elif user_info[4] == 'instructor':
        login_user = Instructor(user_info[0], user_info[1], user_info[2], user_info[3],
                                user_info[4], user_info[5], user_info[6], user_info[7],
                                user_info[8])

    # [self.uid, self.username, self.password,
    #  self.register_time, self.role, self.email]
    elif user_info[4] == 'student':
        login_user = Student(user_info[0], user_info[1], user_info[2],
                             user_info[3], user_info[4], user_info[5])

    return login_user


# use @user_page.route("") for each page url

"""
7. register() in user_controller. GET request, route is “/register”.
Return the “00register.html” page.
"""


@user_page.route("/register")
def register():
    return render_template("00register.html")


"""
8. register_post() in user_controller. POST request, route is “/register”.
Get “username”, “password”, “email”, “register_time”, “role” values from the
request.values. Use the user validation methods to check the username,
password and email. If all valid, register this user. Otherwise, return
render_err_result(msg=”proper message for users”).
"""


@user_page.route("/register", methods=["POST"])
def register_post():
    # Get “username”, “password” values from the request.values
    req = request.values
    username = req["username"] if "username" in req else ""
    password = req["password"] if "password" in req else ""
    email = req["email"] if "email" in req else ""
    register_time = req["register_time"] if "register_time" in req else ""
    role = req["role"] if "role" in req else ""

    # Use the user validation methods to check the username,
    # password and email
    if model_user.validate_username(username) and model_user.validate_password(password) and model_user.validate_email(
            email):
        # If all valid, register this user
        model_user.register_user(username, password, email, register_time, role)
        return render_result(msg="new user register! ")
    else:
        # Otherwise, return render_err_result(msg=”proper message for users”)
        return render_err_result(msg="Failed register plz check! ")


"""
3.4. Task 3 - Students page
1. student_list() in user_controller. GET request, route is “/student-list”.
Try to write this method by referring to the instructor_list and course_list.
Make sure the context dict has “context['one_page_user_list']”,
“context['total_pages']”, “context['page_num_list']”, “context['current_page']”,
“context['total_num']”, “context["current_user_role"]” has values as the web
pages need to show these values and may cause errors if these values are not
exist.
"""


@user_page.route("/student-list")
def student_list():
    # check login user
    if User.current_login_user:
        req = request.values
        page = req['page'] if 'page' in req else 1
        context = {}
        # “context['one_page_user_list']”,
        # “context['total_pages']”, “context['page_num_list']”, “context['current_page']”,
        # “context['total_num']”, “context["current_user_role"]”
        one_page_user_list, total_pages, total_num = model_student.get_students_by_page(int(page))
        # get values for page_num_list
        page_num_list = model_course.generate_page_num_list(int(page), int(total_pages))
        # check one_page_instructor_list, make sure this variable not be None, if None, assign it to []
        if not one_page_user_list:
            one_page_user_list = []

        context['one_page_user_list'] = one_page_user_list
        context['total_pages'] = total_pages
        context['page_num_list'] = page_num_list
        context['current_page'] = int(page)
        context['total_num'] = total_num
        # add "current_user_role" to context
        context['current_user_role'] = User.current_login_user.role

    else:
        return redirect(url_for("index_page.index"))

    return render_template("10student_list.html", **context)


"""
2. student_info() in user_controller. GET request, route is “/student-info”.
Find a student based on the “id” attribute in the request.values. If not exist,
return a new student and set all instance variables with default values. Make
sure the “context["current_user_role"]” has values
"""


@user_page.route("/student-info")
def student_info():
    req = request.values
    student_id = req['id'] if "id" in req else ""
    context = {}

    # If not exist,
    # return a new student and set all instance variables with default values.
    if student_id == "":
        student = model_student.__init__()
    else:
        student = model_student.get_student_by_id(student_id)

    # uid, username, password, register_time, role
    context['id'] = student_id
    # context['username'] = student[1]
    # context['password'] = student[2]
    # context['register_time'] = student[3]
    # context['current_user_role'] = User.current_login_user.role
    # context['email'] = student[-1]
    context['username'] = student.username
    context['password'] = student.password
    context['register_time'] = student.register_time
    context['current_user_role'] = User.current_login_user.role
    context['email'] = student.email

    return render_template("11student_info.html", **context)


"""
3. student_delete() in user_controller. GET request, route is “/student-delete”.
Delete student according to the “id” attribute in the request.values. This
method will return “redirect(url_for(user_page.student_list))” if successful.
Otherwise, return “redirect(url_for(index_page.index))”
"""


@user_page.route("/student-delete")
def student_delete():
    req = request.values
    student_id = req['id']
    # Delete student according to the “id” attribute in the request.values
    result = model_student.delete_student_by_id(student_id)
    # different result
    if result:
        return redirect(url_for("user_page.student_list"))
    else:
        return redirect(url_for("index_page.index"))
