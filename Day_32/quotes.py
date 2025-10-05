import smtplib
import datetime as dt
import random


now = dt.datetime.now()
day_of_week = now.weekday()

def send_quote_email():
    # Reading and getting the random quote
    with open('quotes.txt', mode='r') as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

        #Email Credentials
        my_email = 'sahilservice300@gmail.com'
        password = 'ldxlnrloejkpxzmt'
        with smtplib.SMTP("smtp.gmail.com") as connection :
            connection.starttls()
            connection.login(user=my_email, password=password)
            msg = f"Subject: Today's Motivational Quote!\n\n{quote}"
            connection.sendmail(from_addr=my_email, to_addrs='webcoder41@gmail.com', msg=msg)

if day_of_week == 6:
    send_quote_email()