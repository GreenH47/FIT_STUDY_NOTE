from User import User
from Course import Course
from Review import Review
class Student(User):
    """
    3.4.1 constructor The attributes of student are id(int, default value -1),
    username(str, default value “”),password(str, default value “”),
    user_title(str, default value “”), user_image_50x50(str,default value “”),
    user_initials(str, default value “”), review_id(int, default value -1).
    """

    def __init__(self,_id = -1,username = "", password = "",user_title="",
                 user_image_50x50="",user_initials="",review_id=-1):
        User.__init__(self,_id,username,password)
        self.user_title = user_title
        self.user_image_50x50 = user_image_50x50
        self.user_initials = user_initials
        self.review_id = review_id

    """
    3.4.2 view_courses(args=[])This method prints out the course this student registered. 
    If a student reviews a course, it is assumed that the student is registered in that 
    course. The args positional argument is not used in this method. 
    Just have it when doing method declaration.
    """

    def view_courses(self,args=[]):
        with open("./data/result/user_student.txt", encoding='utf-8') as student_file:
            student_list = [line.strip().split(';;;') for line in student_file.readlines()]
        i = 0
        for student in student_list:
            if self._id == student[0]:
                i = i +1
                review_id = student[-1]
                # only print first 10 courses
                if i < 11:
                    review_list = Review().find_review_by_id(review_id)
                    course_list = Course().find_course_by_id(review_list.course_id)
                    print(course_list)
        # review_list = Review().find_review_by_id(review_id)
        # course_list = Course().find_course_by_id(review_list.course_id)
        # print(course_list)
        print(f"Your courses total number  is: {i}")

    """
    3.4.3 view_reviews(args=[]) This method prints out the review this student wrote. 
    The args positional argument is not used in this method. 
    Just have it when doing method declaration.
    """

    def view_reviews(self,args=[]):
        with open("./data/result/user_student.txt", encoding='utf-8') as student_file:
            student_list = [line.strip().split(';;;') for line in student_file.readlines()]
        i = 0
        for student in student_list:
            if self._id == student[0]:
                i = i + 1
                review_id = student[-1]
                # only print first 10 reviews
                if i < 11:
                    review_list = Review().find_review_by_id(review_id)
                    print(review_list)
        # review_list = Review().find_review_by_id(review_id)
        # print(review_list)
        print(f"Your reviews total number  is: {i}")

    """
    3.4.4 __str__() Use the parent class __str__ method. The return result format is: 
    ”user_id;;;username;;;password;;;title;;;image_50x50;;;initials;;;review_id” 
    id(int, default value -1),
    username(str, default value “”),password(str, default value “”),
    user_title(str, default value “”), user_image_50x50(str,default value “”),
    user_initials(str, default value “”), review_id(int, default value -1).
    """

    def __str__(self):

        text = ';;;'.join([self._id, self.username, self.password,
                           self.user_title, self.user_image_50x50,
                           self.initials, self.review_id])
        return text