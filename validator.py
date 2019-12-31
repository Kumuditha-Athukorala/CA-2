

class Validator:

    def customerDetailsValidate(self,firstName):
        if(len(firstName) > 50 ):
            return False
        if('' == firstName):
            return False
        if('null' == firstName):
            return False
        return True