import paramiko

t = paramiko.Transport("10.10.2.3", 22)

t.connect(username="bender", password="alta3")

sftp = paramiko.SFTPClient.from_transport(t)

sftp.put("chal_02.py", "/home/bender/sams_challenge.py")

sftp.close()
