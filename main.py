import tkinter as tk
from tkinter import *
import random
root = tk.Tk()
root.title("Mayın Tarlası")
mesaj = tk.Label(root, text="", font=("Arial", 10))
mesaj.grid(row=5, column=0, columnspan=5, pady=10)

boyut = 5
mayin_sayisi = 5
tehlike_sayisi = 0
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
                    if 0 <= x < boyut and 0 <= y < boyut and alan[x][y] != 1:
                        alan[x][y] = "tehlike"
                        tehlike_sayisi += 1

guvenli_alan_sayisi = boyut * boyut - (mayin_sayisi+ tehlike_sayisi)
sayac=0
def tikla(i, j):
    global sayac
    if alan[i][j] == 1:
        butonlar[i][j].config(text="*", bg="red")
        mesaj.config(text="Mayına bastınız! Oyun bitti.")
        root.after(2000, root.destroy)
    elif alan[i][j] == "tehlike":
        butonlar[i][j].config(text="⚠", bg="yellow", state="disabled")
    else:
        butonlar[i][j].config(text="0", bg="green", state="disabled")
        sayac += 1
        if sayac == guvenli_alan_sayisi:
            mesaj.config(text="Tebrikler! Tüm güvenli alanları buldunuz.")
            root.after(2000, root.destroy)

butonlar = [[None for j in range(boyut)] for i in range(boyut)]
for i in range(boyut):
    for j in range(boyut):
        buton = tk.Button(root, text=" ", width=8, height=8, command=lambda i=i, j=j: tikla(i, j))
        buton.grid(row=i, column=j)
        butonlar[i][j] = buton

root.mainloop()