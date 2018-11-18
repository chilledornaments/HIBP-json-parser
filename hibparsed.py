#!/usr/bin/env python3
import argparse, json, time, sys

parser = argparse.ArgumentParser(description="A tool to parse HIBP records")
parser.add_argument('pwndfile', help="Path to file to parse")
parser.add_argument('--skip-breach', dest='Breach', default="None", action="store", help="Skip a specific breach")
args = parser.parse_args()

FILE = args.pwndfile
SKIP_BREACH = args.Breach
if SKIP_BREACH is "None":
    print("Returning info for all breaches")
    SKIP_STATUS = "N"
else:
    print("Skipping breach: %s" %SKIP_BREACH)
    SKIP_STATUS = "Y"

# Sensitive breach docs: https://haveibeenpwned.com/FAQs#SensitiveBreach

with open(FILE, "r") as F:
    json_data = json.load(F)
    COUNT = 0
    PASSWORD_COUNT = 0
    if SKIP_STATUS == "Y":
        while True:
            try:
                ALIAS = json_data["BreachSearchResults"][COUNT]["Alias"]
                BREACH = json_data["BreachSearchResults"][COUNT]["Breaches"][0]["Title"]
                SENSITIVE = json_data["BreachSearchResults"][COUNT]["Breaches"][0]["IsSensitive"]
                DATA_LEAKED = json_data["BreachSearchResults"][COUNT]["Breaches"][0]["DataClasses"]
                if BREACH == SKIP_BREACH:
                    COUNT += 1
                else:
                    print("Alias: %s " %ALIAS)
                    print("Breach: %s" %BREACH)
                    if SENSITIVE is True:
                        print("SENSITIVE BREACH")
                    else:
                        print("Not sensitive")
                    for item in DATA_LEAKED: 
                        print("Data leaked: %s" %item)
                        if item == "Passwords":
                            print("PASSWORD COMPROMISED FOR: %s" %ALIAS)
                            PASSWORD_COUNT += 1
                        elif item == "Password hints":
                            print("PASSWORD HINT COMPROMISED FOR: %s" %ALIAS)
                            PASSWORD_COUNT += 1
                    COUNT += 1
            except IndexError:
                print("Ran through index of: "+str(COUNT))
                break

    # We aren't skipping a breach
    else:
        while True:
            try:
                ALIAS = json_data["BreachSearchResults"][COUNT]["Alias"]
                BREACH = json_data["BreachSearchResults"][COUNT]["Breaches"][0]["Title"]
                SENSITIVE = json_data["BreachSearchResults"][COUNT]["Breaches"][0]["IsSensitive"]
                DATA_LEAKED = json_data["BreachSearchResults"][COUNT]["Breaches"][0]["DataClasses"]
                COUNT += 1
                #time.sleep(1)
                print("Alias: %s" %ALIAS)
                print("Breach: %s" %BREACH)
                if SENSITIVE is True:
                    print("SENSITIVE BREACH")
                else:
                    print("Not sensitive")
                for item in DATA_LEAKED: 
                    print("Data leaked: %s" %item)
                    if item == "Passwords":
                        print("PASSWORD COMPROMISED FOR: %s" %ALIAS)
                        PASSWORD_COUNT += 1
                    elif item == "Password hints":
                        print("PASSWORD HINT COMPROMISED FOR: %s" %ALIAS)
                        PASSWORD_COUNT += 1
                    
                print("")
            except IndexError:
                print("Ran through index of: "+str(COUNT))
                break

    F.close()
print("TOTAL COMPROMSED PASSWORDS/HINTS: "+str(PASSWORD_COUNT))