#! /usr/bin/python3

import nmap

nm = nmap.PortScanner()

scan_range = nm.scan('192.168.186.132')

print(scan_range['scan'])