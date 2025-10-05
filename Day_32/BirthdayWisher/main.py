import smtplib
import random
import pandas
import datetime as dt

now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}

# If today is the birthday then read the file and replace the name of the birthday person
if today_tuple in birthdays_dict:
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    birthday_person = birthdays_dict[today_tuple]
    with open(file_path, mode='r') as letter_file :
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    
    # Send Email
    my_email = 'sahilservice300@gmail.com'
    password = 'ldxlnrloejkpxzmt'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        subject = "Happy Birthday!"
        body = contents
        msg = f"Subject: {subject}\n\n{body}"
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=msg)
