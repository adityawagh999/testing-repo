# hello.py

import datetime
import random

def say_hello(name):
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    
    return f"{greeting}, {name}! Welcome to GitHub."

def get_motivational_quote():
    quotes = [
        "Keep pushing forward!",
        "You're doing great — don't stop!",
        "Every day is a new opportunity.",
        "Believe in yourself!",
        "Stay positive, work hard, and make it happen."
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(say_hello(name))
    print(get_motivational_quote())
