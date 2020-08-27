#!/usr/bin/python3
from urllib.request import urlopen
import json
import pandas as pd
import logging
logging.basicConfig(filename='/var/log/actions.log',level=logging.ERROR,
                    format="%(asctime)s:%(levelname)s:%(message)s")


def GetCoronaNationStats():
    """Get the National stats https://api.covid19india.org/data.json"""

    response = urlopen("https://api.covid19india.org/data.json")
    json_data = response.read().decode('utf-8', 'replace')
    d = json.loads(json_data)

    return(d["cases_time_series"][-1])

def GetCoronaStateStats(s_StateName):
    """Get the State status https://api.covid19india.org/data.json"""

    response = urlopen("https://api.covid19india.org/data.json")
    json_data = response.read().decode('utf-8', 'replace')
    d = json.loads(json_data)
    
    statewise  = d["statewise"]
    for x in statewise:
        if (s_StateName in x["state"].replace(" ", "").lower()):
            return(x)

def GetCoronaStateHospital(s_StateName):
    """Get the State status https://api.covid19india.org/data.json"""

    response = urlopen("https://api.rootnet.in/covid19-in/hospitals/medical-colleges")
    json_data = response.read().decode('utf-8', 'replace')
    d = json.loads(json_data)
    
    df = pd.DataFrame(d['data']['medicalColleges'], columns=["state","name","city","ownership","admissionCapacity","hospitalBeds"])
    states = set(df['state'])
    for x in states:
        if(s_StateName in x.replace(" ", "").lower()):
            #logging.error(str(list(df[df['state'] == x]['name'])))
            s_Data = str(list(df[df['state'] == x]['name']))
            s_Data = s_Data.replace("[","")
            s_Data = s_Data.replace("]","")
            return(s_Data)

if __name__ == "__main__":
    #print(GetCoronaStateStats("bengal"))
    print(GetCoronaStateHospital("kerala"))
