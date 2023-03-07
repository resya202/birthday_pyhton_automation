import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Set up your email account details
MY_ADDRESS = "your_email@example.com"
PASSWORD = "your_email_password"

# Read data from the xlsx file
data = pd.read_excel('birthday_data.xlsx')

# Loop through the data and send emails to each friend
for index, row in data.iterrows():
    friend_name = row['Name']
    friend_email = row['Email']
    friend_birthday = row['Birthday']

    # Check if today's date matches the friend's birthday
    if datetime.today().strftime('%m-%d') == friend_birthday.strftime('%m-%d'):
        # Set up the email message
        msg = MIMEMultipart()
        msg['From'] = MY_ADDRESS
        msg['To'] = friend_email
        msg['Subject'] = f"Happy Birthday {friend_name}!"
        body = f"Dear {friend_name},\n\nWishing you a very happy birthday! Have a wonderful day filled with lots of love and happiness.\n\nBest regards,\nYour Name"
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(MY_ADDRESS, PASSWORD)
            smtp.send_message(msg)

        print(f"Sent birthday email to {friend_name} ({friend_email})")
