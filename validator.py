import re


class Validator:

    def nameValidate(self, name):
        if len(name) > 50:
            print("Field cannot be more than 50 characters.")
            return False
        if '' == name or 'null' == name:
            print("Field cannot be blank.")
            return False
        return True

    def addrValidate(self, name):
        if len(name) > 100 :
            print("Address cannot be more than 100 characters.")
            return False
        if '' == name or 'null' == name:
            print("Address cannot be blank.")
            return False
        return True

    def emailValidate(self, email):
        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email")
            return False
        if len(email) > 100 or '' == email or 'null' == email:
            print("Email too long or blank")
            return False
        return True

    def numberValidate(self, no):

        if len(no) > 13 or '' == no or 'null' == no:
            print("Phone Number too long or blank")
            return False
        while True:
            try:
                userInput = int(no)
            except ValueError:
                print("Not a valid number.! Enter again.")
                return False
            else:
                return True
                break
        return True

    def inputNumber(message):
        while True:
            try:
                userInput = int(input(message))
            except ValueError:
                print("Not a valid number.! Enter again.")
                continue
            else:
                return userInput
                break
