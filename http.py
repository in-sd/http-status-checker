#!/usr/bin/env python

import requests

def request(url):
    try:
        return requests.get("http://" +url)
    except requests.exceptions.ConnectionError:
        pass

file=raw_input("enter subdomain file name:")
print("\n")
with open(file) as  subdomain:
         url=subdomain.read()
         url=url.splitlines()
         for line in url:
           
           res=request(line)
           print("\nsuccess\n",line,res)
