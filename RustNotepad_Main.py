from tkinter import messagebox, filedialog, ttk
import os
import tkinter as tk

pencere = tk.Tk()
pencere.title("Rust notepad")
pencere.geometry("800x600")

dizinim = os.getcwd()
os.chdir(dizinim)

birinci_adim = False
klasör_varmi = os.path.exists(dizinim + "/notess")

if klasör_varmi:
    birinci_adim = True
    print("klasör zaten var!")
else:
    os.mkdir(dizinim + "/notess")
    print("klasör oluşturuldu!")
    birinci_adim = True


def Create_Note():
    dosya_adı = dosya_isim.get()
    dosya_uzantısı = dosya_tipi.get()
    notum = notlar.get("1.0", "end-1c")
    cevap = messagebox.askquestion("Uyarı", "Dosyaya yazmaya devam etmek istiyor musunuz?")
    if cevap == "yes":
        dosya = open(dosya_adı + dosya_uzantısı, "a")
        dosya.write(notum)
        dosya.close()
        print("Dosya başarıyla yazıldı")
        messagebox.showinfo("Başarılı", "Dosya başarıyla oluşturuldu!")


def OpenFile():
    filename = filedialog.askopenfilename()
    messagebox.showinfo("Dosya Yolu", filename)
    file = open(filename, "r")
    notlar.delete(1.0, tk.END)
    notlar.insert(tk.END, file.read())
    file.close()


if birinci_adim:
    os.chdir(dizinim + "/notess")
    dosyaisim_label = tk.Label(pencere, text="Not defterinizin adını yazın", font="courier 16 bold", width=30)
    dosya_isim = tk.Entry(pencere, font="courier 16 bold", width=15, justify="left")
    notlar = tk.Text(pencere, font="courier 16 bold", width=75, height=20)
    dosya_tipi = ttk.Combobox(pencere, font="courier 16 bold", width=15, textvariable=tk.StringVar())
    dosya_tipi["values"] = (".txt", ".docx", ".doc", ".pdf", ".ts", ".py", ".cpp", ".js", ".cs", ".c", ".html",
                            ".php", ".xml", ".css", ".bat", ".lua", ".c++", ".cmd", ".apk")
    create_button = tk.Button(pencere, text="Oluştur", font="courier 16 bold", width=15, command=Create_Note)
    file_openner = tk.Button(pencere, text="Dosya Aç", font="courier 16 bold", width=15, command=OpenFile)

    dosyaisim_label.place(x=5, y=30)
    dosya_isim.place(x=49, y=50)
    dosya_tipi.place(x=49, y=95)
    create_button.place(x=50, y=450)
    file_openner.place(x=45, y=510)
    notlar.place(x=300, y=50)

pencere.mainloop()
