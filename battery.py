import time
import psutil
from twilio.rest import Client


account_sid = 'DA02b0c4a7d4319df542110e4465f70298'  #Replace by your sid
auth_token = '2b244e51cfe76263185ee76acb27f8ca'     #Replace by your token 
from_whatsapp_number = 'whatsapp:+14155238876'      #Replace by Your Number 
to_whatsapp_number = 'whatsapp:+910000000007'       #Replace by your Whatsapp Number 

client = Client(account_sid, auth_token)

notified = False

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent

    if percent >= 98 and not notified:
        message = client.messages.create(
            body="Your laptop is 98% charged. Please remove it from charging.",
            from_=from_whatsapp_number,
            to=to_whatsapp_number
        )
        print("Message sent!")
        notified = True

    if percent < 95:
        notified = False  # Reset if battery drops

    time.sleep(60)  # Check every 60 seconds
