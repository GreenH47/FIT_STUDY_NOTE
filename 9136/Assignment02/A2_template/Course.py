
class Course:
    """
    3.5.1 constructor The attributes of course are course_id(int, default value -1),
    course_title(str, default value “”), course_image_100x100(str, default value “”),
    course_headline(str, default value “”), course_num_subscribers(int, default value -1),
    course_avg_rating(float,default value -1.0), course_content_length(float, default value -1.).
    """

    def __init__(self, course_id=-1, course_title="", course_image_100x100="",
                 course_headline="", course_num_subscribers=-1,
                 course_avg_rating=-1.0, course_content_length =-1.0):
        self.course_id = course_id
        self.course_title = course_title
        self.course_image_100x100 = course_image_100x100
        self.course_headline = course_headline
        self.course_num_subscribers = course_num_subscribers
        self.course_avg_rating = course_avg_rating
        self.course_content_length = course_content_length

    """
    3.5.2 find_course_by_title_keyword(keyword) This method has a positional argument 
    keyword(str). Based on the given keyword, it searches the course title of all courses 
    in the course.txt file to find the result. All the result courses will be created as 
    a course object and added into a result list. Finally, return the result list. The 
    result list looks like [Course(), Course(), Course()….]. If not found, return an 
    empty list
    """

    def find_course_by_title_keyword(self,keyword):
        with open("./data/result/course.txt",encoding='utf-8') as course_file:
            course_list = [line.strip().split(';;;') for line in course_file.readlines()]

        # Based on the given keyword, it searches the course title of all courses in the
        # course.txt file to find the result.
        course_search = []
        for course in course_list:
            if keyword in course[1]:
                course_search.append(course)

        #All the result courses will be created as a course object and
        # added into a result list
        course_content = []
        for course in course_search:
            course_content.append(Course(course[0],course[1],course[2],
                                         course[3],course[4],course[5],course[6]))

        return course_content

    """
    3.5.3 find_course_by_id(course_id) This method has a positional argument 
    course id(int or str). You are required to search for the course according to the 
    course id. A course object will be returned. If not found, return None.
    """

    def find_course_by_id(self,course_id):
        with open("./data/result/course.txt", "r", encoding='utf-8') as course_file:
            course_list = [line.strip().split(';;;') for line in course_file.readlines()]

        # Based on the given course id(int or str), it searches the course title of
        # all courses in the course.txt file to find the result.
        for course in course_list:
            if course[0] == course_id:
                return Course(course[0], course[1], course[2],course[3],
                       course[4], course[5], course[6])

    """
    3.5.4 find_course_by_instructor_id(instructor_id) This method has a positional argument 
    instructor id(int or str). Based on the instructor id, a list of course objects will 
    be generated and returned. The result list looks like 
    [Course(), Course(), Course()….]. If not found, return an empty list.
    """

    def find_course_by_instructor_id(self, instructor_id):
        with open("./data/result/user_instructor.txt", "r", encoding='utf-8') as instructor_file:
            instructor_list = [line.strip().split(';;;') for line in instructor_file.readlines()]

        # Based on the given instructor id(int or str), it searches the course title of
        # all courses in the instructor.txt file to find the result.
        # print(instructor_id)
        for instructor in instructor_list:
            if instructor[0] == instructor_id:
                course_id = instructor[-1].split('-')
                # print(course_id)
                instructor_content = []
                for co_id in course_id:
                    instructor_content.append(Course().find_course_by_id(co_id))
                return instructor_content

    """
    3.5.5 courses_overview() This method returns a string that shows the total number of courses.
    """

    def courses_overview(self):
        initial_file = open("./data/result/course.txt", 'a+', encoding='utf-8')
        initial_file.close()
        with open("./data/result/course.txt", encoding='utf-8') as course_file:
            course_list = course_file.readlines()
        text = f'The total number of courses is {len(course_list)}'
        return text

    """
    3.5.6 __str__() Return a string containing all course information.
    course_id=-1, course_title="", course_image_100x100="", course_headline="", 
    course_num_subscribers=-1,course_avg_rating=-1.0, course_content_length =-1
    """

    def __str__(self):
        text = f'Course id: {self.course_id}\nCourse title: {self.course_title}\n' \
               f'Course image: {self.course_image_100x100}\nCourse headline: {self.course_headline}\n' \
               f'Course subscribers: {self.course_num_subscribers}\nCourse rating: {self.course_avg_rating}\n' \
               f'Course length: {self.course_content_length}\n'
        return text