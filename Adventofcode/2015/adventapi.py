#!/usr/bin/env python
import requests

# A simple API to receive level input effortlessly
# allowing more time and effort to be focused on solving the problem.


# use your own session cookie to recieve your personal input!
def levelInput(lvl, year=2015, session='[redacted]'):
    cookies = dict(session=session)
    temp = requests.get("http://adventofcode.com/{}/day/{}/input".format(str(year), str(lvl)), cookies=cookies).text
    # temp = temp.split("\n")
    #if temp[-1] == "": 
    #    temp = temp[:-1]
    return temp
    
