from datetime import datetime

def log_start(func_name):
    print(func_name + " action starts at " + str(datetime.now()))

def log_end(func_name):
    print(func_name + " action ends at " + str(datetime.now()))

def login():
    print("this is login")

def logout():
    print("this is logout")

# log_start("login")
# login()
# log_end("login")
#
# log_start("logout")
# logout()
# log_end("logout")

def logs(func):
    def wrapper():
        print(func.__name__ + " action start at " + str(datetime.now()))
        func()
        print(func.__name__ + " action end at " + str(datetime.now()))
    return wrapper
@logs
def login1():
    print("this is login")

@logs
def logout2():
    print("this is logout")

login1()
logout2()