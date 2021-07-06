from tkinter import *

class App(Tk):

    def __init__(self):
        super().__init__()
        self.creer_widget()
        self.creer_image()
        self.creer_img()

    def triange_v(self):

        self.width = 120
        self.height = 120
        self.tri_v = PhotoImage(file='image/triangle_v2.png').zoom(32).subsample(64)
        self.tri_v_can = Canvas(self, width=self.width, height=self.height, bg='#696F63', highlightthickness=0)
        self.tri_v_can.create_image(self.width / 2, self.height / 2, image=self.tri_v)
        self.tri_v_can.place(x=1000, y=110)
        self.v = self.tri_v_can

    def triange_d(self):

        self.width = 120
        self.height = 120
        self.tri_d = PhotoImage(file='image/triangle_d2.png').zoom(32).subsample(64)
        self.tri_d_can = Canvas(self, width=self.width, height=self.height, bg='#696F63', highlightthickness=0)
        self.tri_d_can.create_image(self.width / 2, self.height / 2, image=self.tri_d)
        self.tri_d_can.place(x=1000, y=110)
        self.d = self.tri_d_can

    def triange_t(self):

        self.width = 120
        self.height = 120
        self.tri_t = PhotoImage(file='image/triangle_t2.png').zoom(32).subsample(64)
        self.tri_t_can = Canvas(self, width=self.width, height=self.height, bg='#696F63', highlightthickness=0)
        self.tri_t_can.create_image(self.width / 2, self.height / 2, image=self.tri_t)
        self.tri_t_can.place(x=1000, y=110)
        self.t = self.tri_t_can

    def creer_image(self):

        self.width = 400
        self.height = 350
        self.image = PhotoImage(file='image/pythonmaman2.png').zoom(48).subsample(64)
        self.canvas = Canvas(self, height=self.width, width=self.height, bg='#696F63', highlightthickness=0)
        self.canvas.create_image(self.width / 2, self.height / 2, image=self.image)
        self.canvas.place(x=-30, y=0)

    def creer_img(self):

        self.width = 210
        self.height = 200
        self.img = PhotoImage(file='image/triangle2.png').zoom(32).subsample(64)
        self.can = Canvas(self, width=self.width, height=self.height, bg='#696F63', highlightthickness=0)
        self.can.create_image(self.width / 2, self.height / 2, image=self.img)
        self.can.place(x=40, y=350)

    def creer_widget(self):

        self.label1 = Label(self, text="Que dois-tu calculer ?", font=("Helvetica", 30), bg='#696F63', fg='black')
        self.label1.place(x=350, y=40)
        self.entry1 = Entry(self, font=("Helvetica", 30), bg='#696F63', fg='black', width=5)
        self.entry1.place(x=800, y=40)
        self.label2 = Label(self, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label2.place(x=350, y=160)
        self.label3 = Label(self, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label3.place(x=750, y=160)
        self.button1 = Button(self, text="Valider", font=("Helvetica", 20), bg='#696F63', fg='black', command=self.v_d_t)
        self.button1.place(x=950, y=38)
        self.entryd = Entry(self, font=("Helvetica", 20), bg='#696F63', fg='black', width=5, bd=0)
        self.entryd.place(x=500, y=220)
        self.labeld = Label(self, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.labeld.place(x=430, y=220)
        self.labeld2 = Label(self, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.labeld2.place(x=590, y=220)
        self.entryv = Entry(self, font=("Helvetica", 20), bg='#696F63', fg='black', width=5, bd=0)
        self.entryv.place(x=500, y=260)
        self.labelv = Label(self, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.labelv.place(x=430, y=260)
        self.labelv2 = Label(self, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.labelv2.place(x=590, y=260)
        self.entryt = Entry(self, font=("Helvetica", 20), bg='#696F63', fg='black', width=5, bd=0)
        self.entryt.place(x=500, y=300)
        self.labelt = Label(self, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.labelt.place(x=430, y=300)
        self.labelt2 = Label(self, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.labelt2.place(x=590, y=300)
        self.label_result = Label(self, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label_result.place(x=350, y=360)
        self.button_reset = Button(self, text="Reinitialiser", font=("Helvetica", 20), bg='#696F63', fg='black', command=self.reinitialiser)
        self.button_reset.place(x=900, y=650)
        self.button_quit = Button(self, text="Fermer", font=("Helvetica", 20), bg='#696F63', fg='black', command=self.quit)
        self.button_quit.place(x=1075, y=650)

    def v_d_t(self):
        vi_di_te = self.entry1.get()
        if vi_di_te == "v" or vi_di_te == "V":
            self.label3['text'] = "D / T"
            self.v_d_t_entry_label()
            self.triange_t()
            self.triange_v()
            self.triange_d()
            self.tri_d_can.destroy()
            self.tri_t_can.destroy()
        elif vi_di_te == "d" or vi_di_te == "D":
            self.label3['text'] = "V * T"
            self.v_d_t_entry_label()
            self.triange_t()
            self.triange_v()
            self.triange_d()
            self.tri_v_can.destroy()
            self.tri_t_can.destroy()
        elif vi_di_te == "t" or vi_di_te == "T":
            self.label3['text'] = "D / V"
            self.v_d_t_entry_label()
            self.triange_t()
            self.triange_v()
            self.triange_d()
            self.tri_v_can.destroy()
            self.tri_d_can.destroy()

    def v_d_t_entry_label(self):
        self.label2['text'] = "Tu dois donc utiliser la formule : "
        self.labeld['text'] = "D = "
        self.labeld2['text'] = "M"
        self.entryd['bd'] = 1
        self.labelv['text'] = "V = "
        self.labelv2['text'] = "M/S"
        self.entryv['bd'] = 1
        self.labelt['text'] = "T = "
        self.labelt2['text'] = "S"
        self.entryt['bd'] = 1
        self.button_v_d_t = Button(self, text="Valider", font=("Helvetica", 20), bg='#696F63', fg='black', command=self.calcul)
        self.button_v_d_t.place(x=800, y=250)

    def calcul(self):
        v = self.entryv.get()
        d = self.entryd.get()
        t = self.entryt.get()
        if v == "":
            v = int(d) / int(t)
            self.label_result['text'] = "Le resultat du calcul est : {} M/S".format(v)
        elif d == "":
            d = int(v) * int(t)
            self.label_result['text'] = "Le resultat du calcul est : {} M".format(d)
        elif t == "":
            t = int(d) / int(v)
            self.label_result['text'] = "Le resultat du calcul est : {} S".format(t)

    def reinitialiser(self):
        self.entryt['bd'] = 0
        self.entryd['bd'] = 0
        self.entryv['bd'] = 0
        self.entry1.delete(0, END)
        self.entryt.delete(0, END)
        self.entryd.delete(0, END)
        self.entryv.delete(0, END)
        self.label_result['text'] = ""
        self.label2['text'] = ""
        self.label3['text'] = ""
        self.labelv['text'] = ""
        self.labelv2['text'] = ""
        self.labelt['text'] = ""
        self.labelt2['text'] = ""
        self.labeld['text'] = ""
        self.labeld2['text'] = ""
        self.triange_t()
        self.triange_v()
        self.triange_d()
        self.tri_v_can.destroy()
        self.tri_d_can.destroy()
        self.tri_t_can.destroy()
        self.button_v_d_t.destroy()



a = True
if a:
    fen = App()
    fen.title("Exercices Physique Chimie")
    fen.geometry("1200x720")
    fen.minsize(1200, 720)
    fen.maxsize(1200, 720)
    fen.iconbitmap('image/molecule.ico')
    fen.config(bg='#696F63')
    fen.mainloop()