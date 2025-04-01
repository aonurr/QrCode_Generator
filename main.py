import qrcode
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
def veri_al():
    global photo
    qrurl=entry.get()
    bc=backcolor.get()
    fc=fillcolor.get()
    bc.lower()
    fc.lower()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qrurl)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fc, back_color=bc)
    img.save("qrcode.png")
    imag = Image.open("qrcode.png")
    photo = ImageTk.PhotoImage(imag)
    labelphoto.config(image=photo)


def qr_indir():
    dosya_yolu = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All Files", "*.*")]
    )
    if dosya_yolu:
        image = Image.open("qrcode.png")  # Önceden kaydedilen QR kodunu al
        image.save(dosya_yolu)  # Seçilen konuma kaydet

        # Seçilen dosya yolunu butonun üzerine yazdır
        button_indir.config(text=f"Kaydedildi: {dosya_yolu.split('/')[-1]}")

mscreen= tk.Tk()
mscreen.title("QR Code Generator By a.onur")
mscreen.geometry("800x600")

label = tk.Label(mscreen, text="Please Enter Url", font=("Arial", 14))
label.pack()
entry = tk.Entry(mscreen, font=("Arial", 12))
entry.pack(pady=10)
label1 = tk.Label(mscreen, text="Please BackGround Color", font=("Arial", 14))
label1.pack()
backcolor = tk.Entry(mscreen, font=("Arial", 12))
backcolor.pack(pady=5)
label2 = tk.Label(mscreen, text="Please Fill Color", font=("Arial", 14))
label2.pack()
fillcolor = tk.Entry(mscreen, font=("Arial", 12))
fillcolor.pack(pady=5)
labelphoto = tk.Label(mscreen)
labelphoto.pack()
button = tk.Button(mscreen, text="Generate QR", command=veri_al)
button.pack(pady=5)
button_indir = tk.Button(mscreen, text="Download QR", command=qr_indir)
button_indir.pack(pady=5)

qq=tk.PhotoImage
mscreen.mainloop()


#img.save("qrcode.png")"""
