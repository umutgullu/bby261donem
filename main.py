import tkinter as tk
from tkinter import *
import random
import os
from menu import menuyu_goster
root = tk.Tk()
root.title("Mayın Tarlası")
mesaj = tk.Label(root, text="", font=("Arial", 10))
lbl_sure = tk.Label(root, text="Süre: 60", font=("Arial", 10, "bold"), fg="black")
# --- SABİT DEĞİŞKENLER ---
boyut = 5
mayin_sayisi = 5
puan = 0
sure = 60
sayac = 0
oyun_devam_ediyor = False 
tehlike_sayisi = 0
guvenli_alan_sayisi = 0
def skoru_kaydet(puan):
    with open("skor.txt", "a") as f:
        f.write(f"{puan}\n")
def skor_penceresi():
    skor_pencere=tk.Toplevel(root)
    skor_pencere.title("Liderlik Tablosu")
    skor_pencere.geometry("200x300")
    baslik=tk.Label(skor_pencere,text="En Yüksek Skorlar",font=("Arial",14))
    baslik.pack(pady=10)
    if not os.path.exists("skor.txt"):
        icerik="Henüz skor kaydı yok."
    else:
        with open("skor.txt","r") as f:
            puanlar=[]
            for satir in f.readlines():
                try:
                    puanlar.append(int(satir.strip()))
                except ValueError:
                    pass
        puanlar.sort(reverse=True)
        icerik=""
        for sira,no in enumerate(puanlar[:5],start=1):
            icerik+=f"{sira}. {no}\n"
    lbl_liste= tk.Label(skor_pencere,text=icerik,font=("Arial",12))
    lbl_liste.pack(pady=10)
def tikla(i, j):
    global sayac
    global puan
    global guvenli_alan_sayisi
    global mayin_sayisi
    global oyun_devam_ediyor
    if oyun_devam_ediyor == False:
        return
    if alan[i][j] == 1:
        butonlar[i][j].config(text="*", bg="red")
        mesaj.config(text=f"Mayına bastınız! Oyun bitti. Toplam Puanınız: {puan}")
        oyun_devam_ediyor = False
        tekrar_oyna_butonu_goster()
        skoru_kaydet(puan)
        skor_penceresi()
    elif alan[i][j] == "tehlike":
        butonlar[i][j].config(text="⚠", bg="yellow", state="disabled")
        puan+=50
        mesaj.config(text=f"Puanınız: {puan}")
    else:
        butonlar[i][j].config(text="0", bg="green", state="disabled")
        sayac += 1
        puan+=100
        kalan_guvenli_alan= guvenli_alan_sayisi - sayac
        mesaj.config(text=f"Kalan Güvenli Alanlar: {kalan_guvenli_alan} | Puanınız: {puan}")
    if sayac == guvenli_alan_sayisi:
        puan+=mayin_sayisi*100
        oyun_devam_ediyor = False
        mesaj.config(text=f"Tebrikler! Tüm güvenli alanları buldunuz. Toplam Puanınız: {puan}")
        tekrar_oyna_butonu_goster()
        skoru_kaydet(puan)
        skor_penceresi()
def geriye_say():
   global sure
   global oyun_devam_ediyor
   if oyun_devam_ediyor == False:
        return
   if sure > 0:
            sure -= 1
            lbl_sure.config(text=f"Kalan Süre: {sure} saniye")
            root.after(1000, geriye_say)
   else:
            mesaj.config(text="Süre doldu! Oyun bitti.")
            skoru_kaydet(puan)
            skor_penceresi()
            tekrar_oyna_butonu_goster()

def tekrar_oyna_butonu_goster():
    btn_tekrar = tk.Button(root, text="TEKRAR OYNA 🔄", font=("Arial", 12, "bold"), bg="black", fg="white", command=oyunu_baslat)
    btn_tekrar.grid(row=7, column=0, columnspan=5, pady=10)
    btn_cikis= tk.Button(root, text="ÇIKIŞ ❌", font=("Arial", 12, "bold"), bg="black", fg="white", command=root.destroy)
    btn_cikis.grid(row=8, column=0, columnspan=5, pady=5)
def oyunu_baslat():
    global alan, butonlar, oyun_devam_ediyor, tehlike_sayisi, guvenli_alan_sayisi, sayac, puan, sure
    root.deiconify()
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            widget.destroy()
    mesaj.grid(row=5, column=0, columnspan=5, pady=10)
    lbl_sure.grid(row=6, column=0, columnspan=5, pady=5)
    puan = 0
    sayac = 0
    sure = 60
    tehlike_sayisi = 0
    oyun_devam_ediyor = True
    
    mesaj.config(text="Oyun başladı! Mayınlara dikkat et.")
    lbl_sure.config(text=f"Süre: {sure} saniye")

    alan = [[0 for j in range(boyut)] for i in range(boyut)]
    mesaj.config(text=f"Mayın Sayısı: {mayin_sayisi}")
    mesaj.config(text="Mayına basma, sarılara dikkat et, yeşil alanları bul!")


    for _ in range(mayin_sayisi):
        i = random.randint(0, boyut - 1)
        j = random.randint(0, boyut - 1)
        while alan[i][j] == 1:
            i = random.randint(0, boyut - 1)
            j = random.randint(0, boyut - 1)
        alan[i][j] = 1


    for i in range(boyut):
        for j in range(boyut):
            if alan[i][j] == 1:
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < boyut and 0 <= y < boyut and alan[x][y]!="tehlike" and alan[x][y] != 1:
                            alan[x][y] = "tehlike"
                            tehlike_sayisi += 1
    guvenli_alan_sayisi = boyut * boyut - (mayin_sayisi+ tehlike_sayisi)

    butonlar = [[None for j in range(boyut)] for i in range(boyut)]
    for i in range(boyut):
        for j in range(boyut):
            buton = tk.Button(root, text=" ", width=8, height=8, command=lambda i=i, j=j: tikla(i, j))
            buton.grid(row=i, column=j)
            butonlar[i][j] = buton
    geriye_say()
root.withdraw()
menuyu_goster(root, oyunu_baslat, skor_penceresi)
root.mainloop()