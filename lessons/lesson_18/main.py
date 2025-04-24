import os
from email_sender import EmailSender
from telegram import Telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    #email sending:
    email_sender = EmailSender(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        sender_email = os.environ.get("GMAIL_EMAIL"),
        sender_password=os.environ.get("GMAIL_PW")
    )

    html_body = EmailSender.render_email_template(template_path="lessons/lesson_18/email_template.html",
                                                  context={"user_name": "Tóbiás",
                                                           "year": 2025})
    

    email_sender.send_email(
        recipients=["nigrushid@gmail.com"],
        subject="Test Email",
        body= html_body, #"Szia!"
        attachments=["lessons/lesson_18/to_send.csv"]
    )

    #telegram message:

    telegram = Telegram(bot_token=os.environ.get("TELEGRAM_BOT_TOKEN"),
                        chat_id=os.environ.get("TELEGRAM_CHAT_ID"))
    
    telegram.send_telegram_message("This is a test message from the course.")

if __name__ == "__main__":
    main()
