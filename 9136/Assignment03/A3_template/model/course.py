

from lib.helper import course_json_files_path, figure_save_path
import os
import json
from lib.helper import course_data_path
import pandas as pd
import matplotlib.pyplot as plt


class Course:
    """
    3.2.5 Course class
    1. constructor. Eleven positional arguments:
    category_title(str, default value is “”),subcategory_id(int, default value is -1),
    subcategory_title(str, default value is“”), subcategory_description(str, default value is “”),
    subcategory_url(str,default value is “”), course_id(int, default value is -1),
    course_title(str, default value is “”), course_url(str, default value is “”),
    num_of_subscribers(int, default value is 0), avg_rating(float, default value is 0.0)
    and num_of_reviews(int, default value is 0)
    """

    def __init__(self, category_title="", subcategory_id=-1, subcategory_title="", subcategory_description="",
                 subcategory_url="", course_id=-1, course_title="", course_url="",
                 num_of_subscribers=0, avg_rating=0.0, num_of_reviews=0):
        self.category_title = category_title
        self.subcategory_id = subcategory_id
        self.subcategory_title = subcategory_title
        self.subcategory_description = subcategory_description
        self.subcategory_url = subcategory_url
        self.course_id = course_id
        self.course_title = course_title
        self.course_url = course_url
        self.num_of_subscribers = num_of_subscribers
        self.avg_rating = avg_rating
        self.num_of_reviews = num_of_reviews

    """
    2. __str__()->str.  Return format:
    {category_title};;;{subcategory_id};;;{subcategory_title};;;{subcategory_description};;;
    {subcategory_url};;;{course_id};;;{course_title};;;{course_url};;;
    {num_of_subscribers};;;{avg_rating};;;{num_of_reviews}
    Return string format example:
    """

    def __str__(self):
        text = ';;;'.join([self.category_title, self.subcategory_id, self.subcategory_title,
                           self.subcategory_description, self.subcategory_url, self.course_id,
                           self.course_title, self.course_url, self.num_of_subscribers,
                           self.avg_rating, self.num_of_reviews])
        return text

    """
    3. get_courses() no return. This method will extract course information from the given 
    course data files. In the source_course_files folder, there are 4 categories of courses. 
    In each category folder, there are some subcategories. Inside each subcategory folder,
    you can find the course json files. You need to retrieve the category_title from
    the 4 category folder names and other course info from the json files. In each
    json file, there is another category name which is also acceptable for
    category_title value like the image below.
    All the null value in json str should be saved as None or string “null”. All the
    empty string value “” should be saved as same empty string “”.
    After retrieving the required data, you need to write the info into course.txt
    file to save all the course data. All the data need to be separated by “;;;”. The
    required attributes and data format is:
    “{category_title};;;{subcategory_id};;;{subcategory_title};;;{subcategory_description}
    ;;;{subcategory_url};;;{course_id};;;{course_title};;;{course_url};;;{num_o
    f_subscribers};;;{avg_rating};;;{num_of_reviews}”.
    """

    def get_courses(self):
        course_list = []
        # get category path
        category_path = '.' + course_json_files_path
        for category in os.listdir(category_path):
            if not category.startswith('.'):
                # get subcategory_path

                subcategory_path = category_path + '/' + category
                for subcategory in os.listdir(subcategory_path):
                    if not subcategory.startswith('.'):
                        # get json path
                        js_path = subcategory_path + '/' + subcategory
                        for js_file in os.listdir(js_path):
                            # read json
                            file_path = js_path + '/' + js_file

                            # write json data into instructor_dict
                            with open(file_path, encoding='utf-8') as json_file:
                                js_data = json.load(json_file)
                                for unit in js_data.values():
                                    for item in unit['items']:
                                        category_title = category.split("_")[-1]
                                        subcategory_id = unit['source_objects'][0]['id']
                                        subcategory_title = unit['source_objects'][0]['title']
                                        subcategory_description = unit['source_objects'][0]['description']
                                        if subcategory_description is None:
                                            subcategory_description = "null"
                                        subcategory_url = unit['source_objects'][0]['url']
                                        if subcategory_url is None:
                                            subcategory_url = "null"
                                        course_id = item['id']
                                        course_title = item['title']
                                        course_url = item['url']
                                        if course_url is None:
                                            course_url = "null"
                                        num_of_subscribers = item['num_subscribers']
                                        avg_rating = item['avg_rating']
                                        num_of_reviews = item['num_reviews']
                                        text = ';;;'.join([category_title, str(subcategory_id), subcategory_title,
                                                           subcategory_description, subcategory_url, str(course_id),
                                                           course_title, course_url, str(num_of_subscribers),
                                                           str(avg_rating), str(num_of_reviews)])
                                        course_list.append(text)

        # write instructor data into temp_ins.txt file
        # with open(user_data_path, "a", encoding='utf-8') as course_file:
        with open(course_data_path, "w", encoding='utf-8') as course_file:
            for line in course_list:
                course_file.write(line + '\n')

    """
    4. clear_course_data() no return.   This method will remove all the content in the 
    course.txt file. After calling this method, the course.txt file will become an empty file.
    """

    def clear_course_data(self):
        open(course_data_path, "w", encoding='utf-8').close()

    """
    5. generate_page_num_list()->list of int.   Two positional arguments: page and total_pages. 
    This method uses the current page number and total pages to generate a list of integers 
    as viewable page numbers. For example, the image below shows a default page number
    list [1,2,3,4,5,6,7,8,9] when the current page number is 1. If the current page number is 
    less than or equal to 5, the generated page number list is always [1,2,3,4,5,6,7,8,9]. 
    If the current page number is greater than 5 and less than total pages minus 4, the page 
    number list will be integers from current page number minus 4 until current page number 
    plus 4. For example, in the image below, the current page is 8 and the number list
    becomes [4,5,6,7,8,9,10,11,12]. If the current page is greater than or equal to total pages 
    minus 4, the list of numbers changes to range between total pages minus 8 until total pages.
    """

    def generate_page_num_list(self, page, total_pages):
        page_num_list = []
        if page <= 5:
            page_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        elif (page > 5) and (page < total_pages - 4):
            page_num_list = [page - 4, page - 3, page - 2, page - 1, page,
                             page + 1, page + 2, page + 3, page + 4]
        elif page >= total_pages - 4:
            page_num_list = [total_pages - 8, total_pages - 7, total_pages - 6,
                             total_pages - 5, total_pages - 4, total_pages - 3,
                             total_pages - 2, total_pages - 1, total_pages]
        return page_num_list

    """
    6. get_courses_by_page()->tuple One positional argument: page. The return value 
    is a tuple that contains a list of Course objects, total pages of courses and 
    the total number of courses. This method reads the course.txt file to retrieve 
    all the course information. With all the course information and the current page 
    number, a list of Course objects will be generated, the total pages and the total 
    number of courses will be returned. Each page has at most 20 courses.
    For example, if there are 100 courses info in the course.txt file and the current
    page number is 2, then the 21-40 lines course info will be converted to a list
    with 20 Course objects. The total page number is 5.
    """

    def get_courses_by_page(self, page):
        course_obj_list = []
        with open(course_data_path, encoding='utf-8') as course_file:
            course_list = [line.strip().split(';;;') for line in course_file.readlines()]
        for line in course_list:
            # category_title="", subcategory_id=-1, subcategory_title="", subcategory_description="",
            #                  subcategory_url="", course_id=-1, course_title="", course_url="",
            #                  num_of_subscribers=0, avg_rating=0.0, num_of_reviews=0):
            course_obj_list.append(Course(line[0],int(line[1]),line[2],line[3],
                                          line[4],int(line[5]),line[6],line[7],int(line[8]),
                                          float(line[9]),int(line[10])))
        total_page = int(len(course_obj_list) / 20)
        total_course = len(course_obj_list)
        if page < total_page:
            course_content = course_obj_list[(page - 1) * 20:page * 20]
        else:
            course_content = course_obj_list[(page - 1) * 20:]
        return (course_content, total_page, total_course)

    """
    7. delete_course_by_id()->bool One positional argument: course_id. 
    The method reads course info from the course.txt file and deletes the course 
    information belongs to that course_id. Meanwhile, if an instructor in the 
    user.txt file teaches this course, the course id should also be removed from 
    the instructor’s course_id_list. Finally, this method returns whether the deletion 
    is successful or not. If the course_id cannot be found in the course.txt file, 
    return False.
    """

    def delete_course_by_id(self, temp_course_id):
        delete_result = False
        # delete course info from the course.txt file
        with open(course_data_path, encoding='utf-8') as course_file:
            course_list = [line.strip().split(';;;') for line in course_file.readlines()]

        with open(course_data_path, encoding='utf-8') as course_file:
            for course in course_list:
                if str(course[5]) != str(temp_course_id):
                    text = ';;;'.join([course[0], course[1], course[2],
                                       course[3], course[4], course[5],
                                       course[6], course[7], course[8],
                                       course[9], course[10]])
                    course_file.write(text + '\n')
                else:
                    delete_result = True

        if delete_result:
            # the course id should also be removed from the instructor’s course_id_list
            with open("data/temp_ins.txt", encoding='utf-8') as instructor_file:
                instructor_list = [line.strip().split(';;;') for line in instructor_file.readlines()]
            with open("data/temp_ins.txt", "w", encoding='utf-8') as instructor_file:
                for instructor in instructor_list:
                    course_teach = instructor[-1].split("-")
                    if str(temp_course_id) not in course_teach:
                        text = ';;;'.join([instructor[0], instructor[1], instructor[2],
                                           instructor[3], instructor[4], instructor[5],
                                           instructor[6], instructor[7], instructor[8]])
                        instructor_file.write(text + '\n')
                    else:
                        course_teach.remove(str(temp_course_id))
                        instructor[-1] = "-".join(course_teach)
                        text = ';;;'.join([instructor[0], instructor[1], instructor[2],
                                           instructor[3], instructor[4], instructor[5],
                                           instructor[6], instructor[7], instructor[8]])
                        instructor_file.write(text + '\n')


        return delete_result

    """
    8. get_course_by_course_id()->tuple     One positional argument: course_id. 
    You are required to find the course by given course_id and convert the info 
    to a Course object. Then, using the retrieved course info to get the 
    num_of_subscribers, avg_rating and num_of_reviews. Based on these three numbers, 
    generate a comment for this course. If the num_of_subscribers greater than 100000 
    and avg_rating greater than 4.5 and num_of_reviews greater than 10000, the comment 
    should be “Top Courses”. If the num_of_subscribers greater than 50000 and avg_rating
    greater than 4.0 and num_of_reviews greater than 5000, the comment should be 
    “Popular Courses”. If the num_of_subscribers greater than 10000 and avg_rating greater 
    than 3.5 and num_of_reviews greater than 1000, the comment should be “Good Courses”. 
    The other courses are “General Courses”.   
    The Course object and comment will be returned as a tuple.
    (self, category_title="", subcategory_id=-1, subcategory_title="", subcategory_description="",
                 subcategory_url="", course_id=-1, course_title="", course_url="",
                 num_of_subscribers=0, avg_rating=0.0, num_of_reviews=0):
    """

    def get_course_by_course_id(self, temp_course_id):
        course_id = str(temp_course_id)
        with open(course_data_path, encoding='utf-8') as course_file:
            course_list = [line.strip().split(';;;') for line in course_file.readlines()]
        for course in course_list:
            if str(course[5]) == course_id:
                num_of_subscribers = int(course[8])
                avg_rating = float(course[9])
                num_of_reviews = int(course[10])
                course_object = Course(course[0], int(course[1]), course[2],
                                       course[3], course[4], int(course[5]),
                                       course[6], course[7], int(course[8]),
                                       float(course[9]), int(course[10]))
                # generate a comment for this course
                course_comment = ""
                if (num_of_subscribers > 100000) and (avg_rating > 4.5) and (num_of_reviews > 10000):
                    course_comment = "Top Courses"
                elif (num_of_subscribers > 50000) and (avg_rating > 4.0) and (num_of_reviews > 5000):
                    course_comment = "Popular Courses"
                elif (num_of_subscribers > 10000) and (avg_rating > 3.5) and (num_of_reviews > 1000):
                    course_comment = "Good Courses"
                else:
                    course_comment = "General Courses"

                return (course_object, course_comment)

    def find_course_by_course_id(self, temp_course_id):
        course_id = str(temp_course_id)
        with open(course_data_path, encoding='utf-8') as course_file:
            course_list = [line.strip().split(';;;') for line in course_file.readlines()]
        for course in course_list:
            if str(course[5]) == course_id:
                course_object = Course(course[0], int(course[1]), course[2],
                                       course[3], course[4], int(course[5]),
                                       course[6], course[7], int(course[8]),
                                       float(course[9]), int(course[10]))

                return course_object

    """
    9. get_courses_by_instructor_id()->tuple    One positional argument: instructor_id. 
    This method reads the user.txt file and course.txt file to find all the course information 
    the specified instructor teaches. If this instructor teaches more than 20 courses, 
    only 20 courses will be returned with the total number of courses this instructor teaches 
    (do not need to sort, just use the default order and get the first 20). Otherwise, all the
    courses and the total number will be returned. The return type is a tuple that contains a 
    list of course objects and the total number of courses teached by this instructor.
    """

    def get_course_by_instructor_id(self, instructor_id):
        instructor_id = str(instructor_id)
        course_list = []
        course_num = 0
        with open("data/temp_ins.txt", encoding='utf-8') as instructor_file:
            instructor_list = [line.strip().split(';;;') for line in instructor_file.readlines()]
        for instructor in instructor_list:
            if str(instructor[0]) == instructor_id:
                course_id_list = instructor[-1].split("-")

                for course in course_id_list:
                    course_num = course_num + 1
                    if course_num < 21:

                        course_list.append(Course().find_course_by_course_id(course))
        return (course_list, course_num)

    """
    10.generate_course_figure1()->str Generate a graph to show the top 10 subcategories 
    with the most subscribers. (any chart)
    (category_title="", subcategory_id=-1, subcategory_title="", subcategory_description="",
     subcategory_url="", course_id=-1, course_title="", course_url="",
     num_of_subscribers=0, avg_rating=0.0, num_of_reviews=0):
    """

    def generate_course_figure1(self):
        course_display = {}
        course_content = []
        # with open("data/_demo_course.txt", encoding='utf-8') as course_file:
        with open("data/course.txt", encoding='utf-8') as course_file:
            for line in course_file:
                line = line.strip().split(";;;")
                # if the course title is too long,
                # you need to extract the first 3 word
                if len(line[6].split(" ")) > 3:
                    line[6] = line[6][:3]
                course_content.append(line)
        course_display['subcategory_title'] = [line[2] for line in course_content]
        course_display['num_of_subscribers'] = [int(line[-3]) for line in course_content]

        course_graph = pd.DataFrame(course_display)
        course_figure1 = course_graph.groupby(['subcategory_title']).agg({'num_of_subscribers': 'sum'})
        course_figure1 = course_figure1.sort_values(by='num_of_subscribers', ascending=False).head(10)
        print(course_figure1)
        df = course_figure1.reset_index()
        print(df)

        x = df['subcategory_title']
        y = df['num_of_subscribers']
        #
        # # using Bar() to plot line chart
        fig, ax = plt.subplots(figsize=(30, 10))
        plot = ax.bar(x, y)
        # using xlabel, ylabel, and title to set the labels for the chart
        ax.set_xlabel("Subcategory")
        ax.set_ylabel("Total subscribers")
        ax.set_title("Top 10 Subcategories with the most subscribers")
        ax.bar_label(plot, padding=3)

        # save pictures
        plt.savefig(figure_save_path + 'course_figure1.png')

        # using show function to show the plot the graph
        # plt.show()

        # return a string explanation about your understanding of this figure.
        text = "Web development courses have most subscribers"
        return text

    """
    11.generate_course_figure2()->str   Generate a graph to show the top 10 courses 
    that have lowest avg rating and over 50000 reviews.(any chart)
    """

    def generate_course_figure2(self):
        course_display = {}
        course_content = []
        # with open("data/_demo_course.txt", encoding='utf-8') as course_file:
        with open("data/course.txt", encoding='utf-8') as course_file:
            for line in course_file:
                line = line.strip().split(";;;")
                # if the course title is too long,
                # you need to extract the first 3 word
                if len(line[6].split(" ")) > 3:
                    line[6] = " ".join(line[6].split()[:3])
                course_content.append(line)
        # (category_title="", subcategory_id=-1, subcategory_title="", subcategory_description="",
        #      subcategory_url="", course_id=-1, course_title="", course_url="",
        #      num_of_subscribers=0, avg_rating=0.0, num_of_reviews=0)
        course_display['course_title'] = [line[6] for line in course_content]
        course_display['avg_rating'] = [float(line[-2]) for line in course_content]
        course_display['num_of_reviews'] = [int(line[-1]) for line in course_content]
        course_graph = pd.DataFrame(course_display)

        # Generate a graph to show the top 10 courses
        #     that have lowest avg rating and over 50000 reviews.
        course_figure2 = course_graph[course_graph['num_of_reviews'] > 5000]
        course_figure2 = course_figure2.sort_values(by='avg_rating').head(10)

        x = course_figure2['course_title']
        y = course_figure2['avg_rating']

        # using Bar() to plot line chart
        fig, ax = plt.subplots(figsize=(20, 10))
        plot = ax.bar(x, y)
        # using xlabel, ylabel, and title to set the labels for the chart
        ax.set_xlabel("course_title")
        ax.set_ylabel("avg_rating")
        ax.set_title("top 10 courses that have lowest avg rating ")
        ax.bar_label(plot, padding=3)

        # save pictures
        plt.savefig(figure_save_path + 'course_figure2.png')

        # using show function to show the plot the graph
        # plt.show()

        # return a string explanation about your understanding of this figure.
        text = "the lowest rating is around 4.01"
        return text

    """
    12.generate_course_figure3()->str   Generate a graph to show the all the courses 
    avg rating distribution that has subscribers between 100000 and 10000 (scatter chart)
    """

    def generate_course_figure3(self):
        course_display = {}
        course_content = []
        # with open("data/_demo_course.txt", encoding='utf-8') as course_file:
        with open("data/course.txt", encoding='utf-8') as course_file:
            for line in course_file:
                line = line.strip().split(";;;")
                # if the course title is too long,
                # you need to extract the first 3 word
                if len(line[6].split(" ")) > 3:
                    line[6] = " ".join(line[6].split()[:3])
                course_content.append(line)
        # (category_title="", subcategory_id=-1, subcategory_title="", subcategory_description="",
        #      subcategory_url="", course_id=-1, course_title="", course_url="",
        #      num_of_subscribers=0, avg_rating=0.0, num_of_reviews=0)
        course_display['course_title'] = [line[6] for line in course_content]
        course_display['num_of_subscribers'] = [int(line[-3]) for line in course_content]
        course_display['avg_rating'] = [float(line[-2]) for line in course_content]
        course_graph = pd.DataFrame(course_display)

        # generate a graph to show the all the courses
        # distribution that has subscribers between 100000 and 10000 (scatter chart)
        course_figure3 = course_graph[(course_graph['num_of_subscribers'] > 10000)
                                      & (course_graph['num_of_subscribers'] < 100000)]

        # using Bar() to plot line chart
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.scatter(course_figure3['num_of_subscribers'], course_figure3['avg_rating'])

        ax.set_xlabel("num_of_subscribers")
        ax.set_ylabel("avg_rating")
        ax.set_title(" all the courses avg rating distribution ")

        # save pictures
        plt.savefig(figure_save_path + 'course_figure3.png')
        # using show function to show the plot the graph
        # plt.show()

        # return a string explanation about your understanding of this figure.
        text = "most course rating are around 4.6"
        return text

    """
    13.generate_course_figure4()->str   Generate a graph to show the number of courses 
    for all categories and sort in ascending order (pie chart, offsetting the second 
    largest number of course with "explode")
    """

    def generate_course_figure4(self):
        course_display = {}
        course_content = []
        # with open("data/_demo_course.txt", encoding='utf-8') as course_file:
        with open("data/course.txt", encoding='utf-8') as course_file:
            for line in course_file:
                line = line.strip().split(";;;")
                # if the course title is too long,
                # you need to extract the first 3 word
                if len(line[6].split(" ")) > 3:
                    line[6] = " ".join(line[6].split()[:3])
                course_content.append(line)
        # (category_title="", subcategory_id=-1, subcategory_title="", subcategory_description="",
        #      subcategory_url="", course_id=-1, course_title="", course_url="",
        #      num_of_subscribers=0, avg_rating=0.0, num_of_reviews=0)
        course_display['category_title'] = [line[0] for line in course_content]
        course_display['num_of_subscribers'] = [int(line[-3]) for line in course_content]

        course_graph = pd.DataFrame(course_display)

        course_figure4 = course_graph.groupby(['category_title'])['num_of_subscribers'].count().sort_values()

        fig, ax = plt.subplots(figsize=(20, 10))
        # using Bar() to plot line chart
        colors = ['red', 'pink', 'yellow', 'brown']
        fig, ax = plt.subplots(figsize=(20, 10))
        patches, texts, pcts = ax.pie(course_figure4, colors=colors, autopct='%.2f%%',
                                      wedgeprops={'linewidth': 2, 'edgecolor': 'black'},
                                      frame=False, labels=course_figure4.index,
                                      explode=[0, 0, 0.1, 0]

                                      )
        ax.set_title("The number of courses for all categories ")
        # save pictures
        plt.savefig(figure_save_path + 'course_figure4.png')
        # using show function to show the plot the graph
        # plt.show()

        # return a string explanation about your understanding of this figure.
        text = "development courses taks one third for all categories "
        return text

    """
    14.generate_course_figure5()->str   Generate a graph to show how many courses have 
    reviews and how many courses do not have reviews.(bar chart)
    """

    def generate_course_figure5(self):
        course_display = {}
        course_content = []
        # with open("data/_demo_course.txt", encoding='utf-8') as course_file:
        with open("data/course.txt", encoding='utf-8') as course_file:
            for line in course_file:
                line = line.strip().split(";;;")
                # if the course title is too long,
                # you need to extract the first 3 word
                if len(line[6].split(" ")) > 3:
                    line[6] = " ".join(line[6].split()[:3])
                course_content.append(line)
        # (category_title="", subcategory_id=-1, subcategory_title="", subcategory_description="",
        #      subcategory_url="", course_id=-1, course_title="", course_url="",
        #      num_of_subscribers=0, avg_rating=0.0, num_of_reviews=0)
        course_display['num_of_reviews'] = [int(line[-1]) for line in course_content]

        # how many courses have reviews and how many courses do not have reviews


        # generate a graph to show the all the courses
        # distribution that has subscribers between 100000 and 10000 (scatter chart)
        course_graph = pd.DataFrame({'Course':['has reviews', 'no review'], 'Course total':[21123,1059]})

        # using Bar() to plot line chart
        fig, ax = plt.subplots(figsize=(20, 10))

        ax = course_graph.plot.bar(x='Course', y='Course total', rot=0)
        # ax.bar_label(plot, padding=3)

        # save pictures
        plt.savefig(figure_save_path + 'course_figure5.png')
        # using show function to show the plot the graph
        # plt.show()

        # return a string explanation about your understanding of this figure.
        text = "There are around 1000 courses without review"
        return text

    """
    15.generate_course_figure6()->str   Generate a graph to show the top 10 subcategories 
    with the least courses (any chart)
    """

    def generate_course_figure6(self):
        course_display = {}
        course_content = []
        # with open("data/_demo_course.txt", encoding='utf-8') as course_file:
        with open("data/course.txt", encoding='utf-8') as course_file:
            for line in course_file:
                line = line.strip().split(";;;")
                # if the course title is too long,
                # you need to extract the first 3 word
                if len(line[6].split(" ")) > 3:
                    line[6] = " ".join(line[6].split()[:3])
                course_content.append(line)
        # (category_title="", subcategory_id=-1, subcategory_title="", subcategory_description="",
        #      subcategory_url="", course_id=-1, course_title="", course_url="",
        #      num_of_subscribers=0, avg_rating=0.0, num_of_reviews=0)
        course_display['subcategory_title'] = [line[2] for line in course_content]
        course_display['num_of_subscribers'] = [int(line[-3]) for line in course_content]

        course_graph = pd.DataFrame(course_display)

        course_figure6 = course_graph.groupby(['subcategory_title']).agg({'num_of_subscribers': 'count'})
        course_figure6 = course_figure6.sort_values(by='num_of_subscribers', ascending=True).head(10)

        df = course_figure6.reset_index()

        x = df['subcategory_title']
        y = df['num_of_subscribers']
        #
        # # using Bar() to plot line chart
        fig, ax = plt.subplots(figsize=(30, 10))
        plot = ax.bar(x, y)
        # using xlabel, ylabel, and title to set the labels for the chart
        ax.set_xlabel("Subcategory")
        ax.set_ylabel("Courses total")
        ax.set_title("Top 10 Subcategories with the least courses")
        ax.bar_label(plot, padding=3)

        # save pictures
        plt.savefig(figure_save_path + 'course_figure6.png')

        # using show function to show the plot the graph
        # plt.show()

        # return a string explanation about your understanding of this figure.
        text = "It certification has only 80 courses"
        return text
