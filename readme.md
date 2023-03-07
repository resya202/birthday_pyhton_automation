# Pyhton automation birthday

In this script, we first import the necessary libraries such as pandas for reading xlsx files and smtplib for sending emails. We then set up our email account details such as email address and password.

Next, we read the data from the xlsx file using pandas and loop through each friend's details. For each friend, we check if today's date matches their birthday, and if so, we set up the email message with their name, email address, and a customized birthday message. We then send the email using smtplib and print a confirmation message to the console.

Make sure to replace your_email@example.com and your_email_password with your actual email account details, and update the birthday_data.xlsx file with your friends' details including their name, email address, and birthday in the format "YYYY-MM-DD".