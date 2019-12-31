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

    def emailValidate(self, name):
        if len(name) > 100 or '' == name or 'null' == name:
            return False
        return True