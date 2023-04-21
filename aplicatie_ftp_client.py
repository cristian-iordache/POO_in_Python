from ftplib import FTP

ftp = FTP()
ftp.connect()
ftp.login()
ftp.dir()
ftp.cwd()