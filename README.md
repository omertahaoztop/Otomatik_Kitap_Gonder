## Türkçe
Yerel bilgisayarımda bulunan kitapların otomatik olarak sunucuya aktarılması
## English
Automatic transfer of books on my local computer to the server
## Cronjob (Her 30 dakikada bir / Every 30 minutes)
*/30 * * * * /usr/bin/python3 /home/omertahaoztop/Masaüstü/Yazılım/Python/Otomatik_Kitap_Gonder/OtomatikGonder.py >> /var/log/kitap.log 2>&1
