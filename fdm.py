# First import required python modules

import requests
import yaml
import json
from pprint import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from crayons import blue, green, white, red, yellow,magenta, cyan

# Second Let's add some global variable
    # we have no global variable in this example

# Third let's define some functions

def fdm_login(ipaddr,username,password,version):
    '''
    This is the normal login which will give you a ~30 minute session with no refresh.  
    '''
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization":"Bearer"
    }
    payload = {"grant_type": "password", "username": "admin", "password": "Sbxftd1234!"}

    request = requests.post("https://{}:{}/api/fdm/v{}/fdm/token".format(ipaddr, FDM_PORT,version),json=payload, verify=False, headers=headers)
    if request.status_code == 400:
        raise Exception("Error logging in: {}".format(request.content))
    try:
        access_token = request.json()['access_token']
        print (green("Token = "+access_token))  
        return access_token        
    except:
        raise

def fdm_get_hostname(ipaddr,token,version):
    '''
    This is a GET request to obtain system's hostname.
    We will use it to verify that the token we got works
    '''
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization":"Bearer {}".format(token)
    }
    try:
        request = requests.get("https://{}:{}/api/fdm/v{}/devicesettings/default/devicehostnames".format(ipaddr, FDM_PORT,version),
                           verify=False, headers=headers)
        return request.json()
    except:
        raise

# Here under our main function from which are called all above functions
# Note: name and main in the next line should have two underscores __ on either side.
if __name__ == "__main__":
    #  load FDM IP & credentials here under
    FDM_USER = "admin"
    FDM_PASSWORD = "Sbxftd1234!"
    FDM_IP_ADDR = "10.10.20.65"
    FDM_PORT = "443"
    FDM_VERSION = "5"# mandatory for FTD 6.6 API version

    token = fdm_login(FDM_IP_ADDR,FDM_USER,FDM_PASSWORD,FDM_VERSION)

    print()    
    print(yellow("BINGO ! You got a token ! :",bold=True))
    print()     
    print()     
    print ('==========================================================================================')
    print()
    x=input("Let's check it. Type Enter")
    hostname = fdm_get_hostname(FDM_IP_ADDR,token,FDM_VERSION)
    print ('JSON HOSTNAME IS =')
    print(json.dumps(hostname,indent=4,sort_keys=True))    
    print()
    print(green('  ===>  ALL GOOD !',bold=True))
    print()
