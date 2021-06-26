#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random
import sys
# ----------------------------------------------------------------------------------------------------
python = sys.executable #script restart
# ----------------------------------------------------------------------------------------------------
euid = os.geteuid()
if euid != 0:
    print ("""Script not started as root. Running sudo..
Script başlatilamiyor.Sistemde ROOT Kullanici olun..
    """)
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # the next line replaces the currently-running process with the sudo
    os.execlpe('sudo', *args)
# ----------------------------------------------------------------------------------------------------
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Toplu Penetrasyon Araci")

print("""Toplu Penetrasyon Aracina Hosgeldiniz.
icindekiler:
1)BruteForce Karsi Sifre Olusturma
2)Port Tarama
3)VPN Sunucusu Kontrol
4)Sunucu Zafiyet Analizi
5)Güvenlik Duvarı Tespiti
6)Exploit Arama
7)Port Servisleri Brute Force
8)Wordpress Site Zaafiyet Analizi
9)Worlist Olusturma
""")
secim=int(input("Lütfen Secim Yapiniz:"))

# ----------------------------------------------------------------------------------------------------
if (secim==1): #pass generator
        os.system("clear")
        os.system("figlet Sifre Olusturucu")
        print ("""
Şifre Oluşturma Aracına Hoşgeldiniz. Sudo Su komutuyla sistemde root olmanızı öneriyorum.Eğer permission denied hatası alırsanız root olduktan sonra tekrar deneyin.
Brute Force(Kaba Kuvvet Saldırısı) önlem olarak güvenli şifre üretir. Oluşturulan Şifre eğer güvenli değilse sizi uyararak bildirir.

1)Şifre Oluşturmak için açılan terminale "1" yazın.
2)Ana Menü için "0" yazın.



        """)

        islemno=int(input("İşlem Numarasını Girin:"))

        if (islemno==1):

        # -*- coding: utf-8 -*-
            sifreler=[]
            bharf=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "Y", "Z", "X"]
            kharf=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "z", "x"]
            oharf=["!","%","?","*","#"]
            rakam=["0","1","2","3","4","5","6","7","8","9"]
            genel=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "Y", "Z","X","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "y", "z", "x","!","%","?","*","#","0","1","2","3","4","5","6","7","8","9"]

            for i in range(10):
                secim=[0,1,2,3]
                x=""

                for j in range(4):
                    k=random.choice(secim)

                    if k==0:
                        x+=random.choice(bharf)
                    elif k==1:
                        x+=random.choice(kharf)
                    elif k==2:
                        x+=random.choice(oharf)
                    else:
                        x+=random.choice(rakam)
                    secim.remove(k)

                for kalan in range(4):
                    x+=random.choice(genel)

                sifreler.append(x)
            print (("Olusturulan Sifreler Listesi===>"),sifreler)
            for i in sifreler:
                for j in range(4):
                    if i[j] in rakam and i[j+1] in rakam:
                        print (i,("sifresi yan yana iki rakam bulundugundan dolayi kullanim acisindan onerilmemektedir.."))
            f = open("passwordgenerator.txt", "w")
            f.write(str(sifreler))    
            f.close()


            print ("Bu dizinin oldugu alana password-generator adinda bir txt dosyasi olusturuldu...")

        elif (islemno==0):
            os.execl(python, python, * sys.argv)
        else:
            print("Yanlis bir ifade girdiniz program kapatildi!")
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
elif (secim==2):
    os.system("clear")
    os.system("apt-get install nmap -y")
    os.system("clear")
    os.system("figlet Port Tarama")
    print(""" Port Tarama Uygulamasina Hosgeldiniz. 
        
        1) Hizli Tarama
        2) Servis ve Versiyon Bilgisi
        3) Isletim Sistemi Bilgisi
        0) Ana Menuye dönmek icin
        
        """)
    hedefip=raw_input("Hedef IP Girin: ")    
    portislem=int(input("Islem numarasi giriniz: "))
    if (portislem==1):        
            os.system("nmap "+hedefip)
    elif (portislem==2):
            os.system("nmap -sS -sV "+hedefip)
    elif (portislem==3):
            os.system("nmap -O"+hedefip)
    elif (portislem==0):
            os.execl(python, python, * sys.argv)
    else:
            print("Hatali bir secim yaptiniz program kapatiliyor.")
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
elif (secim==3):
    os.system("apt-get install ike-scan -y")
    os.system("clear")
    os.system("figlet VPN Kontrol")
    print ("""Hosgeldiniz.. VPN Kontrolu icin ip adresi girin..
1)VPN sunucusunu kontrol etmek
2)Ana menuye donmek icin""")
    vpnislem=int(input("Islem numarasini secin: "))
    hedefip=raw_input("Hedef IP Girin: ")
    if (vpnislem==1):
        os.system("ike-scan "+ hedefip)
    else:
        os.execl(python, python, * sys.argv)
