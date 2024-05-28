'''

import datetime
a=datetime.datetime.now()
print(a)
print(a.strftime("%d"))
print(a.strftime("%y"))
print(a.strftime("%m"))
print(a.strftime("%p"))   '''



'''
import random
# print(random.randint(0,20))
print(random.randint(1001,9999))'''


'''
import random
a=["irfan","ahmed","kavin","kumar","fawaz"]
for i in range(3):
    print(random.choice(a))'''



#atm task using random method:::



import smtplib
import random
from email.mime.text import MIMEText

# Function to generate OTP
def generate_otp():
    return random.randint(1000, 9999)

# Function to send OTP via email
def send_otp_email(otp, to_email):
    from_email = "your_email@gmail.com"  # Replace with your email
    password = "your_email_password"  # Replace with your email password

    msg = MIMEText(f"Your OTP is: {otp}")
    msg['Subject'] = 'OTP Verification'
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

# Your existing code with some modifications

print("Enter your card")

while True:
    try:
        pin = int(input("ENTER YOUR PIN:"))
        if pin == 2468:
            # Generate and send OTP
            otp = generate_otp()
            to_email = "your_email@gmail.com"  # Replace with your email
            send_otp_email(otp, to_email)

            # Verify OTP
            entered_otp = int(input("Enter the OTP sent to your email:"))
            if entered_otp == otp:
                print("OTP Verified. Access granted.")


                print("1.Withdraw")
                print("2.Deposit")
                print("3.Banking")
                select = input("Select the option:")

                if select == "1":
                    amount = int(input("Enter the amount:"))
                    if amount >= 5000:
                        print("Collect your amount")
                    else:
                        raise ValueError("Invalid amount")

                elif select == "2":
                    deposit_amount = int(input("Enter the deposit amount:"))
                    if deposit_amount >= 1000:
                        print("Insert the amount")
                    else:
                        raise ValueError("Invalid deposit amount")

                elif select == "3":
                    print("Your balance is 10000")

                break

            else:
                raise ValueError("Invalid OTP. Access denied.")

        else:
            raise ValueError("Invalid PIN")

    except ValueError as ve:
        print(f"Error: {ve}")
