import requests

class sgMapping:

    def __init__(self, ip, auth):
        self.endpoint = 'https://{0}:9060/ers/config/sgmapping'.format(ip)
        self.auth = auth

    def getAll(self):
        headers = {'ACCEPT': 'application/json'}
        response = requests.get(self.endpoint, 
                                headers=headers, 
                                auth=self.auth,
                                verify=False)
        return response.json()



