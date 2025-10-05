# Working with smtp to send mails
import smtplib

my_email = 'sahilservice300@gmail.com'
password = 'ldxlnrloejkpxzmt'

with smtplib.SMTP("smtp.gmail.com") as connection :
    connection.starttls()
    connection.login(user=my_email, password=password)
    subject = "Greetings"
    body = "Hello Abhishek Nayak Sir! You are the billionare"
    msg = f"Subject: {subject}\n\n{body}"
    connection.sendmail(from_addr=my_email, to_addrs='webcoder41@gmail.com', msg=msg)

#  Working with dates
import datetime as dt

now = dt.datetime.now()
print(now)
year = now.year
month = now.month
day_of_week = now.weekday()
print(month, year, day_of_week)

date_of_birth = dt.datetime(year=2001, month=8, day=17)
print(date_of_birth)