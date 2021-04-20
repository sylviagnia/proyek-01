import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text,'html.parser');
print ('Menampilkan objek html')
print ('======================')
print (obj)
print ('\nMenampilkan title browser dengan tag')
print ('======================================')
print(obj.title)
print ('\nMenampilkan title browser tanpa tag')
print ('=====================================')
print(obj.title.text)
print ('\nMenampilkan semua tag h2')
print ('==========================')
print(obj.find_all('h2'))
print ('\nMenampilkan semua teks h2')
print ('===========================')
for headline in obj.find_all('h2'):
    print (headline.text)
    print ('\nMenampilkan headline berdasarkan div class')
    print ('============================================')
    print (obj.find_all('div',class_='bungkus_txt_headline_center'))
    print ('\nMenampilkan semua teks headline')
    print ('=================================')
    for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
        print(headline.find('h2').text)
        print ('\nMenyimpan headline pada file text')
        print ('===================================')
        f=open('D:\\headline.txt','w')
        for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
            f.write(headline.find('h2').text)
            f.write('\n')
        f.close()
