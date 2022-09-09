import paramiko
import sys
import os
import host as configuration
# Update the next three lines with your
# server's information
if len( sys.argv ) > 1:
    host = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    port ="22"
else:
    host = configuration.host
    username = configuration.username
    password = configuration.password
    port ="22"

#download last version of vulmap 
os.system("wget https://raw.githubusercontent.com/vulmon/Vulmap/master/Vulmap-Linux/vulmap-linux.py")


# Create object of SSHClient and
# connecting to SSH
client = paramiko.client.SSHClient()
# AutoAddPolicy for missing host key to be set before connection setup.
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(host, username=username, password=password)
print ("Successfully connected to", host)

# below line command will actually
# execute in your remote machine

# create  directory
_stdin, _stdout, _stderr = client.exec_command('mkdir /home/gn/vulmap/')
print (_stdout.readlines())
_stdin.close()

sftp = client.open_sftp()
print (sftp)
sftp.put('vulmap-linux.py','/home/gn/vulmap/vulmap-linux.py' )
sftp.close()
print ("copied successfully!")


# execute command on client 
_stdin, _stdout, _stderr = client.exec_command('python3 /home/gn/vulmap/vulmap-linux.py -a > /home/gn/vulmap/result.txt')
print (_stdout.readlines())
_stdin.close()
print ("script execution")

# copy directory 
sftp = client.open_sftp()
print (sftp)
local_path = configuration.local_path
remote_path = configuration.remote_path
sftp.get(remote_path,local_path)
sftp.close()

print ("get result")