#! /usr/bin/env python3
from flask import Flask

import nmap3scanner2

app = Flask(__name__)

#app.config.from_object('config')

@app.route('/')
async def index():
    nmap3scannerresult = await nmap3scanner2.os_detection("127.0.0.1")
    return nmap3scannerresult 
#    return nmap3scanner2.os_detection("127.0.0.1")

if __name__=="__main__":
   app.run(host="0.0.0.0", port=80)

