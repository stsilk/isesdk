import ipaddress

#Class to handle cisco ISE session
class ISE:

    __ip = ''
    __username = ''
    __password = ''

    def __init__(self, username, password, ip):
        self.__username = username
        self.__password = password
        self.ip = ip

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
        self.__password = self.value

    @ip.setter
    def ip(self, value):
        try:
            ipaddress.ip_address(value)
            self.__ip = value
        except ValueError as e:
            print(e)
        


