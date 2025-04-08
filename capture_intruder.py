from picamzero import Camera
import time
from datetime import datetime
import RPi.GPIO as GPIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

cam = Camera()
home_dir = "/home/davis"
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

curr_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
video_filename = f"{home_dir}/Desktop/intruder_alert_{curr_time}.mp4"

try:
    while True:
        input_value = GPIO.input(10)
        if input_value:
            print("Intruder detected!")
            #cam.start_preview()
            cam.record_video(video_filename, duration=10)
            #cam.stop_preview()
            cam.stop_recording()
            print(f"Video saved: {video_filename}")
            subject = "INTRUDER ALERT!!"
            body = "Please see the intruder in the attached video"
            sender_mail = "piburner44@gmail.com"
            recipient_mail = "davidani384@gmail.com"
            send_pass = "rsab kbzp rkah hlij"
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            path_to_file = video_filename

            message = MIMEMultipart()
            message['Subject'] = subject
            message['From'] = sender_mail
            message['To'] = recipient_mail

            body_part = MIMEText(body, 'plain')
            message.attach(body_part)

            try:
                # Attach video file to the email
                with open(path_to_file, 'rb') as file:
                    file_part = MIMEApplication(file.read(), Name="Intruder_Alert.mp4")
                    file_part['Content-Disposition'] = f'attachment; filename="Intruder_Alert.mp4"'
                    message.attach(file_part)

                # Send email via SMTP
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()  # Secure the connection
                    server.login(sender_mail, send_pass)  # Log in to the server
                    server.sendmail(sender_mail, recipient_mail, message.as_string())  # Send email
                    print("Email sent successfully!")
            except Exception as e:
                print(f"Error while sending email: {e}")
            time.sleep(5)
        else:
            print("No intruder detected.")
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nExiting program...")
finally:
    GPIO.cleanup()

    

