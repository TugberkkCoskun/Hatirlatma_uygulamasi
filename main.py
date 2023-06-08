from tkinter import *                           #tutorialspoint' sitesinde gui lere bakıp methodaların özellikleri öğrenilebilir
from tkcalendar import DateEntry
import ssl
import smtplib
from email.mime.text import MIMEText
from tkinter import messagebox
import time

master = Tk()

canvas = Canvas(master, height=650, width=950)        #Canvas'ın içine hangi objenin içine eklemek istediğimizi yazıyoruz bu senaryoda tanımladğımız master
canvas.pack()
# pack bunların 3 üde ekrana yerleştirme işlemi yukarıda tanımladığımız ve masterla ilişkilendirdiğimiz yapıyı eklemeye yarıyor hepsi aynı işi yapıyor ama farklı özellikleri var
# place
# grid
frame_ust = Frame(master, bg="#add8e6")                              #Frame oluşturma yapısı bg = background colour #add8e6 açık mavinin kodu
frame_ust.place(relx= 0.1 , rely=0.1, relheight=0.1, relwidth=0.8)   # Aynı Canvasda olduğu gibi bunuda yerleştiriyoruz konum belirtmemiz gerektiği için place ile yerleştirdik

frame_sol_alt = Frame(master, bg="#add8e6")
frame_sol_alt.place(relx=0.1, rely=0.21, relheight= 0.7, relwidth=0.23)

frame_sag_alt = Frame(master, bg="#add8e6")
frame_sag_alt.place(relx=0.35, rely=0.21, relheight= 0.7, relwidth=0.55)

hatirlatma_etiketi = Label(frame_ust, bg="#add8e6", text="Hatırlatma Tipi:", font="times-new-roman 12 bold")  #stil ile ilgili işlem yapmak istiyorsak burda, frame üst dedik çünkü burda olmasını istiyoruz
hatirlatma_etiketi.pack(padx=10, pady=10, side=LEFT)                                                   #konum ile ilgil işlemler burda, padx ve pady, objelerin iç tarafına boşluk bırakma padding gerekirse oku

hatirlatma_tipi_opsiyon = StringVar()                       # oluşturacağımız drop down menünün default halindeki değeri yazıyoruz
hatirlatma_tipi_opsiyon.set("\t")                           # default değeri ekliyoruz

hatirlatma_tipi_opsiyon_menu = OptionMenu(frame_ust, hatirlatma_tipi_opsiyon,"Alışveriş","Doğum Günü","Ödeme")      #frame üstte yerleşecek, default değeri görücez ilk başta sonra liste
hatirlatma_tipi_opsiyon_menu.pack(padx=10, pady=10, side=LEFT)

hatırlatma_tarihi_calender = DateEntry(frame_ust, width=12, background="orange",foreground = "black",borderwidth = 1, locale="tr_TR")    #DateEntry içine alan parametreleri araştır locale= DİL !
hatırlatma_tarihi_calender._top_cal.overrideredirect(False)                                 #DateEntrynin çalışması için gereken saçma birşey
hatırlatma_tarihi_calender.pack(padx=10,pady=10, side=RIGHT)

hatirlatma_tarihi = Label(frame_ust, bg="#add8e6", text="Hatırlatma Tarihi:",font="times-new-roman 12 bold")
hatirlatma_tarihi.pack(padx=10, pady=10, side=RIGHT)

hatirlatma_yontemi_etiketi =Label(frame_sol_alt, bg="#add8e6", text="Hatırlatma Yöntemi:", font="times-new-roman 12 bold")
hatirlatma_yontemi_etiketi.pack(padx=10, pady=10, anchor= NW)   #ANCHOR ÇAPA PUSULADAKİ NORT WEST E YERLEŞTİR DEMEK GİBİ

var = IntVar()                                                  #Drop down menüde oluşturduğumuz gibi default bir sayı değişkeni oluşturuyoruz. Bu seçenek sayısına göre değer alacak

R1 = Radiobutton(frame_sol_alt,text="Sisteme Kaydet", bg="#add8e6", font="times-new-roman 10",variable=var, value=1)    #variable = tanımladığımız default değere eşitledik , value = her seçenek için 1,2,3 diye gidecek
R1.pack(padx=15, pady=5, anchor=NW)

R2 = Radiobutton(frame_sol_alt, text = "E-posta Gönder", bg="#add8e6", font="times-new-roman 10", variable=var, value=2)
R2.pack(padx= 15, pady=5, anchor=NW)

var1 = IntVar()                             #var 1 değeri tanımlamamızın nedeni: açık value iken 1 i var1 e ata kapalıyken 0'ı var1 e ata bağımsız olduğu için birbirinden her biri için ayrı değer tanımladık
Checkbutton1 = Checkbutton(frame_sol_alt,text ="Bir Ay Önce", bg = "#add8e6", font="times-new-roman 10",variable=var1 , onvalue=1 , offvalue=0)
Checkbutton1.pack(padx=30,pady=3,anchor=NW)

var2 = IntVar()
Checkbutton2 = Checkbutton(frame_sol_alt,text ="Bir Hafta Önce", bg = "#add8e6", font="times-new-roman 10",variable=var2, onvalue=1, offvalue=0)
Checkbutton2.pack(padx=30,pady=3,anchor=NW)

