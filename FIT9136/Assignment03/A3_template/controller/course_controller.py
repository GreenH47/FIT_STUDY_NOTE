from flask import Blueprint, render_template, request, redirect, url_for
from lib.helper import render_result, render_err_result, course_data_path, user_data_path
from model.user import User
from model.course import Course
from model.user_instructor import Instructor

import pandas as pd

from flask import render_template, Blueprint

course_page = Blueprint("course_page", __name__)

model_course = Course()
model_instructor = Instructor()
model_user = User()


def reset_database():
    pass


"""
3.5. Task 4 - Courses page
1. course_list() in course_controller. GET request, route is “/course-list”.
In this method, some code is already provided. Add more code to make the
method run. If the user is not logged in, should not allow access to the courses
and redirect the page to “index_page.index”. If there exists a logged user, get
the expected course list and page number list. Make sure the
“context["current_user_role"]” has values.
For Mac users, if you meet the “Method not allowed” error in pages, try to
refresh the page. If the result can show properly, there should be no errors in
your backend logic and you can ignore this error
"""


@course_page.route("/course-list")
def course_list():
    context = {}
    # check login user
    if User.current_login_user:
        req = request.values
        page = req['page'] if "page" in req else 1

        # get values for one_page_course_list, total_pages, total_num
        one_page_course_list, total_pages, total_num = model_course.get_courses_by_page(int(page))
        # check one_page_course_list, make sure this variable not be None, if None, assign it to []
        if not one_page_course_list:
            one_page_course_list = []
        # get values for page_num_list
        page_num_list = model_course.generate_page_num_list(int(page), int(total_pages))

        context['one_page_course_list'] = one_page_course_list
        context['total_pages'] = total_pages
        context['page_num_list'] = page_num_list
        context['current_page'] = int(page)
        context['total_num'] = total_num

        # add "current_user_role" to context
        context['current_user_role'] = User.current_login_user.role

    else:
        return redirect(url_for("index_page.index"))
    return render_template("02course_list.html", **context)

"""
2. reset_database() in course_controller. POST request, route is
“/reset-database”.
This method simply removes all the content in the user.txt and course.txt files
by calling methods in User and Course class. After finish, return a success
message. If an error happens, return the render_err_result(msg=”exception
happened”) method result. Use try except block in this method to handle
exceptions.
"""
@course_page.route("/reset-database")
def reset_database(self):
    try:
        # removes all the content
        model_user.clear_user_data()
        model_course.clear_course_data()
        return render_result(msg="erase data finished")
    except:
        return render_err_result(msg="can not erase data")

@course_page.route("/process-course", methods=["POST"])
def process_course():
    try:
        model_course.get_courses()
    except Exception as e:
        print(e)
        return render_err_result(msg="error in process course")

    return render_result(msg="process course finished successfully")


@course_page.route("/course-details")
def course_details():
    context = {}
    if User.current_login_user:
        req = request.values
        course_id = req['id'] if "id" in req else -1

        if course_id == -1:
            course = None
        else:
            course, overall_comment = model_course.get_course_by_course_id(int(course_id))

        if not course:
            context["course_error_msg"] = "Error, cannot find course"
        else:
            context['course'] = course
            context['overall_comment'] = overall_comment
        context['current_user_role'] = User.current_login_user.role

    return render_template("03course_details.html", **context)


@course_page.route("/course-delete")
def course_delete():
    req = request.values
    course_id = req['id'] if "id" in req else -1
    print("course delete:", course_id)
    if course_id == -1:
        return render_err_result(msg="course cannot find")
    result = model_course.delete_course_by_id(int(course_id))
    print("course delete:", result)
    if result:
        return redirect(url_for("course_page.course_list"))
    else:
        return render_err_result(msg="course delete error")


@course_page.route("/course-analysis")
def course_analysis():
    context = {}
    if User.current_login_user:
        explain1 = model_course.generate_course_figure1()
        explain2 = model_course.generate_course_figure2()
        explain3 = model_course.generate_course_figure3()
        explain4 = model_course.generate_course_figure4()
        explain5 = model_course.generate_course_figure5()
        explain6 = model_course.generate_course_figure6()

        context['explain1'] = explain1
        context['explain2'] = explain2
        context['explain3'] = explain3
        context['explain4'] = explain4
        context['explain5'] = explain5
        context['explain6'] = explain6
        context['current_user_role'] = User.current_login_user.role
    else:
        return redirect(url_for("course_page.course_list"))

    return render_template("04course_analysis.html", **context)
