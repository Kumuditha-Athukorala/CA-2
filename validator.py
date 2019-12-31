import re


class Validator:

    def customerDetailsValidate(self, firstName):
        if len(firstName) > 50 or '' == firstName or 'null' == firstName:
            print("")
            return False
        return True

    def nameValidate(self, name):
        if len(name) > 50:
            print("Name cannot be more than 50 characters.")
            return False
        if '' == name or 'null' == name:
            print("Name cannot be blank.")
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
        return True
