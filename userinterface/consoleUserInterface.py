import speech_recognition   # API
from validator.validator import EmailValidator
import os   # used in order to acces the environment variables YAHOO_PASSWORD and GMAIL_PASSWORD, so that I don't hardcode them


class ConsoleUI:
    def __init__(self, controller):
        self._controller = controller
        self._listener = speech_recognition.Recognizer()

    def show_addresses(self):
        addresses = self._controller.get_dictionary()
        for key, value in addresses.items():
            print(key + " : " + value)

    def set_server(self, mail, user, password):
        print('\nLogging...')
        self._controller.set_server(mail, user, password)
        print('Logged successfully!\n')

    def get_information(self):
        try:
            with speech_recognition.Microphone() as source:
                print('Listening!')
                voice = self._listener.listen(source)
                information = self._listener.recognize_google(voice)   # google API
                return information.lower()
        except Exception as e:
            print(e)

    def get_receiver(self):
        print("To whom do you want to send an email? Wait for 'Listening!' to appear.")
        self._controller.talk('To whom do you want to send an email?')
        print('\t1. Write;')
        print('\t2. Talk.')
        option = input('Enter option: ')
        if option == '1':
            name = input('Name: ')
        elif option == '2':
            name = self.get_information()
            if name not in self._controller.get_dictionary():
                print("Maybe I can't hear correctly, please try to write the name.")
                self._controller.talk("Maybe I can't hear correctly, please try to write the name.")
                name = input('Name:')
        if name not in self._controller.get_dictionary():
            print('Address associated to this name not found, please write the address.')
            self._controller.talk('Address associated to this name not found, please write the address')

            done = False
            while not done:
                receiver = input('Address: ')
                if not EmailValidator.validate(receiver):
                    print('Email not valid! Try again!')
                    self._controller.talk('Email not valid! Try again!')
                else:
                    done = True

            print('Do you want to add this address to the database? [yes/no]')
            self._controller.talk('Do you want to add this address to the database?')
            ans = self.get_information()
            if ans == 'yes':
                assoc_name = input('Introduce associated name: ')
                self._controller.talk('Introduce associated name')
                try:
                    self._controller.add_address(receiver, assoc_name)
                    print('Address added!')
                    self._controller.talk('Address added')
                except Exception as e:
                    print(e)
                    print("Address not added!")
                    self._controller.talk('Address not added')
            elif ans == 'no':
                pass
        else:
            receiver = self._controller.get_dictionary()[name]

        return receiver

    def get_subject(self):
        print('\nWhat is the subject of your email?')
        self._controller.talk('What is the subject of your email?')
        print('\t1. Write;')
        print('\t2. Talk.')

        done = False
        while not done:
            option = input('Enter option: ')
            if option == '1':
                subject = input('Subject: ')
                done = True
            elif option == '2':
                subject = self.get_information()
                done = True
            else:
                print('Invalid option! Choose between 1 and 2!')

        return subject

    def get_message(self):
        print('\nWhat is the message of your email?')
        self._controller.talk('What is the message of your email?')
        print('\t1. Write;')
        print('\t2. Talk.')

        done = False
        while not done:
            option = input('Enter option: ')
            if option == '1':
                message = input('Message: ')
                done = True
            elif option == '2':
                message = self.get_information()
                done = True
            else:
                print('Invalid option! Choose between 1 and 2!')

        return message

    def start(self):
        done = False

        print("\nAddresses in the database:")
        self.show_addresses()

        while not done:
            print('\nChoose mail:')
            print('\t0. Exit;')
            print('\t1. Yahoo;')
            print('\t2. Gmail.')
            self._controller.talk('Choose mail')
            option = input('Enter option: ')

            if option == '0':
                print('See you later!')
                self._controller.talk('See you later!')
                break
            elif option == '1':
                mail = 'smtp.mail.yahoo.com'
                user = 'paul.adrian2001@yahoo.com'
                password = os.environ.get('YAHOO_PASSWORD')     # environment variable
            elif option == '2':
                mail = 'smtp.gmail.com'
                user = 'paul.adrian242001@gmail.com'
                password = os.environ.get('GMAIL_PASSWORD')     # environment variable

            if option not in ['0', '1', '2']:
                print('Invalid option!')
                self.start()
                break
            else:
                self.set_server(mail, user, password)     # this way the variables are not referenced before assignment

            receiver = self.get_receiver()

            subject = self.get_subject()

            message = self.get_message()

            try:
                self._controller.send_email(user, receiver, subject, message)
                print('\nYour email was sent!')
                self._controller.talk('Your email was sent!')
            except Exception as e:
                print(e)
                print("Your email was not sent!")
                self._controller.talk("Your email was not sent!")

            print('\nDo you want to send another email? [yes/no]')
            self._controller.talk('Do you want to send another email?')
            answer = self.get_information()
            if answer == 'no':
                print('\nSee you later!')
                self._controller.talk('See you later!')
                break

    def close_connection(self):
        self._controller.close_connection()
