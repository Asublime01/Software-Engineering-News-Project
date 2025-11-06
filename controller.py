import smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import model
import datetime




def send_newsletter():
    sender_email = "evilormes225@gmail.com"
    sender_password = "umog ahzw inau vuhk "  
    receiver_email = "gormes@lps.k12.co.us"
    subject = "Newsletter of the Day!"
    with open('email_body.txt', "w") as file:        
        gathered_data = model.get_newsletter_data()
        for info_list in gathered_data:
            

            if info_list.count(";") == 2: #Meaning that there is a description included 
                title, des, url = info_list.split(";")
                file.write(f"Title: {title}\nDescription: {des}\nURL: {url}\n\n")
            elif info_list.count(";") == 1: #No description clause 
                title, url = info_list.split(";") 
                file.write(f"Title: {title}\nURL: {url}\n\n")
                
       

    msg = MIMEMultipart()
    
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    filename = "email_body.txt"  # Replace with your file name
    filepath = "/home/cadenbents/Documents/ScrollDisplay/Software-Engineering-News-Project/email_body.txt"  # Full path to the file

    # Open the file in binary mode
    with open(filepath, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header to indicate attachment
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={filename}",
    )

    # Attach the file to the email
    msg.attach(part)

    smtp_server = "smtp.gmail.com"  # Gmail link
    smtp_port = 587  # TLS port

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

send_newsletter()