var3 = IntVar()
Checkbutton3 = Checkbutton(frame_sol_alt,text ="Her gün", bg = "#add8e6", font="times-new-roman 10",variable=var3, onvalue=1 , offvalue=0)
Checkbutton3.pack(padx=30,pady=3,anchor=NW)

R3 =Radiobutton(frame_sol_alt,text = "E-posta Giriniz:", bg="#add8e6",font="times-new-roman 10", variable=var, value=2)
R3.pack(padx=15, pady=5, anchor=SW)

metin_alani2 = Text(frame_sol_alt,bg="Light Yellow")
metin_alani2.tag_configure("style", foreground="Gray",font=("Verdana",8, "bold", "italic"))
metin_alani2.place(relx=0.1, rely=0.55 ,relwidth= 0.85, relheight=0.1)
karsilama_metni2 = "example@hotmail.com"
metin_alani2.insert("1.0",karsilama_metni2,"style")

from tkinter import messagebox


def hatirlatma_mail_gonder():
    son_mesaj = ""
    son_mesaj += "E-posta İle Gönderildi.."
    kullanici = "tugberk.coskun94@hotmail.com"
    sifre = "xx4yy7f722"

    tip = hatirlatma_tipi_opsiyon.get()
    tarih = hatırlatma_tarihi_calender.get()
    mesaj = metin_alani.get("1.0", "end")

    alici = metin_alani2.get("1.0", "end")
    baslik = "Hatırlatma Maili"
    metin = ("{} tipindeki, {} tarihindeki mesajınız:\n{}".format(tip, tarih, mesaj))
    msg = MIMEText(metin)

    msg["Subject"] = "Hatırlatma Maili"
    msg["From"] = kullanici
    msg["To"] = alici

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    port = 587
    host = "smtp.office365.com"

    eposta_sunucu = smtplib.SMTP(host=host, port=port)
    eposta_sunucu.starttls(context=context)
    eposta_sunucu.login(kullanici, sifre)
    eposta_sunucu.send_message(msg, kullanici, alici)
    eposta_sunucu.quit()
    messagebox.showinfo("Başarılı işlem", son_mesaj)  # Göndere basınca info kutusu çıkartıyor, error ve warning seçenekleride var

def gonder():
    son_mesaj = ""              # ilk olarak mesajı tanımladık
    try:
        if var.get():          # Eğer kullanıcı tarafından herhangi bir değer seçildiyse senaryosu için ilk if i yazıyoruz
            if var.get() == 1:          # 1 aldığı konum sisteme kaydet ibaresi seçildiği konum yukarıda tanımladık
                son_mesaj += "Sisteme Başarıyla Kayıt Edildi.."     # son mesajın içine bunu yazsın
                tip = hatirlatma_tipi_opsiyon.get()  # Eğer hiç bişi seçilmezse hatırlatma tipi opsiyon alanını boş bırakma genel yaz demek
                tarih = hatırlatma_tarihi_calender.get()
                mesaj =  metin_alani.get("1.0","end")                   # 1.0 . indexten sonuna kadar hepsini al demek

                with open("Hatırlatmalar.txt","w",encoding="utf-8") as dosya:       # mesajı encode lamazsak türkçe karakterlerden dolayı hata veriyor
                    dosya.write("{} tipindeki, {} tarihindeki mesajınız:\n{}".format(tip,tarih,mesaj))
                    dosya.close()
                messagebox.showinfo("Başarılı işlem",son_mesaj)
            elif var.get() == 2 and var1.get() == 1:
                hatirlatma_mail_gonder()



        else:
            son_mesaj += "Gerekli alanların doldurulduğundan emin olun"
            messagebox.showwarning("Eksik işlem",son_mesaj)
    except:
        son_mesaj += "Hatalı işlem Yaptınız!"
        messagebox.showerror("Hatalı işlem",son_mesaj)
    finally:
        master.destroy()

hatirlatma_mesaji_etiketi = Label(frame_sag_alt, bg="#add8e6",font="times-new-roman 12 bold",text="Hatırlatma Mesajı:")
hatirlatma_mesaji_etiketi.pack(pady=10, padx=10, anchor=NW)

metin_alani = Text(frame_sag_alt,bg="Light Yellow")
metin_alani.tag_configure("style", foreground="Gray",font=("Verdana",12, "bold"))               #Metin alanı içerisindeki yazının özellikleri
metin_alani.place(relx=0.1, rely=0.17 ,relwidth= 0.8, relheight=0.6)
karsilama_metni = "Mesajınızı buraya giriniz"
metin_alani.insert("1.0",karsilama_metni,"style")                        #Metin alanı içerisine ekleyeceğimiz karşılama yazısı END konumu style bu tanımladığım şekilde ekle

gonder_butonu = Button(frame_sag_alt, text="Gönder", command=gonder)        # genelde buton tasarlarken syntax Nereye, ne yazacak, ne yapacak şeklinde olur gonder adlı bir fonksiyon yazıcaz
gonder_butonu.place(relx=0.42, rely=0.82, relheight=0.1,relwidth=0.15)


master.mainloop()
