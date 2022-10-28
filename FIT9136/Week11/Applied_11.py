def reminder(func):
    func()
    print("Dont forget....")

def action():
    print("I want to buy sth")

# call reminder here
reminder(action)
action()