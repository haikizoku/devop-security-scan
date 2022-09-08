import paramiko
import sys

# Update the next three lines with your
# server's information
if len( sys.argv ) > 1:
    host = sys.argv[1]
    username = "gn"
    password = "gn"
    port ="22"
else:
    host = "192.168.247.138"
    username = "gn"
    password = "gn"
    port ="22"

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
local_path = str("/home/gn/Tp/devop-security-scan/result.txt")
remote_path = str("/home/gn/vulmap/result.txt")
sftp.get(remote_path,local_path)
sftp.close()

print ("get result")


