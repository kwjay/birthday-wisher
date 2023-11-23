import random
import pandas
import datetime as dt
import smtplib

LETTERS_PATHS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
SENDER_NAME = "sender name"
SENDER_EMAIL = "sender@gmail.com"
SENDER_PASSWORD = "password"
PROVIDER_SMTP = "smtp.gmail.com"
PROVIDER_PORT = 587


def format_letter(celebrant_name):
    letter_file = random.choice(LETTERS_PATHS)
    with open(f"letter_templates/{letter_file}") as file:
        letter = file.read()
    letter = letter.replace("[NAME]", celebrant_name)
    letter = letter.replace("[SENDER]", SENDER_NAME)
    return letter


def send_birthday_wishes(celebrant):
    with smtplib.SMTP(PROVIDER_SMTP, PROVIDER_PORT) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        celebrant_name = celebrant["name"]
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=celebrant["email"],
            msg=f"Subject:HAPPY BIRTHDAY {celebrant_name}\n\n{format_letter(celebrant_name)}"
        )


data_file = pandas.read_csv("birthdays.csv")
data = data_file.to_dict(orient="records")
today = dt.datetime.now()

for person in data:
    if person["month"] == today.month and person["day"] == today.day:
        send_birthday_wishes(celebrant=person)
