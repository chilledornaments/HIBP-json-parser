#!/usr/bin/env python3
import argparse, json, time

parser = argparse.ArgumentParser(description="A tool to parse HIBP records")
parser.add_argument('pwndfile', help="Path to file to parse")
args = parser.parse_args()
FILE = args.pwndfile

# Sensitive breach docs: https://haveibeenpwned.com/FAQs#SensitiveBreach

with open(FILE, "r") as F:
    json_data = json.load(F)
    COUNT = 0
    while True:
        try:
            ALIAS = json_data["BreachSearchResults"][COUNT]["Alias"]
            BREACH = json_data["BreachSearchResults"][COUNT]["Breaches"][0]["Title"]
            SENSITIVE = json_data["BreachSearchResults"][COUNT]["Breaches"][0]["IsSensitive"]
            DATA_LEAKED = json_data["BreachSearchResults"][COUNT]["Breaches"][0]["DataClasses"]
            COUNT += 1
            #time.sleep(1)
            print("Alias: "+ALIAS)
            print("Breach: "+str(BREACH))
            if SENSITIVE is True:
                print("SENSITIVE BREACH")
            else:
                print("Not sensitive")
            for item in DATA_LEAKED:
                print("Data leaked: "+item)
            print("")
        except IndexError:
            print("Index done at: "+str(COUNT))
            break
    F.close()