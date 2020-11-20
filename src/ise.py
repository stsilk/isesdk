import ipaddress
import subprocess
import platform

#Class to handle cisco ISE session
class ISE:

    __ip = ''
    __username = ''
    __password = ''
    __baseURL = ''

    def __init__(self, username, password, ip):
        self.username = username
        self.password = password
        self.ip = ip
        self.clientSystem = platform.system()

    def verifyConnection(self):
        print("Pinging ISE Server...")
        if self.clientSystem == 'Windows':
            params = '-n 1 -w 5'
        else:
            params = '-c 1' 
        command = ['ping', params, self.ip]  
        try:
            subprocess.check_output(command)
            print("Successfully pinged server @ {0}".format(self.ip))
        except Exception as e:
            print("Failed to ping server @ {0}".format(self.ip))
            return 

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def ip(self):
        return self.__ip

    @username.setter
    def username(self, value):
        self.__username = value
    
    @password.setter
    def password(self, value):
        self.__password = value

    @ip.setter
    def ip(self, value):
        try:
            ipaddress.ip_address(value)
            self.__ip = value
        except ValueError as e:
            print(e)
        


