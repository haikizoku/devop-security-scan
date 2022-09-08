#!/usr/bin/python3
import sys
import nmap3
import simplejson as json

network = nmap3.Nmap()
results = network.scan_top_ports("192.168.68.126", args="-sn")

with open(results, 'w') as json_file:
        print(json.dump(results, json_file, indent=4))
