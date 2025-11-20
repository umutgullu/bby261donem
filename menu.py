
def menuyu_goster(root,oyunu_baslat,skor_penceresi):
    import tkinter as tk

    def basla_butonu_tiklandi():
        oyunu_baslat()
        menu_pencere.destroy()

    def skor_butonu_tiklandi():
        skor_penceresi()

    menu_pencere = tk.Toplevel(root)
    menu_pencere.title("Mayın Tarlası Menüsü")

    kurallar = """NASIL OYNANIR?
    1. Yeşil kutuları bulmaya çalış.
    2. Kırmızı mayınlara basarsan yanarsın!
    3. Sayılar etraftaki mayın sayısını gösterir.
    4. Şüphelendiğin yere sağ tıklayıp işaretle (Yakında!)."""

    lbl_kurallar = tk.Label(menu_pencere, text=kurallar, font=("Arial", 10), justify="center", fg="darkblue")
    lbl_kurallar.pack(pady=10)
    
    basla_buton = tk.Button(menu_pencere, text="Oyunu Başlat", command=basla_butonu_tiklandi)
    basla_buton.pack(pady=10)

    skor_buton = tk.Button(menu_pencere, text="Skorları Görüntüle", command=skor_butonu_tiklandi)
    skor_buton.pack(pady=10)

    cikis_buton = tk.Button(menu_pencere, text="Çıkış", command=root.quit)
    cikis_buton.pack(pady=10)
    