# pylint:disable=import-error, broad-exception-caught,too-many-instance-attributes, too-many-arguments
""" This module connect with database and fetch result"""
import sys
from dbconnection import PostgresConnection
from dbaction import PostgresAction
from applicationaction import ApplicationAction

def main():
    """This entry point of the program"""
    connection = PostgresConnection(database="postgres",\
             user="sheikjb_new",\
             password="sample",\
             host="localhost",\
             port=5432)

    #creating connection cursor
    connect_object = connection.setup_connection()
    action_object = PostgresAction()
    appaction = ApplicationAction()
    userchoice = int(input('Please enter choices \n1 - Login  \
                           \n2 - Signup  \n3 - Quit \nYour Choice :  '))
    match userchoice:
        case 1:
            #login code
            appaction.login(action_object,connect_object)
        case 2:
            #signup code
            appaction.singup(action_object,connect_object)
        case 3:
            sys.exit('Thanks for visiting us')
        case _:
            print('Please select valid input next time')

if __name__ == "__main__":
    main()
