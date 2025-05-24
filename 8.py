import logging

# 1 - dz
from datetime import date
now = date.today()
logging.basicConfig(level=logging.INFO)
logging.info(now.strftime("%Y-%m-%d"))

print("============================================================")

# 2
print("Math test")
one = 2**10
answer_one = int(input("2^10 = "))
if answer_one != one:
    logging.error(f"Nah, it's {one}")

print("============================================================")

# 3
def login(username, password):
    correct_username = "AaronWarnerAnderson"
    correct_password = "ffashH1on1stA"
    try:
        assert username == correct_username and password == correct_password, "Smth is wrong"
        print("Perfect")
    except AssertionError as e:
        print(e)
user = input("Input name: ")
pwd = input("Input password: ")
login(user, pwd)

print("============================================================")

# 4
def check(age):
    try:
        age = int(age)
        assert age >= 18, "Naughty baby, you're not allowed"
        print("It's alright")
    except ValueError:
        print("It must be a number?")
    except AssertionError as e:
        print(e)

age_input = input("Input your age: ")
check(age_input)

print("============================================================")

# 5
def process_list(input_list):
    try:
        assert len(input_list) >= 3, "It must contain at least 3 items"
        print(f"It contains {len(input_list)} items")
    except AssertionError as e:
        print(e)
process_list([1, 2, 3])
process_list([10, 20])
process_list([])