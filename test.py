import discord
from redmail import gmail
import pandas as pd

gmail_user_name = "samsono.odwori@gmail.com"
gmail_password = "crvbbmmtvwctlogp"

def send_alert(img_path):
    message = "Animal intruder found!!"
    

    # Send an email
    gmail.username = gmail_user_name
    gmail.password = gmail_password

    gmail.send(
        subject="Intruder Alert",
        sender=gmail_user_name,
        receivers="samsono.odwori@gmail.com",
        html="""
            <h1>Unauthorized entity found!</h1>
            {{ myimg }}
        """,
        body_images={"myimg": img_path}
    )

