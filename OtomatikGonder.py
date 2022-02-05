from multiprocessing import AuthenticationError
import paramiko
import os
import sys
from dotenv import load_dotenv
from paramiko import SSHException
load_dotenv()
hostname = os.environ.get('HOSTNAME')
username = os.environ.get('USERNAME')
ssh_key = os.environ.get('SSH_KEY')
local_path = os.listdir("/home/omertahaoztop/Masaüstü/GönderilecekKitaplar/")
remote_path = os.environ.get('REMOTE_PATH')

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    for file in local_path:
        if file.endswith(".pdf") or file.endswith(".epub") or file.endswith(".mobi") or file.endswith(".docx"):
            client.connect(hostname=hostname, username=username, key_filename=ssh_key)
            sftp = client.open_sftp()
            sftp.put(file, remote_path + file)
            print("{} dosyası başarıyla gönderildi. / {} File is successfully sent".format(file,file))
            os.remove('/home/omertahaoztop/Masaüstü/GönderilecekKitaplar/' + file)
            print("Yerelde bulunan Dosya silindi / File is deleted from local")
        else:
            print("Dosya bulunamadı / File not found")
except AuthenticationError:
    print("Lütfen bilgilerinizi kontrol ediniz. / Please check your credentials.")
except SSHException:
    print("SSH Bağlantısında hata / SSH connection error.")
