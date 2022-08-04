from User import User
from Course import Course
from Review import Review
class Instructor(User):
    """
    3.3.1 constructor The attributes of instructor are id(int, default value -1),
    username(str, default value“”), password(str, default value “”),
    display_name(str, default value “”), job_title(str,default value “”),
    image_100x100(str, default value “”), course_id_list(list, default value []).
    """

    def __init__(self,_id = -1,username = "", password = "",display_name="",
                                     job_title="",image_100x100="",course_id_list=[]):
        User.__init__(self,_id,username,password)
        self.display_name = display_name
        self.job_title = job_title
        self.image_100x100 = image_100x100
        self.course_id_list = course_id_list

    """
    3.3.2 view_courses(args=[]) Print out all the courses taught by this instructor. 
    This can be reached by calling the method implemented in the Course class. 
    If the number of courses is greater than 10, only print 10 courses. 
    The args positional argument is not used in this method.
    """

    def view_courses(self,args=[]):
        # by calling the method implemented in the Course class
        course_list = Course().find_course_by_instructor_id(self._id)

        course_content = []

        # Print out all the courses taught by this instructor
        for course in course_list:
            course_content.append(course)

        # If the number of courses is greater than 10, only print 10 courses.
        # if len(course_content) >= 10:
        #     course_content = course_content[:10]
        for course in course_content[:10]:
            print(course)
        print(f"the total number of courses is: {len(course_content)}")


    """
    3.3.3 view_reviews(args=[])Print out all the reviews belong to the courses this 
    instructor teaches. This can be achieved by calling the method implemented in the 
    Course class. If the number of reviews is greater than 10, only print 10 reviews. 
    Also print out the total number of all reviews. The args positional argument is 
    not used in this method
    """

    def view_reviews(self,args=[]):
        instructor_id = self._id
        course_list = Course().find_course_by_instructor_id(instructor_id)
        # print(course_list)
        review_content = []
        # Print out all the courses taught by this instructor
        for course in course_list:
            review_list = Review().find_review_by_course_id(course.course_id)
            review_content.extend(review_list)

        # If the number of reviews is greater than 10, only print 10 reviews
        # if len(review_content) >= 10:
        #     review_content = review_content[:10]
        for review in review_content[:10]:
            print(review)
        print(f"the total number of reviews is: {len(review_content)}")

    """
    3.3.4 __str__() Use the Parent class __str__ method. The return result format is:
    “user_id;;;username;;;password;;;display_name;;;job_title;;;
    image_100x100;;;123123–323–32–3123–3123” 
    """

    def __str__(self):
        course_id = '-'.join(self.course_id_list)
        text =';;;'.join([self._id,self.username,self.password,
                          self.display_name,self.job_title,
                          self.image_100x100,course_id])
        return text