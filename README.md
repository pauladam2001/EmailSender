# EmailSender
### Python-based Email Sender Application for Yahoo/Gmail.
---
# Used Concepts
- Layered Architecture
- Object Oriented Porgramming
- Tkinter Graphical User Interface
- Console User Interface
- SQLite3 Database
- smtplib, pyttsx3, pyaudio, SpeechRecognition API etc.
- PyInstaller
---
# Functionalities
- Send an email with your Yahoo/Gmail account
- Option to talk instead of writing your emails
- Option to save the addresses in the database with a simpler name
---
# How it works - Console UI
- Only for me, I can connect with Yahoo/Gmail, the passwords are stored in environment variables
# How it works - Graphical UI
- Sign in window: Start by logging in with your Yahoo or Gmail account (for Gmail: 'Manage your google account' -> 'Security' -> 'Less secure app access' -> Turn on; for Yahoo: Create a '1-time password' in 'Account info' -> 'Account security' and log in with that password)
- Main window: Introduce the name associated to the address of the receiver (if it is not in the database you need to introduce the email address and after you can save it in the database), the subject and the message and press 'Send email'. You have the option to speak and the computer will let you know if the email was sent.
---
# Demo
- Login Window
- ![SignInWindow](https://user-images.githubusercontent.com/72084877/137708176-735117c0-851e-4682-a8d1-def1ab3a1c53.png) 
