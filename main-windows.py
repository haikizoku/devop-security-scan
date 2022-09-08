import paramiko
import sys
import os


#download last version of vulmap 
os.system("wget https://raw.githubusercontent.com/vulmon/Vulmap/master/Vulmap-Windows/vulmap-windows.ps1")


# Update the next three lines with your
# server's information
if len( sys.argv ) > 1:
    host = sys.argv[1]
    username = "gn"
    password = "gn"
    port ="22"
else:
    host = "192.168.247.141"
    username = "IEUSER"
    password = "Passw0rd!"
    port ="22"

# Create object of SSHClient and
# connecting to SSH
client = paramiko.client.SSHClient()
# AutoAddPolicy for missing host key to be set before connection setup.
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(host, username=username, password=password)
print ("Successfully connected to", host)

# create  directory
_stdin, _stdout, _stderr = client.exec_command('mkdir vulmap')
print (_stdout.readlines())
_stdin.close()
print ("directory created!")

sftp = client.open_sftp()
print (sftp)
sftp.put('vulmap-windows.ps1','vulmap/vulmap-windows.ps1' )
#stdin, stdout, stderr = client.exec_command('powershell iex(New-Object Net.WebClient).DownloadString("https://raw.githubusercontent.com/vulmon/Vulmap/master/Vulmap-Windows/vulmap-windows.ps1")')
#_stdin, _stdout, _stderr = client.exec_command(' powershell -nop  Get-Process -Name explorer | Out-File -FilePath c:\temp\process.txt')
#print (stdout.readlines())
#_stdin.close()
sftp.close()
print ("copied successfully!")

# execute command on client 

#commandPowershell="iex(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/vulmon/Vulmap/master/Vulmap-Windows/vulmap-windows.ps1')"
#_stdin, _stdout, _stderr = client.exec_command('powershell -nop -c ${commandPowershell}')

tdin, stdout, stderr = client.exec_command('powershell vulmap-windows.ps1 -SaveInventoryFile -InventoryOutFile pc0001.json')
print (_stdout.readlines())
tdin.close()
print ("script execution")

