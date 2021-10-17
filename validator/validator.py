import re     # regex


class EmailValidator:
    @staticmethod
    def validate(email):
        for index in range(len(email)):
            character = email[index]
            if character in [' ', '%', '#', '&', '*', '(', ')']:
                return False
        if not (re.search("@gmail.com", email) or re.search("@yahoo.com", email)):
            return False
        return True
