## Dosyalar,Karakter Dizileri,Döngüller,Koşullar,Kaçış Karakterleri##
##Öğrenci ekleme ve öğrenci silme aktif++++++++++++++++
##Dvevamsızlık eksik-----------------------------------
##Bilgi Güncelleme tamam+++++++++++++++++++++++++++++++
##Not girişi eksik-------------------------------------
##İstenmeye veri girişleri önlem alınmadı--------------
##Kullanıcı adı parola ile giriş eksik-----------------
secim=0
kontrol=0
with open("dosya/logger.txt","r+") as dosya:
    secim=int(input("Okuma için 1 yazma için 2"))
    if secim==1:
     veri=dosya.read().split("\n")
     arama=input(str("Öğrenci Numarasını Gir:>"))
     for i in range(len(veri)):
         if arama in veri[i]:
             kumar=veri[i].split(" ")
             print(kumar)

    else:
      with open("dosya/logger.txt", "a+") as dosya2:

        yazsec=input(str("""
        Öğrenci eklemek için 1
        Öğrenci Silmek İçin 2
        Bilgi güncellemk için 3
        Not girişi için 4
        devamsızlık girişi için 5
        >>>> """))
        ##### ÖĞRENCİ EKLEME BAŞLANGIÇ###############
        if yazsec=="1":
            ad=input(str("Öğrenci Adını Girin>>>"))
            soyad=input(str("Öğrenci Soyad Girin>>>"))
            telefon=int(input("Öğrenci telefon numarası>>>"))
            dogum=input(str("Öğrenci doğum tarihi gün.ay.yıl şeklinde>>>"))
            numara=int(input("Öğrenci numarasını girin>>"))
            #yas=
            eklenecek=str(numara)+" "+ad+" "+soyad+" "+str(telefon)+" "+dogum+"\n"
            listex=[eklenecek]
            dosya2.writelines(listex)
            ### ÖĞRENCİ EKLEME BİTİŞ<<<<<<<<<<
            #-----------------------------------------------------------#

##         DEVAMSIZLIK GİRİŞİ BÖLÜMÜÜ###################
        elif yazsec=="5":
            print("Devamsızlık Modülü Aktif Değil!!\n")
            asddas=input("Çıkmak için enter")
        #####  DEVAMSIZLIK GİRİŞİ BİTİŞ##########
        elif yazsec=="2":
             jargon=[]
             with open("dosya/logger.txt", "r+") as dosya2:
               veri=dosya.read()
               jargon=veri.split("\n")
               print(jargon)
               sayy=input(str("Numara gir"))
               print(str(len(jargon)))
               hsdf=input("sdsdsd")
               i=0
               while i<len(jargon):
                   if sayy in jargon[i]:

                     jargon.pop(i)
                     for i in range(len(jargon)):
                         jargon[i]+="\n"
                     with open("dosya/logger.txt", "w") as dosya3:

                       dosya3.writelines(jargon)
                       i+=1
                   else:
                       i+=1
                       continue

          ####################### BİLGİ GÜNCELLEME BAŞLANGIÇ#####################
        elif yazsec=="3":

             jargon = []
             with open("dosya/logger.txt", "r+") as dosya2:
                 veri = dosya.read()
                 jargon = veri.split("\n")
                 print(jargon)
                 sayy = input(str("Numara gir"))
                 i = 0
                 while i < len(jargon):
                     if sayy in jargon[i]:
                        print(jargon[i])
                        hangisi=input(str("""İsim güncellemk için 1
                        Soyad güncellemek için 2
                        Telefon numarası Güncellemek için 3
                        Doğum tarihi güncellemek için 4
                        >>>"""))
                        if hangisi=="1":

                            ad = input(str("Yeni Adı Girin:>>"))
                            komodor = jargon[i]
                            jargon[i] = ""
                            komodor = komodor.split(" ")
                            komodor[1] = ad
                            komodor = " ".join(komodor)
                            print(jargon)
                            jargon[i] = komodor
                            print(jargon)
                            for i in range(len(jargon)):
                                if jargon[i] == "":
                                    continue
                                else:
                                    jargon[i] += "\n"
                        elif hangisi=="2":
                            soyad=input(str("Yeni Soyadı Girin:>>"))
                            komodor=jargon[i]
                            jargon[i]=""
                            komodor=komodor.split(" ")
                            komodor[2]=soyad
                            komodor=" ".join(komodor)
                            print(jargon)
                            jargon[i]=komodor
                            print(jargon)
                            for i in range(len(jargon)):
                                if jargon[i]=="":
                                    continue
                                else:
                                    jargon[i]+="\n"

                        elif hangisi=="3":
                            telefon = input(str("Yeni Telefon Numarası Girin:>>"))
                            komodor = jargon[i]
                            jargon[i] = ""
                            komodor = komodor.split(" ")
                            komodor[3] = telefon
                            komodor = " ".join(komodor)
                            print(jargon)
                            jargon[i] = komodor
                            print(jargon)
                            for i in range(len(jargon)):
                                if jargon[i] == "":
                                    continue
                                else:
                                    jargon[i] += "\n"

                        elif hangisi=="4":
                            dogum = input(str("Yeni Doğum Girin:>>"))
                            komodor = jargon[i]
                            jargon[i] = ""
                            komodor = komodor.split(" ")
                            komodor[4] = dogum
                            komodor = " ".join(komodor)
                            print(jargon)
                            jargon[i] = komodor
                            print(jargon)
                            for i in range(len(jargon)):
                                if jargon[i] == "":
                                    continue
                                else:
                                    jargon[i] += "\n"

                        else:
                            print("Geçersiz Seçenek!!")
                            break

                        with open("dosya/logger.txt", "w") as dosya3:

                             dosya3.writelines(jargon)
                             i += 1
                     else:
                         i += 1
                         continue
 ########################### BİLGİ GÜNCELLEME BİTİŞ######################################################
