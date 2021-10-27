#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os
import getpass

while True:
    ## where to connect to
    ex = input("Continue? (Y/n)").lower()
    print(ex)
    if ex == "n" or ex == "no":
        break
    elif ex == "" or ex == "y" or ex == "yes":
        ip = input("What's the IP? ")
        un = input("How bout that username? ")
        ps = getpass.getpass("What's the secret password? ")
        
        t = paramiko.Transport(ip, 22) ## IP and port
        
        ## how to connect (see other labs on using id_rsa private/public keypairs)
        t.connect(username=un, password=ps)
        
        ## Make an sftp connection object
        sftp = paramiko.SFTPClient.from_transport(t)
        
        ## iterate across the files within directory
        for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
          if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
            sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location
        
        ## close the connection
        sftp.close() # close the connection
    else:
        print("Type yes or no silly")
