# pylint:disable=import-error, broad-exception-caught,too-many-instance-attributes, too-many-arguments
"""This Module is Responsible for connecting to database"""
import sys
from psycopg2 import connect
class PostgresConnection:
    """ This is the class used to setup connection"""
    def __init__(self,database,user,password,host,port):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connect_object = None
        self.query = None
        self.query_cursor = None
        self.record_list = None
        self.columnname = None
        self.dataframe = None

    def setup_connection(self):
        """Setting up the connections"""
        try:
            con = connect(database=self.database,\
            user=self.user,\
            password=self.password,\
            host=self.host,\
            port=self.port)
        except Exception as genralexception:
            print('Connection Error due to some reason',genralexception)
            sys.exit("Exiting program due to database connectivity issue")
        else:
            print('Successfully established the connection , please proceed further')
            return con
        