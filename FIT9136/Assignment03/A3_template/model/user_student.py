from model.user import User


class Student(User):
    """
    3.2.4 Student class
    1. constructor. Six positional arguments: uid(int, default value is -1),
    username(str, default value is “”), password(str, default value is “”),
    register_time(str, default value is “yyyy-MM-dd_HH:mm:ss.SSS”),
    role(str, default value is “student”), email(str,default value is “”)
    """

    def __init__(self, uid=-1, username="", password="", register_time="yyyy-MM-dd_HH:mm:ss.SSS",
                 role="student", email=""):
        User.__init__(self, uid, username, password, register_time, role)
        self.email = email

    """
    2. __str__()->str.
    Return string format example:
    """

    def __str__(self):
        text = ';;;'.join([str(self.uid), self.username, self.password,
                           self.register_time, self.role, self.email])
        return text

    """
    3. get_students_by_page()->tuple.   One positional argument: page. 
    This method reads the user.txt file to retrieve all the student information. 
    With all the student information and the current page number, a list of 
    Student objects and the total pages will be generated. Each page has at 
    most 20 students. A tuple contains the list of students, total page number 
    and the total number of students will be returned.
    """

    def get_students_by_page(self, page):
        student_obj_list = []
        with open("data/temp_stu.txt", encoding='utf-8') as student_file:
            student_list = [line.strip().split(';;;') for line in student_file.readlines()]
        total_page = int(len(student_list) / 20)
        # uid=-1, username="", password="", register_time="yyyy-MM-dd_HH:mm:ss.SSS",
        #                  role="student", email=""
        for line in student_list:
            student_obj_list.append(Student(int(line[0]),line[1],line[2],
                                            line[3],line[4],line[5]))

        if page < total_page:
            student_content = student_obj_list[(page - 1) * 20:page * 20]
        else:
            student_content = student_obj_list[(page - 1) * 20:]
        return (student_content, total_page, len(student_list))

        # student_dict = {}
        # uid = User().generate_unique_user_id()
        # student_dict[uid] = [uid, self.username, self.password,
        #                    self.register_time, self.role,self.email]
        #
        # # write student data into temp_stu.txt file
        # # with open(user_data_path, "a", encoding='utf-8') as json_file:
        # with open("data/temp_stu.txt", "w", encoding='utf-8') as json_file:
        #     for key, value in student_dict.items():
        #         test = key + ';;;' + ';;;'.join(value)
        #         json_file.write(test + '\n')

    """
    4. get_student_by_id()->Student object One positional argument id. 
    This method returns a student object by retrieving the id from the 
    user.txt file
    """

    def get_student_by_id(self, student_id):
        with open("data/user.txt", encoding='utf-8') as student_file:
            student_list = [line.strip().split(';;;') for line in student_file.readlines()]

        for student in student_list:
            if str(student[0]) == str(student_id):
                return Student(int(student[0]), student[1], student[2],
                               student[3], student[4], student[5])

    """
    5. delete_student_by_id()->bool One positional argument id. 
    This method deletes a student item from the user.txt file based on the given id.
    """

    def delete_student_by_id(self, student_id):
        delete_result = False
        with open("data/temp_stu.txt", encoding='utf-8') as student_file:
            student_list = [line.strip().split(';;;') for line in student_file.readlines()]

        with open("data/temp_stu.txt", "w", encoding='utf-8') as student_file:
            for student in student_list:
                if str(student[0]) != str(student_id):
                    text = ';;;'.join([student[0], student[1], student[2],
                                       student[3], student[4], student[5]])
                    student_file.write(text + '\n')
                    User().txt_merge()
                else:
                    delete_result = True
        return delete_result
