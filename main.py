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
sftp.put('vulmap-linux.py','/home/gn/destination.txt' )
sftp.close()
print ("copied successfully!")
   
# redirecting all the output in cmd_output
# variable
cmd_output = stdout.read()
print('log printing: ', command, cmd_output)
