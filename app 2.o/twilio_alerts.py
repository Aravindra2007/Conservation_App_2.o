from twilio.rest import Client

ACCOUNT_SID = "AC6c7690f9d0b31b8d1873288a5968f28a"
AUTH_TOKEN = "153d3f795a940e42e15f3bc671a49da8"
TWILIO_PHONE = "+19788833751"
to_number = "+918919146448"

def send_sms(to_number, message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE,
        to=to_number
    )
