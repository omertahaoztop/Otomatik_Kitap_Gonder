## Türkçe
E-book formatında bulunan dosyaların kitap.omertahaoztop.com ismiyle bulunan sunucuda yerel klasörümden otomatik olarak eklenmesi.
## English
Automatic addition of files in e-book format from my local folder on the server with the name book.omertahaoztop.com.
## Cronjob (Her 30 dakikada bir / Every 30 minutes)
*/30 * * * * /usr/bin/python3 /home/omertahaoztop/Masaüstü/Yazılım/Python/Otomatik_Kitap_Gonder/OtomatikGonder.py >> /var/log/kitap.log 2>&1
