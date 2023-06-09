"""This Module is responsible for performing all the application access """
import sys
from otp_validation import OtpValidation



class ApplicationAction:
    """This class contains all the methodes which perform application actions"""
    def __init__(self):
        pass

    def login_user_ask(self):
        """This function is responsible for taking user inputs"""
        username = input('Enter Username : ')
        passwd = input('Enter password : ')
        return (username,passwd)

    def singup_user_ask(self):
        """This function responsible for taking user input for singh up"""
        first_name = input('Enter FirstName : ')
        last_name = input('Enter LastName : ')
        email_adress = input('Enter Email Address : ')
        phone_number = input('Enter Phone Number : ')
        username = input('Enter Username : ')
        passwd = input('Enter password : ')
        return (first_name,last_name,email_adress,phone_number,username,passwd)   

    def login(self,action_object,connect_object):
        """This function used to perform login operation"""
        username,passwd = self.login_user_ask()
        query = f"select * from auth where username='{username}'"
        columnname = ["username","password","phone_number","email_adress","first_name","last_name"]
        
        try:
            result = action_object.excute_qurey(connect_object,query)
            print(result)
            result = result.fetchall()
            dataframe = action_object.create_dataframe(result,columnname)
            dataframe = dataframe[['username','password']]
            if dataframe['username'].get(0) == username:
                if dataframe['password'].get(0) == passwd:
                    print('Login Successfully..!')                
                else:
                    sys.exit(f"Incorrect Password for the use {username}")
            else:
                print("User does not exist, please signp !!")
        except ValueError:
            print('username and password not found')



    def singup(self,action_object,connect_object):
        """This function used to perform singup operation"""
        first_name,last_name,email_adress,phone_number,username,passwd = self.singup_user_ask()
        otpv = OtpValidation(email_adress)
        if otpv.otpvalidation():
            query = f"insert into auth (first_name,last_name,email_adress,phone_number,username,password) \
                values('{first_name}','{last_name}','{email_adress}','{phone_number}','{username}','{passwd}')"
            action_object.excute_qurey(connect_object,query).execute("commit")
            print("Signup Successfully")

