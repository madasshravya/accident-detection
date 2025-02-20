import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(detected_gun, address, name):
    # Email configuration
    sender_email = "malarvizhi.ramu1986@gmail.com"
    receiver_email = "sandhya01027@gmail.com"
    password = "yazyisjpzfsiqwes"
    
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Vehicle Behavior Prediction"
    
    # Email body
    body = f"Detected Vehicle Crash "
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to SMTP server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

# Example usage
detected_gun = "Vehicle Behavior Type"
address = "123 Main Street"
name = "John Doe"
send_email(detected_gun, address, name)
