import smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import model
import datetime




def send_newsletter():
    sender_email = "mr.cryan225@gmail.com"
    sender_password = "zwqd hhzj awmv ieuu"  
    receiver_email = "gormes@lps.k12.co.us"
    subject = "Newsletter of the Day!"
            
    gathered_data = model.get_newsletter_data()
    email_bodyList = []
    for info_list in gathered_data:
        
        if info_list.count(";") == 2: #Meaning that there is a description included 
            title, des, url = info_list.split(";")
            line = f"{title}   Description: {des}   URL: {url}"
            email_bodyList.append(line)
        elif info_list.count(";") == 1: #No description clause 
            title, url = info_list.split(";") 
            line = f"{title}   URL: {url}"
            email_bodyList.append(line)
               

    
    body = "\n\n".join(f"- {item}" for item in email_bodyList)
       

    msg = MIMEText(body, "plain")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

send_newsletter()