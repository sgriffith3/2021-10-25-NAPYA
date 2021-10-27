import paramiko

key = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

sess = paramiko.SSHClient()
sess.set_missing_host_key_policy(paramiko.AutoAddPolicy())

sess.connect(hostname="10.10.2.4", username="fry", pkey=key)
s_in, s_out, s_err = sess.exec_command("ls -al")
out = s_out.read().decode()
print(out)
sess.close()
