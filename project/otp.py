import smtplib
import random
import math
import os

n = "0123456789"
otp = ""
for i in range(6):
    otp+= n[math.floor(random.random()*10)]
OT = otp + " is your One-Time-Password for verification"
message = OT

email = smtplib.SMTP(host='smtp.gmail.com', port=587)  # To call the gmail account client
email.starttls()
#Aqui foi preciso conectar um gmail seguindo estes passos: https://support.google.com/mail/answer/185833?hl=en#
email.login(user="camila.oliveirahftecnologia@gmail.com", password="dopf jtvn sfay gzug")  
key = input("Enter your email address : ") #gerar e-mail em: https://temp-mail.org/en/
email.sendmail(from_addr= "camila.oliveirahftecnologia@gmail.com", to_addrs=key, msg=message)   # Envia o OTP pelo e-mail definido
x = input("Enter your OTP: ") 
if x == otp:
    print("Your account has been successfully verified.")
else:
    print("Please check your OTP once again.")