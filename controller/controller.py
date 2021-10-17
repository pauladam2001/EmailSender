import smtplib  # simple mail transport protocol
# import pyaudio
import pyttsx3  # in order for python to talk
from email.message import EmailMessage  # for subject


class Controller:
    def __init__(self, repository):
        self._repository = repository
        self._engine = pyttsx3.init()

    def set_server(self, mail, user, password):
        self._server = smtplib.SMTP(mail, 587)      # server name and port
        self._server.starttls()     # now the server trusts me
        self._server.login(user, password)

    def talk(self, text):           # with this function python talks to me
        self._engine.say(text)
        self._engine.runAndWait()

    def send_email(self, sender, receiver, subject, message):
        email = EmailMessage()
        email['From'] = sender
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(message)
        self._server.send_message(email)
        self._server.quit()

    def get_dictionary(self):
        return self._repository.get_dictionary()

    def add_address(self, address, nickname):
        self._repository.add_address(address, nickname)

    def close_connection(self):
        self._repository.close_connection()
