from tkinter import *

# Creer l'application -------------------------------------------------------------------------------------------------#

class App(Tk):

# Ce qui ce charge au debut -------------------------------------------------------------------------------------------#

    def __init__(self):
        Tk.__init__(self)
        self.creer_frame()
        self.creer_img()
        self.creer_image()
        self.creer_widget()

# Creer mes trois triangle avec les mains -----------------------------------------------------------------------------#

    def triange_v(self):

        self.width = 100
        self.height = 100
        self.tri_v = PhotoImage(file='image/triangle_v.png').zoom(52).subsample(64)
        self.tri_v_can = Canvas(self, width=self.width, height=self.height, bg='#696F63', highlightthickness=0)
        self.tri_v_can.create_image(self.width / 2, self.height / 2, image=self.tri_v)
        self.tri_v_can.place(x=1000, y=90)
        self.v = self.tri_v_can

#----------------------------------------------------------------------------------------------------------------------#

    def triange_d(self):

        self.width = 100
        self.height = 100
        self.tri_d = PhotoImage(file='image/triangle_d.png').zoom(52).subsample(64)
        self.tri_d_can = Canvas(self, width=self.width, height=self.height, bg='#696F63', highlightthickness=0)
        self.tri_d_can.create_image(self.width / 2, self.height / 2, image=self.tri_d)
        self.tri_d_can.place(x=1000, y=90)
        self.d = self.tri_d_can

#----------------------------------------------------------------------------------------------------------------------#

    def triange_t(self):

        self.width = 100
        self.height = 100
        self.tri_t = PhotoImage(file='image/triangle_t.png').zoom(52).subsample(64)
        self.tri_t_can = Canvas(self, width=self.width, height=self.height, bg='#696F63', highlightthickness=0)
        self.tri_t_can.create_image(self.width / 2, self.height / 2, image=self.tri_t)
        self.tri_t_can.place(x=1000, y=90)
        self.t = self.tri_t_can

# Creer le triangle sans les mains ------------------------------------------------------------------------------------#

    def creer_img(self):

        self.width = 400
        self.height = 400
        self.img = PhotoImage(file='image/triangle.png').zoom(64).subsample(64)
        self.can = Canvas(self, width=self.width, height=self.height, bg='#696F63', highlightthickness=0)
        self.can.create_image(self.width / 2, self.height / 2, image=self.img)
        self.can.place(x=0, y=375)

# Creer l'image avec le texte -----------------------------------------------------------------------------------------#

    def creer_image(self):

        self.width = 400
        self.height = 400
        self.image = PhotoImage(file='image/pythonmaman.png').zoom(96).subsample(64)
        self.canvas = Canvas(self, height=self.width, width=self.height, bg='#696F63', highlightthickness=0)
        self.canvas.create_image(self.width / 2, self.height / 2, image=self.image)
        self.canvas.grid(row=0, column=0, sticky=W)

# Creer les differentes boites ( qui ne se voit pas ) -----------------------------------------------------------------#

    def creer_frame(self):

        self.frame0_0 = Frame(self,bg='#696F63')
        self.frame0_0.grid(row=0, column=0)
        self.frame0_1 = Frame(self, bg='#696F63')
        self.frame0_1.grid(row=0, column=1)
        self.frame0_2 = Frame(self, bg='#696F63')
        self.frame0_2.grid(row=0, column=2)
        self.frame0_3 = Frame(self, bg='#696F63')
        self.frame0_3.grid(row=0, column=3)

