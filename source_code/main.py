from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

hunians = []
hunians.append(Apartemen("Nelly Joy", "A",12, 3, 3))
hunians.append(Rumah("Sekar MK", 3, 5, 2))
hunians.append(Indekos("Bp. Romi", "Cahya", "Rp. 10.000.000 per tahun"))
hunians.append(Rumah("Satria",2, 1, 4))
hunians.append(Apartemen("Azzahra", "B", 22, 7, 5))

gambar = []

def open_data_page():
    root.destroy()  # Menutup landing page
    data_page()  # Membuka halaman data seluruh residen


def data_page():
    root = Tk()
    root.title("Data Seluruh Residen")
    root.geometry("520x250+250+250")  


    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos":
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

        def details(index):
            top = Toplevel()
            top.title("Detail " + hunians[index].get_jenis())
            top.geometry("520x250+250+250")  # Mengatur ukuran dan posisi jendela

            d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
            d_frame.pack(padx=10, pady=10)

            d_summary = Label(d_frame, text="Summary: \n\n" + hunians[index].get_detail(), anchor="w", justify="left").grid(row=0, column=0, sticky="w")
            
    

            btn = LabelFrame(top, padx=0, pady=0)
            btn.pack(padx=10, pady=10)
            b_close = Button(btn, text="Close", command=top.destroy)
            b_close.grid(row=0, column=0)


root = Tk()
root.title("Praktikum DPBO Python")
root.geometry("520x250+250+250")  

label = Label(root, text="Selamat datang di HAHA HIHI HUHUnian")
label.pack(pady=20)

# objek tkinter ImageTk
img = Image.open("05_PyGUI\codingan\images\gambar.png")
img = img.resize((180,130))
imgTk = ImageTk.PhotoImage(img)
gambar.append(imgTk)

# menampilkan gambar hunian
labelImg = Label(root, image = imgTk)
labelImg.pack()


button = Button(root, text="Masuk", command=open_data_page)
button.pack(pady=10)

root.mainloop()
