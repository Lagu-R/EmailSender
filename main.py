import smtplib


MY_EMAIL = "Sender_Email"
MY_PASSWORD = "password"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="Recipient Email",
                        msg="Subject:Hello subjcet \n\n Body text here")
    connection.close()