# Creer les textes, les boutons et les entrées ( visible ou non ) -----------------------------------------------------#

    def creer_widget(self):

        self.label1 = Label(self.frame0_1, text="Que dois-tu calculer ?", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label1.pack()
        self.entry1 = Entry(self.frame0_2,  font=("Helvetica", 20), bg='#696F63', fg='black')
        self.entry1.pack()
        self.label2 = Label(self.frame0_1, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label2.pack()
        self.label3 = Label(self.frame0_2, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label3.pack()
        self.label4 = Label(self.frame0_1, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label4.pack()
        self.label5 = Label(self.frame0_2, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label5.pack()
        self.button1 = Button(self.frame0_3, text="Valider", font=("Helvetica", 20), bg='#696F63', fg='black', command=self.vitesse)
        self.button1.pack()
        self.label6 = Label(self.frame0_3, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label6.pack()
        self.label7 = Label(self.frame0_3, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label7.pack()
        self.label8 = Label(self.frame0_3, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label8.pack()
        self.label9 = Label(self.frame0_3, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label9.pack()
        self.label10 = Label(self.frame0_2, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label10.pack()
        self.label11 = Label(self.frame0_2, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label11.pack()
        self.label12 = Label(self.frame0_1, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label12.pack()
        self.label13 = Label(self.frame0_1, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label13.pack()
        self.label14 = Label(self.frame0_1, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label14.pack()
        self.label15 = Label(self.frame0_2, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label15.pack()
        self.label16 = Label(self.frame0_3, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label16.pack()
        self.label17 = Label(self.frame0_1, text="", font=("Helvetica", 20), bg='#696F63', fg='red')
        self.label17.pack()
        self.entry18 = Entry(self.frame0_2, font=("Helvetica", 20), bg='#696F63', fg='black', bd=0, highlightthickness=0)
        self.entry18.pack()
        self.label19 = Label(self.frame0_3, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label19.pack()
        self.label20 = Label(self.frame0_1, text="", font=("Helvetica", 20), bg='#696F63', fg='blue')
        self.label20.pack()
        self.entry21 = Entry(self.frame0_2, font=("Helvetica", 20), bg='#696F63', fg='black', bd=0, highlightthickness=0)
        self.entry21.pack()
        self.label22 = Label(self.frame0_3, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label22.pack()
        self.label23 = Label(self.frame0_1, text="", font=("Helvetica", 20), bg='#696F63', fg='lime')
        self.label23.pack()
        self.entry24 = Entry(self.frame0_2, font=("Helvetica", 20), bg='#696F63', fg='black', bd=0, highlightthickness=0)
        self.entry24.pack()
        self.label25 = Label(self.frame0_3, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label25.pack()
        self.label26 = Label(self.frame0_1, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label26.pack()
        self.label27 = Label(self.frame0_2, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label27.pack()
        self.button28 = Button(self.frame0_3, text="Valider", font=("Helvetica", 20), bg='#696F63', fg='black', command=self.v_d_t)
        self.button28.pack()
        self.label29 = Label(self.frame0_1, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label29.pack()
        self.label30 = Label(self.frame0_2, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label30.pack()
        self.label31 = Label(self.frame0_3, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label31.pack()
        self.label32 = Label(self.frame0_1, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label32.pack()
        self.label33 = Label(self.frame0_2, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label33.pack()
        self.label34 = Label(self.frame0_3, text="", font=("Helvetica", 20), bg='#696F63', fg='black')
        self.label34.pack()
        self.button36 = Button(self, text="Fermer", font=("Helvetica", 20), bg='#696F63', fg='black', command=self.end)
        self.button36.place(x=1080, y=650)
        self.button37 = Button(self, text="Réinitialiser", font=("Helvetica", 20), bg='#696F63', fg='black', command=self.remove_all)
        self.button37.place(x=900, y=650)

# Reinitialiser / Remettre a neuf -------------------------------------------------------------------------------------#

    def remove_all(self):
        self.entry1.destroy()
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.label4.destroy()
        self.label5.destroy()
        self.label6.destroy()
        self.label7.destroy()
        self.label8.destroy()
        self.label9.destroy()
        self.label10.destroy()
        self.label11.destroy()
        self.label12.destroy()
        self.label13.destroy()
        self.label14.destroy()
        self.label15.destroy()
        self.label16.destroy()
        self.label17.destroy()
        self.entry18.destroy()
        self.label19.destroy()
        self.label20.destroy()
        self.entry21.destroy()
        self.label22.destroy()
        self.label23.destroy()
        self.entry24.destroy()
        self.label25.destroy()
        self.label26.destroy()
        self.label27.destroy()
        self.button28.destroy()
        self.label29.destroy()
        self.label30.destroy()
        self.label31.destroy()
        self.label32.destroy()
        self.label33.destroy()
        self.label34.destroy()
        self.button37.destroy()
        self.button1.destroy()
        self.button36.destroy()
        self.button28.destroy()
        self.triange_t()
        self.triange_v()
        self.triange_d()
        self.tri_v_can.destroy()
        self.tri_d_can.destroy()
        self.tri_t_can.destroy()
        self.creer_widget()

# Faire apparaitre la bonne formule avec le bon triangle celon la reponse ecrit avant ---------------------------------#

    def vitesse(self):

        ze = self.entry1.get()
        if ze == "v":
            self.label4['text'] = "Tu dois utiliser la formute :"
            self.label5['text'] = "v = d/t"
            self.label13['text'] = "Ecrire les données :"
            self.entry18['bd'] = 1
            self.entry18['highlightthickness'] = 1
            self.label17['text'] = "d = "
            self.label19['text'] = "m"
            self.entry21['bd'] = 1
            self.entry21['highlightthickness'] = 1
            self.label20['text'] = "t = "
            self.label22['text'] = "s"
            self.entry24['bd'] = 1
            self.entry24['highlightthickness'] = 1
            self.label23['text'] = "v = "
            self.label25['text'] = "m/s"
            self.triange_t()
            self.triange_v()
            self.triange_d()
            self.tri_t_can.destroy()
            self.tri_d_can.destroy()


        elif ze == "d":
            self.label4['text'] = "Tu dois utiliser la formute :"
            self.label5['text'] = "d = v*t"
            self.label13['text'] = "Ecrire les données :"
            self.entry18['bd'] = 1
            self.entry18['highlightthickness'] = 1
            self.label17['text'] = "d = "
            self.label19['text'] = "m"
            self.entry21['bd'] = 1
            self.entry21['highlightthickness'] = 1
            self.label20['text'] = "t = "
            self.label22['text'] = "s"
            self.entry24['bd'] = 1
            self.entry24['highlightthickness'] = 1
            self.label23['text'] = "v = "
            self.label25['text'] = "m/s"
            self.triange_t()
            self.triange_v()
            self.triange_d()
            self.tri_v_can.destroy()
            self.tri_t_can.destroy()


        elif ze == "t":
            self.label4['text'] = "Tu dois utiliser la formute :"
            self.label5['text'] = "t = d/v"
            self.label13['text'] = "Ecrire les données :"
            self.entry18['bd'] = 1
            self.entry18['highlightthickness'] = 1
            self.label17['text'] = "d = "
            self.label19['text'] = "m"
            self.entry21['bd'] = 1
            self.entry21['highlightthickness'] = 1
            self.label20['text'] = "t = "
            self.label22['text'] = "s"
            self.entry24['bd'] = 1
            self.entry24['highlightthickness'] = 1
            self.label23['text'] = "v = "
            self.label25['text'] = "m/s"
            self.triange_t()
            self.triange_v()
            self.triange_d()
            self.tri_v_can.destroy()
            self.tri_d_can.destroy()


        else:
            self.label4['text'] = "Minuscule !!!"
            self.label5['text'] = ""
            self.entry1.delete(0, END)

# Creer la bonne reponse au calcul en haut ----------------------------------------------------------------------------#

    def v_d_t(self):
        v = self.entry24.get()
        d = self.entry18.get()
        t = self.entry21.get()
        if v == "":
            v = int(d) / int(t)
            self.entry24.delete(0, END)
            self.entry21.delete(0, END)
            self.entry18.delete(0, END)
            self.label29['text'] = "Le resultat de ton calcul est :"
            self.label32['text'] = "{} m/s".format(v)

        elif d == "":
            d = int(v) * int(t)
            self.entry24.delete(0, END)
            self.entry21.delete(0, END)
            self.entry18.delete(0, END)
            self.label29['text'] = "Le resultat de ton calcul est :"
            self.label32['text'] = "{} m".format(d)

        elif t == "":
            t = int(d) / int(v)
            self.entry24.delete(0, END)
            self.entry21.delete(0, END)
            self.entry18.delete(0, END)
            self.label29['text'] = "Le resultat de ton calcul est :"
            self.label32['text'] = "{} s".format(t)

        else:
            self.label29['text'] = "Tu as du mal ecrire, recommence"

# Quitté le programme ( proprement ) ----------------------------------------------------------------------------------#

    def end(self):
        self.quit()

# Creer la fenetre ( que elle s'affiche ) -----------------------------------------------------------------------------#


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

# Fin, Projet réaliser par QUENTIN BORRAS -----------------------------------------------------------------------------#