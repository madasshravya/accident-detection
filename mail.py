import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from datetime import datetime 

def get_live_location():
    try:
        # Use a reliable geolocation service or API to get live location
        response = requests.get('http://ip-api.com/json/')
        if response.status_code == 200:
            data = response.json()
            latitude = data['lat']
            longitude = data['lon']
            return latitude, longitude
        else:
            raise Exception("Failed to retrieve location data")
    except Exception as e:
        print("Error retrieving location:", e)
        return None, None

def send_email(detected_gun, address, name):
    # Email configuration
    sender_email = "shravyamadas@gmail.com"
    receiver_email = "madasshravya@gmail.com"
    password = "jitmrnbybrbnimos"
    
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Vehicle Behavior Prediction"
    
    # Get live location
    latitude, longitude = get_live_location()

    #Get current system time
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S"); 
    
    # Email body
    body = f"Detected Vehicle Crash at {address}. \n\n"
    if latitude is not None and longitude is not None:
        body += f"Live Location:\nLatitude: {latitude}\nLongitude: {longitude}\n"
    else:
        body += "Failed to retrieve live location."
    body += f"Accident time: {current_time}"
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to SMTP server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

# Example usage
detected_gun = "Vehicle Behavior Type"
address = "IIIT campus, Basar, Telangana, India "
name = "John Doe"
send_email(detected_gun, address, name)
