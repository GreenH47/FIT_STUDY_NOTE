class Review:
    """
    3.6.1 constructor The attributes of review are id(int, default value -1),
    content(str, default value “”),rating(float, default value -1.0),
    course_id(int, default value -1).
    """

    def __init__(self, _id=-1, content="",rating=-1.0,course_id=-1):
        self._id = _id
        self.content = content
        self.rating = rating
        self.course_id= course_id

    """
    3.6.2 find_review_by_id(review_id) This method has a positional argument 
    review id(int or srt). It finds the review information based on the given 
    id from the review.txt file. A review object will be returned. 
    If not found, return None.
    """

    def find_review_by_id(self, review_id):
        with open("./data/result/review.txt", "r", encoding='utf-8') as review_file:
            review_list = [line.strip().split(';;;') for line in review_file.readlines()]

        for review in review_list:
          if review_id == review[0]:
              return Review(review[0], review[1], review[2], review[3])

    """
    3.6.3 find_review_by_keywords(keyword) This method has a positional argument 
    keyword(str). It finds the reviews whose content contains the given keyword from 
    the review.txt file. A list of review objects will be generated and returned. 
    The result list looks like [Review(), Review(),Review()….]. 
    If not found, return an empty list. The keyword cannot be empty
    """

    def find_review_by_keywords(self, keyword):
        with open("./data/result/review.txt", encoding='utf-8') as review_file:
            review_list = [line.strip().split(';;;') for line in review_file.readlines()]

        # Based on the given keyword, it searches the course title of all review in the
        # review.txt file to find the result.
        review_search = []
        for review in review_list:
            if keyword in review[1]:
                review_search.append(review)

        #All the result review will be created as a review object and
        # added into a result list
        review_content = []
        for review in review_search:
            review_content.append( Review(review[0],review[1],review[2],review[3]))
        return review_content


    """
    3.6.4 find_review_by_course_id(course_id)This method has a positional argument 
    course id(int or str). It finds the reviews that belong to the given course id. 
    A list of review objects will be generated and returned. The result list looks 
    like [Review(), Review(), Review()….]. If not found, return an empty list.
    """

    def find_review_by_course_id(self, course_id):
        with open("./data/result/review.txt", encoding='utf-8') as review_file:
            review_list = [line.strip().split(';;;') for line in review_file.readlines()]

        # It finds the reviews that belong to the given course id
        review_search = []
        for review in review_list:
            if course_id == review[3]:
                review_search.append(review)

        # All the result courses will be created as a course object and
        # added into a result list
        review_content = []
        for review in review_search:
            review_content.append(Review(review[0], review[1], review[2],review[3]))
        return review_content


    """
    3.6.5 reviews_overview() This method returns a string that shows the total number of reviews.
    """

    def reviews_overview(self):
        initial_file = open("./data/result/review.txt", 'a+', encoding='utf-8')
        initial_file.close()
        with open("./data/result/review.txt",encoding='utf-8') as review_file:
            review_list = review_file.readlines()
        text = f'The total number of reviews is {len(review_list)}'
        return text

    """
    3.6.6 __str__() Return a string containing all review attributes
    _id=-1, content='',rating=-1.0,course_id=-1
    """

    def __str__(self):
        text = f'Review id: {self._id}\nReview content: {self.content}\n' \
               f'Review rating: {self.rating}\nCourse id: {self.course_id}\n'
        return text