elif (secim==4):
    os.system("apt-get install nikto -y")
    os.system("clear")
    os.system("figlet Zaafiyet Analizi")
    print ("""
Hosgeldiniz.. Zaafiyet analizi icin ip adresi girin..
1)Zaafiyet analizini baslatmak icin
not: Sistemde bir zaafiyet bulursa Exploitleriyle birlikte size bir cikti verir..
2)Ana menuye donmek icin""")
    niktosec=int(input("Seciminizi yapin: "))
    hedefip=raw_input("Hedef IP Girin: ")
    if (niktosec==1):
        os.system("nikto -h"+ hedefip)
    else:
        os.execl(python, python, * sys.argv)
elif (secim==5):
    os.system("apt-get install wafw00f")
    os.system("clear")
    os.system("figlet Guvenlik Duvari Tespiti")
    print ("""
Hosgeldiniz.. Güvenlik Duvari Tespiti icin site adresi girin..
1)Guvenlik Duvari Tespiti icin
2)Ana menuye donmek icin""")
    wafsecim=str(raw_input("Site Adresi Girin:"))
    if (wafsecim==1):
        os.system("wafw00f "+wafsecim)
    else:
        os.execl(python, python, * sys.argv)
elif (secim==6):    
    os.system("clear")
    os.system("figlet Exploit Arama")
    print ("""
Hosgeldiniz.. Veritabanında Exploit arama işlemi icin seciminizi girin..
1)Exploit aramak icin
2)Ana menuye donmek icin""")
    exploitsecim=int(input("Seciminizi Girin:"))
    anahtar=str(raw_input("Anahtar Kelime Girin:"))
    if (exploitsecim==1):
        os.system("searchsploit "+ anahtar)
    else:
        os.execl(python, python, * sys.argv)
elif (secim==7):
    os.system("apt-get install ncrack -y")    
    os.system("clear")
    os.system("figlet Port Kaba Kuvvet")
    print ("""
Hosgeldiniz.. Portlara yönelik kaba kuvvet işlemi icin seciminizi girin..
1) FTP
2) SSH
not:(telnet,http,smb gibi diğer portlar yakında gelecek..)
3)Ana menuye donmek icin""")
    portislemno=raw_input("Islem Numarasi Girin:")
    porthedefip=raw_input("Hedef IP adresini girin:")
    kullaniciadi=raw_input("Kullanici Adi Wordlist Yolu:")
    sifre=raw_input("Sifrelerin bulundugu dosya yolu:")
    if (portislemno==1):
        os.system("ncrack -p 21 -U"+ kullaniciadi + " -P " + sifre + " " + porthedefip)
    elif (portislemno==2):
        os.system("ncrack -p 22 -U"+ kullaniciadi + " -P " + sifre + " " + porthedefip)
    else:
        os.execl(python, python, * sys.argv)
elif (secim==8): 
    os.system("apt-get install wpscan -y")
    os.system("clear")
    os.system("figlet Wordpress Tarama")
    print ("""
Hosgeldiniz.. Wordpress Zaafiyet Tespit islemleri icin seciminizi girin..
1)Hizli Tarama
2)Eklenti Tarama
3)Tema Tarama
4)Yonetim Kullanici adi tarama
5)Ana menuye donmek icin
Not:Update Sorarsa Y yazip bekleyin..""")
    wpsecim=str(raw_input("Seciminizi Girin: "))
    siteadresi=raw_input("Site Adresi Girin: ")
    if (wpsecim==1):
        os.system("wpscan --url "+ siteadresi)
    elif (wpsecim==2):
        os.system("wpscan --url "+ siteadresi + " --enumerate p")
    elif (wpsecim==3):
        os.system("wpscan --url "+ siteadresi + " --enumerate t")
    elif (wpsecim==4):
        os.system("wpscan --url "+ siteadresi + " --enumerate u")
    else:
        os.execl(python, python, * sys.argv)
elif (secim==9):
    os.system("apt-get install crunch -y")
    os.system("clear")
    os.system("figlet Wordlist Olusturma")
    print ("""
Hosgeldiniz.. Wordlist olusturmak icin seciminizi girin..
1)Wordlist Olusturma
2)Ana Menuye donme
""")
    wordlistsecim=int(raw_input("Seciminizi girin:"))
    if (wordlistsecim==1):
        print("Olusturulacak Wordlistte ki Degerleri Girin")
        minkarakter=int(raw_input("Minimum Karakter Sayisi: "))
        maxkarakter=int(raw_input("Maksimum Karakter Sayisi: "))
        try: input=raw_input
        except NameError: pass
        karakter=input("Kullanacaginiz Karakterleri Girin: ")
        print("Ornek Kullanim: /home/kali/Desktop/parola.txt")
        kayityeri=(raw_input("Wordlistin kaydedilmesi istediginiz dizini girin:"))
        os.system("crunch "+ str(minkarakter) +" "+ str(maxkarakter) + " " + str(karakter) + " -o " + str(kayityeri))
        print("islem tamamlandi.. Parola dosyasi konumu: "+str(kayityeri))
    else:
        os.execl(python, python, * sys.argv)
else:
    print ("Hatali Bir Secim Yaptiniz Program Kapatiliyor....!!")
