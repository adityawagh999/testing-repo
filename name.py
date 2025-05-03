import datetime

def say_hello(name):
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    return f"{greeting}, {name}! Welcome to GitHub."

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(say_hello(name))