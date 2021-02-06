#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random

os.system("apt-get install figlet")
os.system("apt-get update")
os.system("clear")
os.system("figlet Toplu Penetrasyon Araci")

print("""Toplu Penetrasyon Aracina Hosgeldiniz.
icindekiler:
1)BruteForce Karsi Sifre Olusturma
2)Port Tarama""")
secim=int(input("Lütfen Secim Yapiniz:"))
if (secim==1):
        print ("""
        Şifre Oluşturma Aracına Hoşgeldiniz. Sudo Su komutuyla sistemde root olmanızı öneriyorum.Eğer permission denied hatası alırsanız root olduktan sonra tekrar deneyin.
        Brute Force(Kaba Kuvvet Saldırısı) önlem olarak güvenli şifre üretir. Oluşturulan Şifre eğer güvenli değilse sizi uyararak bildirir.

        1)Şifre Oluşturmak için açılan terminale "1" yazın.
        2)Çıkmak için "2" yazın.



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

        elif (islemno==2):
            print("Program kapatılıyor.")
        else:
            print("Yanlis bir ifade girdiniz program kapatildi!")
elif (secim==2):
    os.system("clear")
    os.system("apt-get install nmap")
    os.system("clear")
    os.system("figlet Port Tarama")
    print(""" Port Tarama Uygulamasina Hosgeldiniz. 
    
    1) Hizli Tarama
    2) Servis ve Versiyon Bilgisi
    3) Isletim Sistemi Bilgisi
    
    """)
    hedefip=int(input("Hedef IP Girin: "))
    portislem=int(input("Islem numarasi giriniz: "))
    if (portislem==1):        
        os.system("nmap "+hedefip)
    elif (portislem==2):
        os.system("nmap -sS -sV "+hedefip)
    elif (portislem==3):
        os.system("nmap -O"+hedefip)
    else:
        print("Hatali bir secim yaptiniz program kapatiliyor.")


