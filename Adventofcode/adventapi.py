#!/usr/bin/env python
import requests

# A simple API to receive level input effortlessly
# allowing more time and effort to be focused on solving the problem.

# use your own session cookie to recieve your personal input!
def levelInput(lvl,session='[redacted]'):
    cookies = dict(session=session)
    return requests.get("http://adventofcode.com/day/"+str(lvl)+"/input",cookies=cookies).text
