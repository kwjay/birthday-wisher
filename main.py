import smtplib

sender_email = "email@gmail.com"
sender_password = "password"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=sender_email, password=sender_password)
connection.sendmail(
    from_addr=sender_email,
    to_addrs="birthday_guy@gmail.com",
    msg="Subject:Hello\n\nHello"
)
connection.close()
