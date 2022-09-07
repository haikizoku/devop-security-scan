#!/usr/bin/python3
import sys
import nmap3
import simplejson as json


nmap = nmap3.Nmap()
nmapscan = nmap3.NmapScanTechniques()

#target = "192.168.1xx.xxx"
target = input("[+] Enter the target you want to scan : ")


def top_port_scan(target) :
    results_top_port_scan = nmapscan.scan_top_ports(target)
    print(json.dumps(results_top_port_scan , indent=4 , sort_keys=True))

def os_detection(target) :
    results_os_detection = nmapscan.nmap_os_detection(target)
    print(json.dumps(results_os_detection , indent=4 , sort_keys=True)) #MUST BE ROOT

def ver_detection(target):
    results_version_detection = nmapscan.nmap_version_detection(target)
    print(json.dumps(results_version_detection , indent=4 , sort_keys=True)) #MUST BE ROOT

def tcp_scan(target):
    results_tcp_scan = nmapscan.nmap_tcp_scan(target)
    print(json.dumps(results_tcp_scan , indent=4 , sort_keys=True))

def syn_scan(target):
    results_syn_scan = nmapscan.nmap_syn_scan(target)
    print(json.dumps(results_syn_scan , indent=4 , sort_keys=True)) 

print(""" nmap3scanner """)


ch = int(input("""
    CHOOSE FROM THE FOLLOWING SCAN OPTIONS
    [1] COMMON PORT SCAN
    [2] TCP SCAN ( -sT )   
    [3] TCP SYN SCAN ( -sS )
    [4] OS DETECTION ( -O ) {requires root privileges}
    [5] VERSION DETECTION ( -Sv ) {requires root privileges} : """))

if ch==1:
    top_port_scan(target)
elif ch==2:
    tcp_scan(target)
elif ch==3:
    syn_scan(target)
elif ch==4:
    os_detection(target)
elif ch==5:
    ver_detection(target)
else:
    print("INVALID OPTION")