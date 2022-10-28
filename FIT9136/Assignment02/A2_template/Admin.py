import re
import os
from User import User
from Course import Course
from Review import Review


class Admin(User):
    """
    3.2.1 constructor Admin only have attributes id(int, default value -1),
    username(str, default value “”)and password(str, default value “”)
    which can be inherited from the parent class.
    """

    def __init__(self, _id=-1, username="", password=""):
        User.__init__(self, _id, username, password)

    """
    3.2.2 register_admin() This method checks the user_admin.txt file 
    to find out whether the username already exists or not. 
    If not, register this admin. If it exists, do nothing.
    """

    def register_admin(self):
        # read user_admin.txt file
        # admin_list = []
        initial_file = open("./data/result/user_admin.txt",'a+', encoding='utf-8')
        initial_file.close()
        with open("./data/result/user_admin.txt",encoding='utf-8') as admin_file:
            # for line in admin_file.readlines():
            #     admin_list = admin_list.append(line.strip().split(';;;'))
            admin_list = [line.strip().split(';;;') for line in admin_file.readlines()]
        # print(admin_list)
        # print(self.username)
        # find out whether the username already exists or register this admin
        i = 0
        for admin in admin_list:
            if self.username not in admin:
                i = i + 1
        if i == len(admin_list):
            # print(i,len(admin_list))
            with open("./data/result/user_admin.txt","a+", encoding='utf-8') as admin_file2:
                # admin_password = self.encryption(self.password)
                user_id = self.generate_unique_user_id()
                password = User().encryption(self.password)
                text = f'{user_id};;;{self.username};;;{password}\n'
                admin_file2.write(text)
                text2 =(f'Admin account  register successfully\n'
                        f'User id: {user_id}\n'
                        f'User name: {self.username}\n'
                        f'User password: {self.password}\n')
                print(text2)

        else:
            print('Admin account already exists!')

    """
    3.2.3 extract_course_info()This method can get course information from the 
    raw_data.txt. The extracted course info should be saved into file following 
    the format below:
    “course_id;;;course_title;;;image_100x100;;;headline;;;num_of_subscribers;;;
    avg_rating;;;course_content_length” .
    For each line in the raw_data.txt file, you can copy and paste it to Json 
    Parser Onlineto check the format. Each line contains more than one course.
    All the corresponding attributes can be found in the text. You can use the 
    library re or str methods to extract the data. The course content length in the 
    text is like “40.5 hours”. Only 40.5 need to be retrieved. The course data 
    will be saved into the course.txt file
    """

    def extract_course_info(self):
        with open("./data/course_data/raw_data.txt", "r", encoding='utf-8') as raw_file1:
            raw_list = raw_file1.readlines()
        course_info = []

        for line in raw_list:
            # find course id
            course_id = re.findall(r'"_class":"course","id":(\d+?),"title":', line)

            # find course title
            course_title = re.findall(r'"course","id":\d+?,"title":"(.*?)"', line)

            # find image_100x100
            image_100x100 = re.findall(r'"image_50x50":".*?","image_100x100":"(.*?)"', line)

            # find headline
            headline = re.findall(r'"headline":"(.*?)"', line)

            # find num_of_subscribers
            num_of_subscribers = re.findall(r'"headline":".*?","num_subscribers":(\d+?),"caption_locales":', line)

            #  find avg_rating
            avg_rating = re.findall(r'"avg_rating":(.*?),"avg_rating_recent":', line)

            # find course_content_length
            course_content_length = re.findall(r'"content_info_short":"(.*?)",', line)
            course_content_length = [re.search(r'\d+[\.\d]*', time).group() for time in course_content_length]

            # saved into file following the format
            for co_id in range(len(course_id)):
                text = [course_id[co_id], course_title[co_id],
                        image_100x100[co_id], headline[co_id],
                        num_of_subscribers[co_id], avg_rating[co_id],
                        course_content_length[co_id]]
                co_inf = ';;;'.join(text)
                course_info.append(co_inf)

            # The course data will be saved into the course.txt file
            course_file = open("./data/result/course.txt", "w", encoding='utf-8')
            for line in course_info:
                course_file.write(line + '\n')

            course_file.close()

    """
    3.2.4 extract_review_info() This method can get review information
    from the review_data folder. The extracted review info saving format is
    “review_id;;;review_content;;;review_rating;;;course_id”
    The course id can be obtained from each file’s name in the 
    review_data folder.
    """

    def extract_review_info(self):
        review_info = []
        # find review_data file path
        for file in os.listdir('./data/review_data'):
            review_path = './data/review_data/' + file

            # read json files
            with open(review_path, "r", encoding='utf-8') as review_file:
                review_list = review_file.read()

            # find review_id
            review_id = re.findall(r'"_class": "course_review", "id": (\d+?),', review_list)

            # find review_content
            review_content = review_content = re.findall(r'"content": "(.*?)", "rating":', review_list)

            # find review_rating
            review_rating = re.findall(r'"rating": (.*?), "created":', review_list)


            # The extracted review info saving format
            for co_id in range(len(review_id)):
                text = [review_id[co_id], review_content[co_id],
                        review_rating[co_id],
                        file[:-5]]
                review_str = ';;;'.join(text)
                review_info.append(review_str)

        # save review_info into review.txt
        with open("./data/result/review.txt", "w", encoding='utf-8') as review_save:
            review_save.write('\n'.join(review_info))


    """
    3.2.5 extract_students_info() This method can get student information 
    from the review_data folder. Each review string contains one user 
    information. Assume each user only has one review. The attributes of 
    each student are id, username, password, user_title, user_image_50x50,
    user_initials and review_id. If a student’s id cannot be found in the 
    string, you need to generate it by calling the generate_unique_user_id() 
    method defined in the User class. The username should be generated by 
    converting the user_title to lowercase and replacing all the whitespace 
    to underscore. The password is generated by converting user_initials to 
    lowercase and combining the user id. The password expression looks like 
    “user_initials + user_id + user_initials”. User_initials can be obtained 
    from the review data. For example, user_id is 12345, user initials is “DE”,
    the password is “de12345de”. The student info will be written into file
    user_student.txt and the format example is:
    “id;;;username;;;password;;;user_title;;;user_image_50x50;;;user_initials;;;review_id” 
    """

    def extract_students_info(self):
        student_info = []
        # find review_data file path
        for file in os.listdir('./data/review_data'):
            student_path = './data/review_data/' + file

            # read json files
            with open(student_path, "r", encoding='utf-8') as student_file:
                student_list = student_file.read()

            # find review_id
            review_id = re.findall(r'"_class": "course_review", "id": (\d+?),', student_list)
            students = re.findall(r'"user_modified": .*?, "user": \{(.*?)\},', student_list)

            for idx in range(len(students)):
                if re.search(r'"id": (\d+)', students[0]):
                    student_id = re.search(r'"id": (\d+)', students[idx]).group(1)
                else:
                    student_id = User.generate_unique_user_id(self)

                student_id = str(student_id)
                student_name = re.search(r'"display_name": "(.*?)"', students[idx]).group(1)
                student_name = student_name.lower().replace(' ', '_')
                student_initials = re.search(r'"initials": "(.*?)"', students[idx]).group(1)
                student_password = student_initials.lower() + student_id+ student_initials.lower()
                student_password = self.encryption(student_password)
                student_image_50x50 = re.search(r'"image_50x50": "(.*?)"', students[idx]).group(1)
                student_title = re.search(r'"title": "(.*?)"', students[idx]).group(1)
                text = ';;;'.join([student_id, student_name, student_password, student_title,
                                   student_image_50x50, student_initials, review_id[idx]])
                student_info.append(text)
        with open('./data/result/user_student.txt', "w", encoding='utf-8') as file:
            file.write('\n'.join(student_info))


    """
    3.2.6 extract_instructor_info()This method extracts information from 
    the raw_data.txt file in the course_data folder.Each course item contains
    several instructor information. The username is generated by converting 
    the instructor_display_name to lowercase and replacing all the whitespace 
    to underscore. The password uses the instructor id directly. The instructor 
    info saving format example is:
    “id;;;username;;;password;;;display_name;;;job_title;;;
    image_100x100;;;course_id1–course_id2–course_id3–course_id4” .
    Since each instructor can teach more than one course, before saving the 
    instructor information, you need to check whether the instructor already exists 
    in the user_instructor.txt file or not. If it exists, the course id should be 
    appended to the existing instructor string. For example, given an instructor string:
    If a new course id 55555 is teached by this instructor, the string will be updated as
    below:The format of instructor data will be explained in the Instructor class section.
    """

    def extract_instructor_info(self):
        # read user_instructor.txt
        with open("./data/result/user_instructor.txt",encoding='utf-8') as instructor_file:
            instructor_list = [line.strip().split(';;;') for line in instructor_file.readlines()]

        # build instructor_dict
        instructor_dict = {}
        for instructor in instructor_list:
            instructor_info = {}
            instructor_info['id'] = instructor[0]
            instructor_info['password'] = instructor[2]
            instructor_info['display_name'] = instructor[3]
            instructor_info['job_title'] = instructor[4]
            instructor_info['image_100x100'] = instructor[5]
            instructor_info['course'] = instructor[6].split('-')
            instructor_dict[instructor[1]] = instructor_info

        # read raw_data.txt
        with open("./data/course_data/raw_data.txt", "r", encoding='utf-8') as raw_file:
            raw_list = raw_file.read()

        # find all course_id
        course_id = re.findall(r'"course","id":(\d+?),', raw_list)

        # extracts instructor information from the raw_data.txt file
        instructor_extracted = re.findall(r'"visible_instructors":\[\{.*?\}\],', raw_list)

        for i in range(len(instructor_extracted)):
            if len(re.findall(r'"id":(\d+?)', instructor_extracted[i])) > 1:
                # find instructor_id
                instructor_id = re.findall(r'"id":(\d+)', instructor_extracted[i])

                # instructor_username   converting the instructor_display_name
                # to lowercase and replacing all the whitespace  to underscore
                instructor_username = re.findall(r'"display_name":"(.*?)"', instructor_extracted[i])
                instructor_username = [username.lower().replace(' ', '_') for username in instructor_username]

                # The instructor_password uses the instructor id directly
                # instructor_password = [ids for ids in instructor_id]
                instructor_password = [self.encryption(ids) for ids in instructor_id]

                # find instructor_display_name
                instructor_display_name = re.findall(r'"display_name":"(.*?)"', instructor_extracted[i])

                # find instructor_job_title
                instructor_job_title = re.findall(r'"job_title":"(.*?)"', instructor_extracted[i])

                # find instructor_image_100x100
                instructor_image_100x100 = re.findall(r'"image_100x100":"(.*?)"', instructor_extracted[i])

                # instructor_course_id
                instructor_course_id = course_id[i]

                for idx in range(len(instructor_id)):
                    if instructor_username[idx] not in instructor_dict:
                        instructor_info = {}
                        instructor_info['id'] = instructor_id[idx]
                        instructor_info['password'] = instructor_password[idx]
                        instructor_info['display_name'] = instructor_display_name[idx]
                        instructor_info['job_title'] = instructor_job_title[idx]
                        instructor_info['image_100x100'] = instructor_image_100x100[idx]
                        instructor_info['course'] = [instructor_course_id]
                        instructor_dict[instructor_username[idx]] = instructor_info

                    else:
                        instructor_dict[instructor_username[idx]]['course'].append(instructor_course_id)
            else:
                # find instructor_id
                instructor_id = re.search(r'"id":(\d+)', instructor_extracted[i])[1]

                # instructor_username   converting the instructor_display_name
                # to lowercase and replacing all the whitespace  to underscore
                instructor_username = re.search(r'"display_name":"(.*?)"', instructor_extracted[i])[1]
                instructor_username = instructor_username.lower().replace(' ', '_')

                # The instructor_password uses the instructor id directly
                instructor_password = self.encryption(instructor_id)

                # find instructor_display_name
                instructor_display_name = re.search(r'"display_name":"(.*?)"', instructor_extracted[i])[1]

                # find instructor_job_title
                instructor_job_title = re.search(r'"job_title":"(.*?)"', instructor_extracted[i])[1]

                # find instructor_image_100x100
                instructor_image_100x100 = re.search(r'"image_100x100":"(.*?)"', instructor_extracted[i])[1]

                # instructor_course_id
                instructor_course_id = course_id[i]

                if instructor_username not in instructor_dict:
                    instructor_info = {}
                    instructor_info['id'] = instructor_id
                    instructor_info['password'] = instructor_password
                    instructor_info['display_name'] = instructor_display_name
                    instructor_info['job_title'] = instructor_job_title
                    instructor_info['image_100x100'] = instructor_image_100x100
                    instructor_info['course'] = [instructor_course_id]
                    instructor_dict[instructor_username] = instructor_info

                else:
                    instructor_dict[instructor_username]['course'].append(instructor_course_id)

        with open('./data/result/user_instructor.txt', "w", encoding='utf-8') as instructor_file:
            for key, value in instructor_dict.items():
                text = ';;;'.join([value['id'], key, value['password'],
                                   value['display_name'], value['job_title'],
                                   value['image_100x100'], '-'.join(value['course'])
                                   ]) + '\n'
                instructor_file.write(text)

    """
    3.2.7 extract_info() This method calls all the extract info methods defined before, 
    including extract_course_info(), extract_instructor_info(), extract_students_info() 
    and extract_review_info().
    """

    def extract_info(self):
        self.extract_course_info()
        print('course information already extract into course.txt')

        self.extract_instructor_info()
        print('instructor information already extract into user_instructor.txt')

        self.extract_students_info()
        print('students information already extract into user_student.txt')

        self.extract_review_info()
        print('review information already extract into review.txt')


    """
    3.2.7 remove_data() This method can delete all the data in the course.txt, review.txt, 
    user_student.txt and user_instructor.txt files.
    """

    def remove_data(self):
        # delete all the data in course.txt files
        open("./data/result/course.txt", "w", encoding = 'utf-8').close()
        # delete all the data in review.txt files
        open("./data/result/review.txt", "w", encoding = 'utf-8').close()
        # delete all the data in user_student.txt files
        open("./data/result/user_student.txt", "w", encoding = 'utf-8').close()
        # delete all the data in user_instructor.txt files
        open("./data/result/user_instructor.txt", "w", encoding = 'utf-8').close()


    """
    3.2.8 view_courses(args=[]) This method will call the methods implemented in Course 
    class to perform various view course methods. The variable “args” can be an empty list 
    or must contain two elements. The first element is the command(can only be
    “TITLE_KEYWORD/ID/INSTRUCTOR_ID”) and the second element is the value(could be title keyword, 
    course id or instructor id). For example, args=[“TITLE_KEYWORD”,“web”]. If the “args” is an 
    empty list, printing out the overview of courses (using the course_overview method implemented 
    in Course class). Add validations to provide proper output message if user input 
    incorrect command or values.
    """

    def view_courses(self,args=[]):
        # This method will call the methods implemented in Course class to
        # perform various view course methods.
        if args:
            # The first element is the command(can only be
            #     “TITLE_KEYWORD/ID/INSTRUCTOR_ID”)

            if args[0] == 'TITLE_KEYWORD':
                i = 0
                course_list = Course.find_course_by_title_keyword(self,args[1])
                for course in course_list:
                    i = i + 1
                    if i < 11:
                        print(course)
                print(f'search course result number is: {i}')

            elif args[0] == 'ID':
                course_list = Course.find_course_by_id(self,args[1])
                print(course_list)

            elif args[0] == 'INSTRUCTOR_ID':
                i = 0
                course_list = Course.find_course_by_instructor_id(self,args[1])
                for course in course_list:
                    i = i + 1
                    if i < 11:
                        print(course)
                print(f'search course result number is: {i}')

            else:
                print('Invalid input command or values! Please check')
                course_list = Course.courses_overview(self)
                print(course_list)

        # If the “args” is an empty list, printing out the overview of courses
        # (using the course_overview method implemented in Course class)
        else:
            course_list = Course.courses_overview(self)
            print(course_list)


    """
    3.2.9 view_users() This method prints out the total number of admin, instructor 
    and students separately with proper description messages
    """

    def view_users(self):
        # prints out the total number of admin
        with open("./data/result/user_admin.txt",encoding='utf-8') as admin_file:
            admin_list = admin_file.readlines()
        print(f'admin account total number is: {len(admin_list)}')

        # prints out the total number of instructor
        with open("./data/result/user_instructor.txt", encoding='utf-8') as instructor_file:
            instructor_list = instructor_file.readlines()
        print(f'instructor account total number is: {len(instructor_list)}')

        # prints out the total number of admin
        with open("./data/result/user_student.txt",encoding='utf-8') as student_file:
            student_list = student_file.readlines()
        print(f'student account total number is: {len(student_list)}')

    """
    3.2.10 view_reviews(args=[])This method will call the methods implemented 
    in Review class to perform various view review methods. The args list can 
    be empty or must contain two elements. The first element is the command
    (can only be “ID/KEYWORD/COURSE_ID”) and the second element is the value
    (could be review id, review keyword or course id). If the args is an empty list, 
    print out the overview of reviews(using the review_overview method implemented 
    in Review class); Add validations to provide proper output message if user 
    input incorrect command or values.
    """

    def view_reviews(self,args=[]):
        # This method will call the methods implemented in Course class to
        # perform various view course methods.
        if args:
            # The first  (can only be “ID/KEYWORD/COURSE_ID”)
            # second  (could be review id, review keyword or course id).

            if args[0] == 'ID':
                review_list = Review.find_review_by_id(self,args[1])
                print(review_list)

            elif args[0] == 'KEYWORD':
                review_list = Review.find_review_by_keywords(self,args[1])
                i = 0
                for review in review_list:
                    i = i + 1
                    if i <11:
                        print(review)
                print(f'search review result number is: {i}')

            elif args[0] == 'COURSE_ID':
                review_list = Review.find_review_by_course_id(self,args[1])
                i = 0
                for review in review_list:
                    i = i +1
                    if i <11:
                        print(review)
                print(f'search review result number is: {i}')

            else:
                print('Invalid !')
                review_list = Review.reviews_overview(self)
                print(review_list)

        #  If the args is an empty list,  print out the overview of reviews
        #  (using the review_overview method implemented in Review class);
        else:
            review_list = Review.reviews_overview(self)
            print(review_list)

    """
    3.2.11 __str__() Since the Admin class does not have any instance variables 
    different from the User class, you can use the parent 
    class’s __str__ method directly.
    """

    def __str__(self):
        User.__str__(self)