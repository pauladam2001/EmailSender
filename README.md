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
- Login Window (press 'Sign in' button or enter after you type your password in order to connect)
- ![SignInWindow](https://user-images.githubusercontent.com/72084877/137708176-735117c0-851e-4682-a8d1-def1ab3a1c53.png) 
- Main window (you can write or press 'Talk' button and you can speak; after you introduce the name, if the address is not in the database you will be able to introduce it. After you write the address press enter or 'Next' button in order to validate it and to have the possibility to introduce it in the database)
- ![MainWindow](https://user-images.githubusercontent.com/72084877/137708340-cebdc63c-5d1d-4da8-b82a-bf6d44ce1136.png)
- After you complete every field press 'Send email' and the application will let you know if your email was sent.
- ![SendEmail](https://user-images.githubusercontent.com/72084877/137709595-442f3bca-de10-4f40-9e52-39d2e931879b.png)
- Press 'Show contacts'button if you want to see addresses already in the database.
- ![Addresses](https://user-images.githubusercontent.com/72084877/137709758-1e382351-af16-4e45-888e-db5742faef51.png)
