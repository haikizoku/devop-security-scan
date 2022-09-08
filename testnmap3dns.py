import nmap3
nmap = nmap3.Nmap()
results = nmap.nmap_dns_brute_script("192.168.56.1")
print(results)