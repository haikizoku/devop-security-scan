import sys
import os
import nmap3    # import nmap.py module



try:
    nm = nmap.PortScanner()        # instantiate nmap.PortScanner object
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(1)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(1)

nm.scan('127.0.0.1', '22')     # scan host 127.0.0.1, ports from 22 to 443
nm.command_line()                  # get command line used for the scan : nmap -oX - -p 22-443
nm.scaninfo()                      # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
nm.all_hosts()
nm['127.0.0.1'].hostname()
nm['127.0.0.1'].state()
nm['127.0.0.1'].all_protocols()

if ('tcp' in nm['127.0.0.1']):
    list(nm['127.0.0.1']['tcp'].keys()) # get all ports for tcp protocol

nm['127.0.0.1'].all_tcp()           # get all ports for tcp protocol (sorted version)
nm['127.0.0.1'].all_udp()
nm['127.0.0.1'].all_ip()
nm['127.0.0.1'].all_sctp()

if nm['127.0.0.1'].has_tcp(22):     # is there any information for port 22/tcp on host 127.0.0.1
    nm['127.0.0.1']['tcp'][22]          # get infos about port 22 in tcp on host 127.0.0.1
    nm['127.0.0.1'].tcp(22)             # get infos about port 22 in tcp on host 127.0.0.1
    nm['127.0.0.1']['tcp'][22]['state'] # get state of port 22/tcp on host 127.0.0.1 (open

# a more usefull example :
for host in nm.all_hosts():
    print('----------------------------------------------------') 
    print('Host : {0} ({1})'.format(host, nm[host].hostname()))  
    print('State : {0}'.format(nm[host].state()))

    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : {0}' .format (proto))

        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print ('port : {0}\tstate : {1}'.format(port, nm[host][proto][port]['state']))

print(nm.csv())