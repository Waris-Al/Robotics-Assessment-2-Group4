# Import necessary libraries
from picamzero import Camera
import time
from datetime import datetime
import RPi.GPIO as GPIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication 

# Initialise the camera
cam = Camera()

# Set your home directory path
home_dir = "/home/davis"

# Set GPIO mode to BOARD layout
GPIO.setmode(GPIO.BOARD)

# Set GPIO pin 10 as input with pull-down resistor
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Generate a timestamped filename for the recorded video
curr_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
video_filename = f"{home_dir}/Desktop/intruder_alert_{curr_time}.mp4"

# Try to run the motion detection loop
try:
    while True:
        # Read input from the sensor on GPIO pin 10
        input_value = GPIO.input(10)

        # If motion is detected (input is HIGH)
        if input_value:
            print("Intruder detected!")

            # Record a 10-second video
            # cam.start_preview()  # Uncomment if you want a live preview
            cam.record_video(video_filename, duration=10)
            # cam.stop_preview()
            cam.stop_recording()

            print(f"Video saved: {video_filename}")

            # Email setup
            subject = "INTRUDER ALERT!!"
            body = "Please see the intruder in the attached video"
            sender_mail = "piburner44@gmail.com"
            recipient_mail = "davidani384@gmail.com"
            send_pass = "rsab kbzp rkah hlij"  # App password (never share publicly!)
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            path_to_file = video_filename

            # Create the email message object
            message = MIMEMultipart()
            message['Subject'] = subject
            message['From'] = sender_mail
            message['To'] = recipient_mail

            # Attach the text body
            body_part = MIMEText(body, 'plain')
            message.attach(body_part)

            try:
                # Open the recorded video file and attach it
                with open(path_to_file, 'rb') as file:
                    file_part = MIMEApplication(file.read(), Name="Intruder_Alert.mp4")
                    file_part['Content-Disposition'] = 'attachment; filename="Intruder_Alert.mp4"'
                    message.attach(file_part)

                # Send the email using SMTP
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()  # Start TLS encryption
                    server.login(sender_mail, send_pass)  # Login to email account
                    server.sendmail(sender_mail, recipient_mail, message.as_string())  # Send the email

                    print("Email sent successfully!")

            except Exception as e:
                # Handle any errors that occur during email sending
                print(f"Error while sending email: {e}")

            # Wait for a few seconds to avoid sending multiple emails too quickly
            time.sleep(5)

        else:
            print("No intruder detected.")

        time.sleep(1)


except KeyboardInterrupt:
    print("\nExiting program...")

# Clean up GPIO settings when program exits
finally:
    GPIO.cleanup()
