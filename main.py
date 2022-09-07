import paramiko


# Update the next three lines with your
# server's information

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

sftp = client.open_sftp()
print (sftp)
sftp.put('vulmap-linux.py','/home/gn/vulmap-linux.py' )
sftp.close()
print ("copied successfully!")



# execute command on client 
_stdin, _stdout, _stderr = client.exec_command('python3 /home/gn/vulmap-linux.py -a')
print (_stdout.readlines())
_stdin.close()
