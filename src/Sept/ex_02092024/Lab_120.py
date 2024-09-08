## real exmple
##WebAutomation  selenium
## Page goign to automate : app.vwo.com


class VWOLoginPage:

    def __init__(self, email_arg ,pwd_arg):
        self.email =  email_arg
        self.pwd =  pwd_arg

    def login_confirm(self):
        if self.email == "test@gmail.com" and self.pwd == "Test":
            print ("Allow the login")
        else:
            print ("Not allowed")


#create obj:
email = input("Enter the email\n")
pwd = input("Enter the pwd\n")
oVWO = VWOLoginPage(email , pwd)
oVWO.login_confirm()
