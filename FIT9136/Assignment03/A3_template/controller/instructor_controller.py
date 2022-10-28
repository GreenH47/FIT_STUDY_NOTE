from flask import Blueprint, render_template, request, redirect, url_for
from lib.helper import render_result, render_err_result, course_data_path, user_data_path
from model.user import User
from model.course import Course

import pandas as pd
from flask import render_template, Blueprint

from model.user_instructor import Instructor

instructor_page = Blueprint("instructor_page", __name__)

model_instructor = Instructor()
model_course = Course()

"""
3.6. Task 5 - Instructors page
1. Instructor_list() in instructor_controller. Get request, route is “/instructor-list”.
In this method, some code is already provided. Add more code to make the
method run. If the user is not logged in, should not allow access to the
instructors and redirect the page to “index_page.index”. If there exists a
logged user, get the expected instructor list and page number list. Make sure
the “context["current_user_role"]” has values.
For Mac users, if you meet the “Method not allowed” error in pages, try to
refresh the page. If the result can show properly, there should be no errors in
your backend logic and you can ignore this error.
"""


@instructor_page.route("/instructor-list")
def instructor_list():
    # check login user
    if User.current_login_user:
        req = request.values
        page = req['page'] if "page" in req else 1
        context = {}
        # get values for one_page_instructor_list, total_pages, total_num
        one_page_instructor_list, total_pages, total_num = model_instructor.get_instructors_by_page(int(page))
        # get values for page_num_list
        page_num_list = model_course.generate_page_num_list(int(page), int(total_pages))
        # check one_page_instructor_list, make sure this variable not be None, if None, assign it to []
        if not one_page_instructor_list:
            one_page_instructor_list = []

        context['one_page_instructor_list'] = one_page_instructor_list
        context['total_pages'] = total_pages
        context['page_num_list'] = page_num_list
        context['current_page'] = int(page)
        context['total_num'] = total_num
        # add "current_user_role" to context
        context['current_user_role'] = User.current_login_user.role

    else:
        return redirect(url_for("index_page.index"))

    return render_template("07instructor_list.html", **context)


"""
2. teach_courses() in instructor_controller. GET request, route is
“/teach-courses”.
In this method , some code is already provided. Add more code to make the
method run. If the user is not logged in, should not allow access to the teach
courses and redirect the page to “index_page.index”. If there exists an “id”
attribute in the request.values, assign this value to the instructor_id. If there is
no “id” attribute in the request.values, use the current logged user’s id as the
instructor_id. Then, you can get the teach courses list. Make sure the
“context["current_user_role"]” has values.
"""


@instructor_page.route("/teach-courses")
def teach_courses():
    context = {}
    # check login user
    if User.current_login_user:
        # get instructor id
        req = request.values
        instructor_id = req['id'] if "id" in req else ""

        # If there is no “id” attribute in the request.values, use the current
        # logged user’s id as the instructor_id.
        if instructor_id == "":
            instructor_id = User.current_login_user.uid
        # get values for course_list, total_num
        course_list, total_num = model_course.get_course_by_instructor_id(instructor_id)

        context['course_list'] = course_list
        context['total_num'] = total_num
        # add "current_user_role" to context
        context['current_user_role'] = User.current_login_user.role

    else:
        return redirect(url_for("index_page.index"))
    return render_template("09instructor_courses.html", **context)


@instructor_page.route("/instructor-analysis")
def instructor_analysis():
    # if Instructor.instructor_data.shape[0] == 0:
    #     return render_err_result(msg="no instructor in datafile")

    explain1 = model_instructor.generate_instructor_figure1()

    context = {}
    context['explain1'] = explain1

    return render_template("08instructor_analysis.html", **context)


@instructor_page.route("/process-instructor", methods=["POST"])
def process_instructor():
    try:
        model_instructor.get_instructors()
    except Exception as e:
        print(e)
        return render_err_result(msg="error in process instructors")

    return render_result(msg="process instructors finished successfully")
