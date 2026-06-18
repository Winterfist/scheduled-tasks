import os
import smtplib
from datetime import datetime
import random
import pandas as pd
#----------SET UP CONNECTION CREDENTIALS--------------
my_email = "ciurea.andrei4@gmail.com"
password = "ojti aamk bhlh ebov"
#----------GET CURRENT DAY AND MONTH-------------------
today_date_day = datetime.now().day
today_date_month = datetime.now().month
#---------GET DATA AND COMPARE-------------------------
dates = pd.read_csv("birthdays.csv")
matches = dates[(dates["month"] == today_date_month) & (dates["day"]==today_date_day)]
#--------CONNECT AND SEND MAIL FOR MATCHES-------------
for _,match in matches.iterrows():
    template_file = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(template_file, 'r') as template:
        letter_content = template.read()
    personalized_message = letter_content.replace("[NAME]", match["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=match["email"], msg=f"Subject:Happy birthday!\n\n{personalized_message}")
