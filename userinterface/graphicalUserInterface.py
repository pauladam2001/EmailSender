from tkinter import *
from tkinter import messagebox
import speech_recognition
import re
from validator.validator import EmailValidator


class GraphicalUI:
    def __init__(self, controller):
        self._controller = controller
        self._listener = speech_recognition.Recognizer()

        self.sign_in_window = Tk()
        self.sign_in_window.title("Login")
        self.sign_in_window.iconbitmap("../EmailSender/email.ico")
        self.sign_in_window.config(bg='white')
        # self.main_window.geometry("400x200")

        screen_width = self.sign_in_window.winfo_screenwidth()
        screen_height = self.sign_in_window.winfo_screenheight()
        x = (screen_width / 2) - (400 / 2)  # make the main window pop on the middle of the screen
        y = (screen_height / 2) - (200 / 2)
        self.sign_in_window.geometry(f'{400}x{200}+{int(x)}+{int(y)}')

    def set_server(self, mail, user, password):
        self._controller.set_server(mail, user, password)

    def get_information(self):
        try:
            with speech_recognition.Microphone() as source:
                self._controller.talk('Listening!')
                voice = self._listener.listen(source)
                information = self._listener.recognize_google(voice)   # google API
                return information.lower()
        except Exception as e:
            messagebox.showerror('Error', 'Please talk!')

    def sign_in_button(self):
        self.sign_in(None)

    def sign_in(self, arg):                 # to bind enter event we need arg
        self.user = self.user_entry.get()
        passwd = self.password_entry.get()
        mail = ''

        if re.search("@yahoo.com", self.user):
            mail = 'smtp.mail.yahoo.com'
        elif re.search("@gmail.com", self.user):
            mail = 'smtp.gmail.com'
        else:
            messagebox.showerror('Invalid mail', 'The address is not valid!')
            self.user_entry.delete(0, END)
            self.password_entry.delete(0, END)
        if mail != '':
            try:
                self.set_server(mail, self.user, passwd)
                self.sign_in_window.destroy()
                self.start_main_window()
            except Exception:
                messagebox.showerror('Error', 'Username or password not valid!')
                self.user_entry.delete(0, END)
                self.password_entry.delete(0, END)

    def start_sing_in_window(self):
        username_frame = Frame(self.sign_in_window, bg='white')
        username_frame.pack(pady=20)

        login_label = Label(username_frame, text='Yahoo / Gmail', bg='white', fg='dark green')
        login_label.pack(pady=5)

        user_label = Label(username_frame, text='Username:', bg='white', fg='dark green')
        user_label.pack(side=LEFT)

        self.user_entry = Entry(username_frame, {}, width=50, border=2)
        self.user_entry.pack(pady=10)

        password_frame = Frame(self.sign_in_window)
        password_frame.pack()

        password_label = Label(password_frame, text='Password:', bg='white', fg='dark green')
        password_label.pack(side=LEFT)

        self.password_entry = Entry(password_frame, show='*', width=50, border=2)        # so the password is secured
        self.password_entry.pack()
        self.password_entry.bind('<Return>', self.sign_in)          # binding enter key to password entry so we don't need to press the sign in button every time

        button_frame = Frame(self.sign_in_window, bg='white')
        button_frame.pack(pady=15)

        sign_in_button = Button(button_frame, padx=15, text='Sign in', bg='dark green', fg='white', activebackground='green', activeforeground='white', width=10, height=20, command=self.sign_in_button)
        sign_in_button.pack(pady=10)

        self.sign_in_window.mainloop()

    def get_name_button(self):
        name = self.get_information()
        if name is None:
            pass
        else:
            if name not in self._controller.get_dictionary():
                self._controller.talk("Maybe I can't hear correctly, please try to write the name")
            else:
                self.name_entry.insert(0, name)
                self.receiver_entry.configure(state=NORMAL)     # now we can place the associated address in the entry
                self.receiver_entry.insert(0, self._controller.get_dictionary()[name])

    def get_name_entry(self, arg):
        name = self.name_entry.get()
        self.receiver_entry.configure(state=NORMAL)  # now we can write the address in the entry
        if name not in self._controller.get_dictionary():
            self._controller.talk('Address associated to this name not found, please write the address')
        else:
            self.receiver_entry.insert(0, self._controller.get_dictionary()[name])

    def get_receiver_button(self):
        self.get_receiver(None)

    def get_receiver(self, arg):
        receiver = self.receiver_entry.get()
        if not EmailValidator.validate(receiver):
            self._controller.talk('Email not valid! Try again!')
            self.receiver_entry.delete(0, END)
        else:
            self._controller.talk('Do you want to add this address to the database?')
            answer = self.get_information()
            if answer == 'yes':
                try:
                    self._controller.add_address(receiver, self.name_entry.get())
                    self._controller.talk('Address added!')
                except Exception:
                    messagebox.showinfo('Error', 'Address or name already in the database!')
            elif answer == 'no':
                pass

    def get_subject_button(self):
        subject = self.get_information()
        self.subject_entry.insert(0, subject)

    def get_message_button(self):
        message = self.get_information()
        self.message_entry.insert(0, message)

    def show_addresses(self):
        addresses = self._controller.get_dictionary()
        addresses_to_show = ''
        for key, value in addresses.items():
            addresses_to_show += key + ' - ' + value + '\n'
        messagebox.showinfo('Addresses', addresses_to_show)

    def send_email(self):
        try:
            self._controller.send_email(self.user, self.receiver_entry.get(), self.subject_entry.get(),
                                        self.message_entry.get())
            self._controller.talk('Your email was sent!')
            self.name_entry.delete(0, END)
            self.receiver_entry.delete(0, END)
            self.subject_entry.delete(0, END)
            self.message_entry.delete(0, END)
        except Exception:
            self._controller.talk("Your email was not sent!")

    def start_main_window(self):
        self.main_window = Tk()
        self.main_window.title('EmailAutomation')
        self.main_window.iconbitmap("../EmailSender/email.ico")
        self.main_window.config(bg='white')

        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        x = (screen_width / 2) - (525 / 2)  # make the main window pop on the middle of the screen
        y = (screen_height / 2) - (280 / 2)
        self.main_window.geometry(f'{525}x{280}+{int(x)}+{int(y)}')

        main_frame = Frame(self.main_window, bg='white')
        main_frame.grid(row=0, column=0, pady=10)

        name_label = Label(main_frame, text='Name of receiver: ', pady=5, padx=20, bg='white', fg='dark green')
        name_label.grid(row=1, column=0)

        self.name_entry = Entry(main_frame, width=50, border=2)
        self.name_entry.grid(row=1, column=1)
        self.name_entry.bind('<Return>', self.get_name_entry)

        talk_name_button = Button(main_frame, text='Talk', padx=15, bg='dark green', fg='white', activebackground='green', activeforeground='white', command=self.get_name_button)
        talk_name_button.grid(row=1, column=2, padx=10)

        receiver_label = Label(main_frame, text="Receiver's address: ", pady=10, bg='white', fg='dark green')
        receiver_label.grid(row=2, column=0)

        self.receiver_entry = Entry(main_frame, width=50, state=DISABLED, border=2)
        self.receiver_entry.grid(row=2, column=1)
        self.receiver_entry.bind('<Return>', self.get_receiver)

        address_button = Button(main_frame, text='Next', padx=15, bg='dark green', fg='white', activebackground='green', activeforeground='white', command=self.get_receiver_button)
        address_button.grid(row=2, column=2)

        subject_label = Label(main_frame, text='Subject: ', pady=10, bg='white', fg='dark green')
        subject_label.grid(row=3, column=0)

        self.subject_entry = Entry(main_frame, {}, width=50, border=2)
        self.subject_entry.grid(row=3, column=1)

        talk_subject_button = Button(main_frame, text='Talk', padx=15, bg='dark green', fg='white', activebackground='green', activeforeground='white', command=self.get_subject_button)
        talk_subject_button.grid(row=3, column=2)

        message_label = Label(main_frame, text='Message: ', pady=10, bg='white', fg='dark green')
        message_label.grid(row=4, column=0)

        self.message_entry = Entry(main_frame, {}, width=50, border=2)
        self.message_entry.grid(row=4, column=1)

        talk_message_button = Button(main_frame, text='Talk', padx=15, bg='dark green', fg='white', activebackground='green', activeforeground='white', command=self.get_message_button)
        talk_message_button.grid(row=4, column=2)

        show_database_button = Button(main_frame, text='Show contacts', bg='dark green', fg='white', activebackground='green', activeforeground='white', command=self.show_addresses)
        show_database_button.grid(row=7, column=1)

        send_email_button = Button(main_frame, text='Send email', bg='dark green', fg='white', activebackground='green', activeforeground='white', command=self.send_email)
        send_email_button.grid(row=5, column=1, pady=20)

        self.main_window.mainloop()
