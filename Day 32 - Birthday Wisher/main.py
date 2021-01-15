import smtplib
import datetime as dt
import pandas as pd
import random

placeholder = "[NAME]"
my_email = "codetestpython@gmail.com"
password = "abcd1234()"

today = (dt.datetime.now().month, dt.datetime.now().day)

# open the file that includes all birthdays
birthdays = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays.iterrow()}

if today in birthdays_dict:
    # open a random letter and replace the recipient's name
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        letter_contents = letter_file.read()
        friend_name = birthdays_dict[today]["name"]
        new_letter = letter_contents.replace(placeholder, friend_name)

    # SMTP host information: Gmail = smtp.gmail.com, Hotmail = smtp.live.com, Yahoo = smtp.mail.yahoo.com

    with smtplib.SMTP("smtp.gmail.com") as connection:
        # secure connection to email server
        connection.starttls()
        connection.login(user=my_email, password=password)

        # In order for the email to be sent off using Python you need to change your email security options.
        # For Gmail, make sure that "2-step verification" and "Use your phone to sin in" are set to "off".
        # In addition you would need to turn on your "Less secure app access" option.
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_dict[today]["email"],
                            msg=f"Subject:Happy Birthday {friend_name}!\n\n{new_letter}.")

