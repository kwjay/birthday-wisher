import random
import pandas
import datetime as dt

LETTERS_PATHS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
SENDER_NAME = "Jakub"


def format_letter(celebrant_name):
    letter_file = random.choice(LETTERS_PATHS)
    with open(f"letter_templates/{letter_file}") as file:
        letter = file.read()
    letter.replace("[NAME]", celebrant_name)
    letter.replace("[SENDER]", SENDER_NAME)
    return letter


def send_birthday_wishes(celebrant):
    pass


data_file = pandas.read_csv("birthdays.csv")
data = data_file.to_dict(orient="records")
today = dt.datetime.now()

for person in data:
    if person["month"] == today.month and person["day"] == today.day:
        send_birthday_wishes(celebrant=person)

# 4. Send the letter generated in step 3 to that person's email address.




