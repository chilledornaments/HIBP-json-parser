# HIBP-json-parser
Parses json files from HIBP (https://haveibeenpwned.com) domain searches.

This was born out of me accidentally downloading a .json instead of a .xls file.

Run `./hibparsed.py filename` on a valid HIBP domain search json and the parser will spit out the alias, the breach, what was compromised, and if the breach contained sensitive information. 
