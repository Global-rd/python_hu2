import azure.functions as func
import logging
from email_sender import EmailSender
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="f_robotdream_python_http_test")
def f_robotdream_python_http_test(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    email_sender = EmailSender(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        sender_email = os.environ.get("GMAIL_EMAIL"),
        sender_password=os.environ.get("GMAIL_PW")
    )

    email_sender.send_email(
        recipients=["nigrushid@gmail.com"],
        subject="Test Email",
        body= "Szia!"
    )

    challenge = req.params.get("challenge")

    if challenge:
        return func.HttpResponse(challenge, status_code=200)
    
    return func.HttpResponse("All good!", status_code=200)