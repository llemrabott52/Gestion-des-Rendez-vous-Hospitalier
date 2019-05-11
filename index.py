#coding:utf-8
from tkinter import*
from PIL import Image, ImageTk
import  tkinter as Tk 
import sqlite3
import tkinter.messagebox
 
conn=sqlite3.connect('database.db')
c=conn.cursor()

ids=[]


class Application:
    """
    Application c'est la classe dans laquel on va faire notre projet en créant un constructeur et des differents attributs et methodes
    et à la fin on crée un objet qui faire appel à cette classe en passant comme paramètre 'root' qui ouvre la fenetre principale
    et cette paramètre correspond à celle declaré dans la constructeur
    """
    def __init__(self,master):
        
        """
        Dans cette constructeur on prend comme parametre d'entré self et master ,self indique l'objet courant ,
        master indique le fenetre principale (acceuil) quand on le remplace par 'root' en créant un objet
        b=Application(root) et dans cette fenetre  on va faire notre travail en ajoutant cadres ,images, textes etc..
        """
        ##self.master: le master de l' objet courant on va le passer le master qu' on la pris comme parametre dans le constructeur __init__
        self.master=master  
        ##self.hautFrame est un cadre inclut dans le fenetre  master qu'on la met en haut de cette fenetre dont la longueur est 1200 et la largeur est 150 et avec couleur  lightsteelblue
        self.hautFrame=Frame(self.master,width=1200,height=150,bg='lightsteelblue')
        self.hautFrame.pack(side=TOP)
        ##self.framebienv est un cadre inclut dans le fenetre  master positionné avec  abscisse x=163 et ordonnée 0  dont la longueur est 1200 et la largeur est 150 et avec couleur 'midnightblue'
        self.framebienv=Frame(self.master,width=1047,height=105,bg='midnightblue')
        self.framebienv.place(x=163,y=0)
        ##self.cadreInfo est un cadre inclut dans le fenetre  master qu'on la met en bas de cette fenetre  par rapport à hautFrame qui est en haut avec une largeur de 1200 et longueur de 620 et dont la couleur est 'lightsteelblue
        self.cadreInfo=Frame(self.master,width=1200,height=620,bg='lightsteelblue')
        self.cadreInfo.pack(side=BOTTOM)
        
        

        ##self.image est une variable dans laquel on va mettre  une image de format png 'logo.png'  ouvrit en utilisant 'Image.open' importé de la bibliotheque Pillow qu'on le doit l'installé pour mettre des images
        self.image = Image.open("logo.png")
        ##self.photo est une variable dans laquel on va mettre  l'image ouvrit self.image  en utilisant ImageTk.PhotoImage  importé de la bibliotheque Pillow 
        self.photo = ImageTk.PhotoImage(self.image)
        ##self.canvas est une zone rectangulaire destiné a contenir des images et autres figures et cette variable self.canvas est crée dans le cadre hautFrame pour mettre dedans notre image 'logo.png'
        ##self.canvas.create_image permet de creer  ou mettre notre objet image "logo.png "  dans le canvas
        self.canvas = Tk.Canvas(self.hautFrame, width =500, height =160,bg='lightsteelblue')
      
        self.canvas.create_image(0,0, anchor = Tk.NW, image= self.photo)
        self.canvas.place(x=10,y=0)
        
       
        ##self.saisir est un boutton appelé 'Saisir un rendez-vous' mit dans le cadre 'self.hautFrame' qui renvoie vers la fenetre 'appoint(self)' qui est une fonction,
        ##saisir a une largeur de 30 ,longueur de 2, police de caractère 'arial 10 bold' et couleur background:steelblue , couleur foreground :blanche
        self.saisir=Button(self.hautFrame,text="Saisir un rendez-vous",width=30,height=2,font=('arial 10 bold'),bg='steelblue',fg='white',command=self.appoint)
        self.saisir.place(x=163,y=105)
        ##self.chercher est un boutton appelé 'chercher et modifier rendez-vous'  mit dans le cadre 'self.hautFrame' qui renvoie vers la fenetre 'update(self)' qui est une fonction,
        ##chercher  a une largeur de 37 ,longueur de 2, police de caractère 'arial 10 bold' et couleur background:steelblue , couleur foreground :blanche
        self.chercher=Button(self.hautFrame,text="chercher et modifier rendez-vous",width=37,height=2,font=('arial 10 bold'),bg='steelblue',fg='white',command=self.update)
        self.chercher.place(x=380,y=105)
        ##self.voir est un boutton appelé 'Voir Les rendez-vous' mit dans le cadre 'self.hautFrame' qui renvoie vers la fenetre 'voirRendezVous(self)' qui est une fonction,
        ##voir  a une largeur de 30 ,longueur de 2, police de caractère 'arial 10 bold' et couleur background:steelblue , couleur foreground :blanche
        self.voir=Button(self.hautFrame,text="Voir Les rendez-vous",width=30,height=2,font=('arial 10 bold'),bg='steelblue',fg='white',command=self.voirRendezVous)
        self.voir.place(x=680,y=105)
        ##self.info est un boutton appelé 'Plus d'information' mit dans le cadre 'self.hautFrame' qui renvoie vers la fenetre 'Information(self)' qui est une fonction,
        ##info  a une largeur de 34 ,longueur de 2, police de caractère 'arial 10 bold' et couleur background:steelblue , couleur foreground :blanche 
        self.info=Button(self.hautFrame,text="Plus d'information",width=34,height=2,font=('arial 10 bold'),bg='steelblue',fg='white',command=self.Information)
        self.info.place(x=920,y=105)
        ##self.bienvenue est une étiquette(Label) appelé 'LOGICIEL DE GESTION  DES RENDEZ-VOUS DES PATIENTS' mit dans le cadre 'self.framebienv',
        ##bienvenue a police de caractère 'arial 22 bold' et couleur background:midnightblue , couleur foreground :blanche
        self.bienvenue=Label(self.framebienv,text="LOGICIEL DE GESTION  DES RENDEZ-VOUS DES PATIENTS",font=('arial 22 bold'),fg='white',bg='midnightblue')
        self.bienvenue.place(x=80,y=30)
        
        
        
        requet="SELECT * FROM appointments"
        ##self.result va prendre le resultat de l'execution de la requete "SELECT * FROM appointments" avec c.execute(requet)
        self.result=c.execute(requet)
        ##self.rows va prendre tout les lignes de self.result par fetchall()
        self.rows= self.result.fetchall()
        if self.rows==[]:
            ##self.framevide: Si self.rows retourne une liste vide ,pas de resultat de la requete alors on crée une cadre self.framevide dans le cadre self.vadreInfo , avec largeur 1200 ,longueur 510 et couleur background 'midnightblue'
            self.framevide=Frame(self.cadreInfo,width=1200,height=510,bg='midnightblue')
            self.framevide.place(x=0,y=20)
            ##self.bdVide: est une étiquette dont le nom est 'Aucun patient n'est saisi ,veuiller saisir un patient..' écrit dans le cadre self.framevide dans le cas ou
            ##la requete retourne resultat vide donc la liste self.rows est vide
            self.bdVide=Label(self.framevide,text="Aucun patient n'est saisi ,veuiller saisir un patient..",font=('arial 30 bold'),fg='white',bg='midnightblue')
            self.bdVide.place(x=100,y=180)
        else:
           ##self.texte: dans le cas ou self.rows retourne une resultat alors on crée une zone de texte de variable self.texte dans le cadre self.cadreInfo de largeur 140 et longueur 30 positionné avec abscisse de 25 et ordonnée 25, 
           self.texte=Text(self.cadreInfo,width=140,height=30)
           self.texte.place(x=25,y=25)
           ##dans cette Zone de texte on a inseré pour chaque colonne Nom,Prenom,Age ,Genre,Location  neumero de Telephone et le temps prevu du rendez-vous de chaque patient ....etc 
           self.texte.insert(END,"ID\t\tNom\t\tPrenom\t\tAge\t\tGenre\t\tLocation\t\tNumero_tel\t\tTemps_prevu\n")
           self.texte.insert(END,"-------------------------------------------------------------------------------------------------------------------------------------------\n")
        
          
           for  row in self.rows:
                 self.texte.insert(END,"{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}\t\t{5}\t\t{6}\t\t{7}\n".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
                
    
    
    def appoint(self):
        """
        'appoint' est une fonction  dont  on va crée une fenetre fen1 dans laquel on va saisir les rendez-vous des patients avec son nom,prenom,son age ,location et son date prevu pour le rendez-vous
        et dans le fenetre de cette fonction on va lire  les journaux des patients saisis .
        """
        def revenir1():
            self.fen1.destroy()
            self.master.deiconify()
            
        self.master.withdraw()
        ##fen1 est la fenetre dans laquel on va saisir les rendez-vous des patients et
        ##en affichant le journal des  saisis 
        self.fen1=tkinter.Toplevel(self.master)
        self.fen1.geometry("1200x720+0+0")
        self.fen1.resizable(False,False)
         
        ##self.left c'est  le cadre à gauche de fen1 dans laquel ov saisir les informations d'un patient et
        ##cette cadre prend toute la longueur de fen1 et prend un largeur de 800px
        self.left=Frame(self.fen1,width=800,height=720,bg='lightsteelblue')
        self.left.pack(side=LEFT)
        ##self.right c'est  le cadre à droite  de fen1 dans laquel dans lequel on va afficher le journal des patients saisis ,
        ##cette cadre  prend toute la longueur de fen1 et prend un largeur de 400px
        self.right=Frame(self.fen1,width=400,height=720,bg='steelblue')
        self.right.pack(side=RIGHT)
        ##etiquette 'label' represente le titre du formulaire saisie pour le patient
        self.heading=Label(self.left,text="Saisir un rendez-vous d'un  Patient",font=('arial 25 bold'),fg='green',bg='lightsteelblue')
        self.heading.place(x=80,y=0)
        ##etiquette 'label' du nom du patient saisie
        self.nom=Label(self.left,text="Nom :",font=('arial 12 bold'),fg='black',bg='lightsteelblue')
        self.nom.place(x=0,y=100)
        ##etiquette 'label' du prenom du patient saisie
        self.prenom=Label(self.left,text="Prenom :",font=('arial 12 bold'),fg='black',bg='lightsteelblue')
        self.prenom.place(x=0,y=140)
         
        ##etiquette 'label' de l'age du patient saisie
        self.age=Label(self.left,text="Age  :",font=('arial 12 bold'),fg='black',bg='lightsteelblue')
        self.age.place(x=0,y=180)
        ##etiquette 'label' du numero telephone  du patient saisie
        self.phone=Label(self.left,text="Numero_tel :",font=('arial 12 bold'),fg='black',bg='lightsteelblue')
        self.phone.place(x=0,y=220)
        ##etiquette 'label' du genre du patient saisie
        self.genre=Label(self.left,text="Genre :",font=('arial 12 bold'),fg='black',bg='lightsteelblue')
        self.genre.place(x=0,y=260)
        ##etiquette 'label' de location  du patient saisie
        self.location=Label(self.left,text="Location :",font=('arial 12 bold'),fg='black',bg='lightsteelblue')
        self.location.place(x=0,y=300)
       
        ##etiquette 'label' de temps du rendez-vous du patient saisie
        self.temps=Label(self.left,text="Temps rendez-vous :",font=('arial 12 bold'),fg='black',bg='lightsteelblue')
        self.temps.place(x=0,y=340)
        
         
        ## entrez nom du patient
        self.nom_ent=Entry(self.left,width=30)
        self.nom_ent.place(x=250,y=100)
        ## entrez prenom du patient
        self.prenom_ent=Entry(self.left,width=30)
        self.prenom_ent.place(x=250,y=140)
         
     
        ## entrez l'age du patient
        self.age_ent=Spinbox(self.left,from_=1,to=100)
        self.age_ent.place(x=250,y=180)
        ## entrez le numero telephone du patient
        self.phone_ent=Entry(self.left,width=30)
        self.phone_ent.place(x=250,y=220)
       
        #entrer le genre
        def  change(*args):
            print("running change")
            print(self.variable.get())
        ##self.variable est une variable de type String qui prend 2 valeurs pour le menu d' option  de genre soit 'masculin' ou 'feminin'
        self.variable = StringVar(self.left)
        self.variable.set("choisir genre") # default value
        self.variable.trace("w",change)
        ##self.genre_ent  est une menu d'option pour entrer le genre du patient et cette menu prend 2 valeurs 'masculin' ou 'feminin' 
        self.genre_ent=OptionMenu(self.left,self.variable,"Masculin","Feminin")
        self.genre_ent.config(bg ="lightsteelblue")
        self.genre_ent.config(font=('arial 10 bold')) 
        self.genre_ent.place(x=250,y=260)
  
        #entrez la location 
        def  change2(*args):
            print("running change")
            print(self.variable2.get())
        ##self.variable2 est une variable de type String qui varie selon le choix de l'utilisateur dans une liste d'options pour la location et cette liste prend les differentes villes en Mauritanie 
        self.variable2 = StringVar(self.left)
        self.variable2.set("choisir la location") # default value
        self.variable2.trace("w",change2)
        ##self.location_ent est une menu de liste d'option permet le choix de location parmi plusieurs villes de Mauritanie 
        self.location_ent=OptionMenu(self.left,self.variable2,"Ksar","Arafat","Teyarett","Toujounine","ES-Sebkha","DAR NAIM","Tevragh zeina","EL-MINA","Ouad-Naga","Boutilimit","Rosso","Nouadhibou","Atar","Kaedi","Tidjikja","Akjoujt","Bogué","Nema","selibaby")
        self.location_ent.config(bg ="lightsteelblue")
        self.location_ent.config(font=('arial 10 bold')) 
        self.location_ent.place(x=250,y=300)
        
        #temps du rendez-vous
        def  change3(*args):
            print("running change")
            print(self.variable3.get())
        ##self.variable3 est une variable de type String qui varie selon le choix de l'utilisateur dans une liste d'options pour le temps prevu du rendez-vous et cette liste prend des durées de temps bien precis 
        self.variable3 = StringVar(self.left)
        self.variable3.set("choisir Le temps") # default value
        self.variable3.trace("w",change3)
        ##self.temps_ent est une menu de liste d'option permet le choix de temps prevu pour le rendez-vous parmi plusieurs temps bien precisé
        self.temps_ent=OptionMenu(self.left,self.variable3,"08:00PM","08:15PM","08:30PM","08:45PM","09:00PM","09:15PM","09:30PM","09:45PM","10:00PM","10:15PM","10:30PM","10:45PM","11:00PM","11:15PM","11:30PM","11:45PM","12:00PM","12:15PM","12:30PM","12:45PM","13:00PM")
        self.temps_ent.config(bg ="lightsteelblue")
        self.temps_ent.config(font=('arial 10 bold')) 
        self.temps_ent.place(x=250,y=340)
        
        ##self.submit c'est la boutton qui permet d'ajouter un rendez-vous
        self.submit=Button(self.left,text="Ajouter un rendez-vous",font=('arial 8 bold'),width=25,height=2,bg='steelblue',fg="white",command=self.add_appointement)
        self.submit.place(x=265,y=410)
        ##self.retourner c'est la boutton qui nous permet de retourner au fenetre d'acceuil
        self.retourner=Button(self.left,text="<=",width=5,height=1,bg='steelblue',fg='white',font=('arial 12 bold'),command=revenir1)
        self.retourner.place(x=0,y=0)
        
        ##self.log c'est une étiquette qui donne le titre 'journal' qui affiche le journal du patient saisie 
        self.log=Label(self.right,text="Journal",font=('arial 20 bold'),fg='white',bg='steelblue')
        self.log.place(x=140,y=3)
        ##self.box c'est une zone de texte dans laquel on va afficher le journal du patient saisie 
        self.box=Text(self.right,width=40,height=35)
        self.box.place(x=40,y=50)
        
        requet2="SELECT ID  FROM appointments"
            
        self.result=c.execute(requet2)
        for self.row in self.result:
             ##self.id va prendre toute les valeurs de la colonne des IDs des patients  
             self.id=self.row[0]
             ids.append(self.id)
            
        ##rendre les ids par ordre croissant
        self.new=sorted(ids)
        self.final_id=self.new[len(ids)-1]
                
        #Afficher le nombre des rendez-vous , le rendez-vous saisi et son temps prevu
            
        self.box.insert(END,"le nombre total des rendez-vous est: " +str(self.final_id)+"\n")
        
        
    #fonction fait actions quand on clique sur boutton
    def add_appointement(self):
        """
        add_appointement est une fonction qui prend les valeurs saisie par l'utilisateur ,c'est à dire les informations du patient,
        si l'un des champs n'est pas encore remplie ,l'application va afficher une alerte qui demande à remplir tout les champs sinon
        les informations du patients seront saisies dans la table 'appointments' de notre  base de donnée et dès que les données sont saisie
        il va nous affiche une alerte de la succès de l'insertion et dans le journal on va recupérer les données que nous venont de saisir en affichant
        aussi le nombre des patients saisis 
        """
        ##obtenir le nom du patient saisie
        self.val1=self.nom_ent.get()
        ##obtenir le prenom du patient saisie
        self.val2=self.prenom_ent.get()
        ##obtenir l'age du patient saisie
        self.val3=self.age_ent.get()
        ##obtenir le genre du patient par le choix de l'un des options 
        self.val4= self.variable.get()
        ##obtenir le Location  du patient par le choix de l'un des options 
        self.val5=self.variable2.get()
        ##obtenir le numero du telephone  du patient saisie
        self.val6=self.phone_ent.get()
        ##obtenir le temp du rendez-vous du patient par le choix de l'un des options 
        self.val7=self.variable3.get()
        #checking si l'un des elts entrés est vide 
        if self.val1=='' or self.val2=='' or self.val3=='' or  self.val4=='' or self.val5=='' or self.val6==''or self.val7=='' :
            tkinter.messagebox.showinfo("Attention","s'il te plait remplir tout les champs")
        else:
            requet= "INSERT INTO 'appointments' (nom,Prenom,age,genre,location,phone,temps_prevu) VALUES(?,?,?,?,?,?,?)"
            c.execute(requet,(self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.val7,))
            conn.commit()
            print("Les eléments sont bien insérés dans la base de données")
            tkinter.messagebox.showinfo("Succès","Le rendez-vous pour le patient "+self.val1+" est enregistré avec succès")
            
           
            self.box.insert(END,"le rendez-vous fixe pour "+self.val1+" en temps prevu: "+str(self.val7)+"\n")
            
    def update(self):
        """
        update c'est une fonction qui permet de créer une fenetre self.fen2 et il permet aussi de chercher dans cette fenetre
        un rendez-vous d'un patient par son nom et le modifier ou supprimer si on a besoin de le faire 
        """
        def revenir2():
            self.fen2.destroy()
            self.master.deiconify()
            
            
        self.master.withdraw()
        ##self.fen2 est une fenetre sera ouvert  quand on clique sur le boutton 'chercher et modifier un rendez-vous' dans le fenetre d'acceuil 
        self.fen2=tkinter.Toplevel(self.master)
        self.fen2.geometry("1200x720+0+0")
        self.fen2.resizable(False,False)
        ##self.CadreFen2 est un cadre qui prend l'ecran plein  de la fenetre self.fen2 en lui ajoutant une couleur background 'lightsteelblue'
        self.CadreFen2=Frame(self.fen2,width=1200,height=720,bg='lightsteelblue')
        self.CadreFen2.pack()
        ##self.heading est une étiquette qui represente le titre de la fenetre qui est "chercher un rendez-vous et le modifier"
        self.head=Label(self.CadreFen2,text="chercher un rendez-vous et le modifier",font="arial 25 bold",fg='green',bg='lightsteelblue')
        self.head.place(x=150,y=0)
        ##self.name est une étiquette 'label' a pour texte "entrer le nom du patient:"
        self.name=Label(self.CadreFen2,text="entrer le nom du patient:",font="arial 15 bold",bg='lightsteelblue')
        self.name.place(x=0,y=60)
        ##self.entr_name est une entrée qui permet de saisir le nom du patient afin de le saisir 
        self.entr_name=Entry(self.CadreFen2,width=30)
        self.entr_name.place(x=240,y=61)
        ##self.search est un boutton qui permet chercher un patient en envoyant la commande de la recherche vers la fonction chercher_db qui retourne les informations du patient 
        self.search=Button(self.CadreFen2,text="chercher",width=15, bg="steelblue",fg='white',font=('arial 12 bold'),command=self.chercher_db)
        self.search.place(x=350,y=100)
        ##self.retourner2 est un boutton qui permet de retourner au fenetre precendent c'est à dire la fenetre d'acceuil
        self.retourner2=Button(self.CadreFen2,text="<=",width=5,height=1,bg='steelblue',fg='white',font=('arial 12 bold'),command=revenir2)
        self.retourner2.place(x=0,y=0)
    def chercher_db(self):
        """
        chercher_db est une fonction qui permet de chercher les informations du rendez-vous d'un patient selon le nom de ce patient et elle recupère ces informations
        de notre base de donnée et elle les affiche sur le meme fenetre ou on l'a chercher et avec cette affichage elle nous propose 2 bouttons l'un permet la modification
        des informations du rendez-vous et l'autre permet la suppression du rendez-vous
        """
        ##self.input_name permet de recupère le nom du patient saisie par l'utilisateur
        self.input_name=self.entr_name.get()
        req="SELECT * FROM appointments WHERE nom LIKE ?"
        self.result=c.execute(req,(self.input_name,))
        for self.row in self.result:
            self.nom=self.row[1]
            ##self.Prenom permet de recupère le prenom du patient cherché d'après la base de donnée 
            self.Prenom=self.row[2]
            self.age=self.row[3]
            self.genre=self.row[4]
            self.location=self.row[5]
            self.phone=self.row[6]
            ##self.temps_prevu permet de recupère le temps prevu de rendez-vous du patient cherché d'après la base de donnée 
            self.temps_prevu=self.row[7]
        #les labels
        ##self.lab_nom est une étiquette qui a pour texte 'Nom du patient'
        self.lab_nom=Label(self.CadreFen2,text='Nom du patient:',font='arial 15 bold',bg='lightsteelblue')
        self.lab_nom.place(x=0,y=150)
        ##self.lab_prenom est une étiquette qui a pour texte 'Prenom du patient' 
        self.lab_prenom=Label(self.CadreFen2,text='Prenom du patient:',font='arial 15 bold',bg='lightsteelblue')
        self.lab_prenom.place(x=0,y=180)
        ##self.lab_age est une étiquette qui a pour texte  'Age'
        self.lab_age=Label(self.CadreFen2,text='Age',font='arial 15 bold',bg='lightsteelblue')
        self.lab_age.place(x=0,y=210)
        ## self.lab_genre est une étiquette qui a pour texte 'genre'
        self.lab_genre=Label(self.CadreFen2,text='Genre:',font='arial 15 bold',bg='lightsteelblue')
        self.lab_genre.place(x=0,y=240)
        ##self.lab_location est une étiquette qui a pour texte 'Location'
        self.lab_location=Label(self.CadreFen2,text='Location:',font='arial 15 bold',bg='lightsteelblue')
        self.lab_location.place(x=0,y=270)
        ##self.lab_phone est une étiquette qui a pour texte 'Numero Tel'
        self.lab_phone=Label(self.CadreFen2,text='Numero Tel:',font='arial 15 bold',bg='lightsteelblue')
        self.lab_phone.place(x=0,y=300)
        ##self.lab_temps  est une étiquette qui a pour texte 'temps du rendez-vous'
        self.lab_temps=Label(self.CadreFen2,text='temps du rendez-vous:',font='arial 15 bold',bg='lightsteelblue')
        self.lab_temps.place(x=0,y=330)
        #Entry for labels
        ##self.entr_nom est une entrée dans laquelle on insert le nom du patient cherché par l'utilisteur d'après la base de donnée 
        self.entr_nom=Entry(self.CadreFen2,width=30)
        self.entr_nom.place(x=300,y=150)
        self.entr_nom.insert(END,self.nom)
        ##self.entr_prenom est une entrée dans laquelle on insert le prenom du patient cherché par l'utilisteur d'après la base de donnée
        self.entr_prenom=Entry(self.CadreFen2,width=30)
        self.entr_prenom.place(x=300,y=180)
        self.entr_prenom.insert(END,self.Prenom)
        ## self.entr_age est une entrée dans laquelle on insert l'age du patient cherché par l'utilisteur d'après la base de donnée
        self.entr_age=Entry(self.CadreFen2,width=30)
        self.entr_age.place(x=300,y=210)
        self.entr_age.insert(END,str(self.age))
        ##self.entr_genre est une entrée dans laquelle on insert le genre du patient cherché par l'utilisteur d'après la base de donnée
        self.entr_genre=Entry(self.CadreFen2,width=30)
        self.entr_genre.place(x=300,y=240)
        self.entr_genre.insert(END,self.genre)
        ##self.entr_location est une entrée dans laquelle on insert la location du patient cherché par l'utilisteur d'après la base de donnée
        self.entr_location=Entry(self.CadreFen2,width=30)
        self.entr_location.place(x=300,y=270)
        self.entr_location.insert(END,self.location)
        ##self.entr_phone  est une entrée dans laquelle on insert le numéro du telephone du patient cherché par l'utilisteur d'après la base de donnée
        self.entr_phone=Entry(self.CadreFen2,width=30)
        self.entr_phone.place(x=300,y=300)
        self.entr_phone.insert(END,str(self.phone))
        ##self.entr_temps  est une entrée dans laquelle on insert le temps prevu du rendez-vous du patient cherché par l'utilisteur d'après la base de donnée
        self.entr_temps=Entry(self.CadreFen2,width=30)
        self.entr_temps.place(x=300,y=330)
        self.entr_temps.insert(END,self.temps_prevu)
        
        ##self.update est un boutton  permet de modifier les informations d'un patient à l'aide de la fonction 'modifier' 
        self.update=Button(self.CadreFen2,text='Modifier',font='arial 11 bold',width=20,height=2,bg='springgreen',command=self.modifier)
        self.update.place(x=400,y=410)
        ##self.delete est un boutton permet de supprimer le rendez-vous d'un patient à l'aide de la fonction 'supprimer'
        self.delete=Button(self.CadreFen2,text='Supprimer',font='arial 11 bold',width=20,height=2,bg='red',command=self.supprimer)
        self.delete.place(x=150,y=410)
         
    def modifier(self):
        """
        modifier est une fonction qui permet de modifier les informations d'un patient cherché par l'utilisateur et si ces informations
        sont modifiés dans la base de donnée ,elle va nous affiche une alerte qui indique la succès du modification 
        """
        #Les variables qu'on va les modifiers
        
        ##self.var1 est une variable prend le nom du patient affiché d'après la recherche de rendez-vous de ce patient afin de permettre à l'utilisateur de le modifier 
        self.var1=self.entr_nom.get()
        ##self.var2 est une variable prend le prénom du patient affiché d'après la recherche de rendez-vous de ce patient afin de permettre à l'utilisateur de le modifier 
        self.var2=self.entr_prenom.get()
        ##self.var3 est une variable prend l'age du patient affiché d'après la recherche de rendez-vous de ce patient afin de permettre à l'utilisateur de le modifier 
        self.var3=self.entr_age.get()
        ##self.var4 est une variable prend le genre du patient affiché d'après la recherche de rendez-vous de ce patient afin de permettre à l'utilisateur de le modifier 
        self.var4=self.entr_genre.get()
        ##self.var5 est une variable prend la location du patient affiché d'après la recherche de rendez-vous de ce patient afin de permettre à l'utilisateur de le modifier 
        self.var5=self.entr_location.get()
        ##self.var6 est une variable prend le numéro du telephone du patient affiché d'après la recherche de rendez-vous de ce patient afin de permettre à l'utilisateur de le modifier 
        self.var6= self.entr_phone.get()
        ##self.var7 est une variable prend le temps prévu du rendez-vous du patient affiché d'après la recherche de rendez-vous de ce patient afin de permettre à l'utilisateur de le modifier 
        self.var7=self.entr_temps.get()
            
        query="UPDATE appointments SET nom=? , Prenom=? , age=? , genre=? , location=? , phone=? , temps_prevu=? WHERE nom LIKE ?"
        ##self.run prend la requete de modification et le faire executer ,dès qu'il affiche une alerte de succès d'execution alors la modification se réalise dans la base de donnée 
        self.run=c.execute(query,( self.var1,self.var2,self.var3,self.var4,self.var5,self.var6,self.var7,self.input_name,))
        conn.commit()    
        tkinter.messagebox.showinfo("Succès","Vous avez modifié le rendez-vous avec succès!")
        
    def supprimer(self):
        """
        supprimer est une fonction qui permet à l'utilisateur de supprimer un rendez-vous d'un patient cherché avec toute ses informations
        et ca sera une suppression definitive de la base de donnée et dès que la suppression se réalise ,il s'affiche une alerte indiquant
        la succès de la suppression 
        """
        #Supprimer un rendez-vous
        query2="DELETE FROM appointments WHERE nom LIKE ?"
        c.execute(query2,(self.input_name,))
        conn.commit()
        tkinter.messagebox.showinfo("Succès","Vous avez supprimé le rendez-vous avec succès!")
        #après la suppression ,enlever les données supprimés du rendez-vous
        self.entr_nom.destroy()
        self.entr_prenom.destroy()
        self.entr_age.destroy()
        self.entr_genre.destroy()
        self.entr_location.destroy()
        self.entr_phone.destroy()
        self.entr_temps.destroy()
    
    def voirRendezVous(self):
        """
        voirRendezVous est une fonction permet de crée une fenetre self.fen3 et dans cette fenetre elle va afficher par ordre le patient
        qui doit entrer chez le docteur en cliquant sur le boutton 'patient suivant' et cette fonction va utilisé une autre fonction
        funct(self) pour configurer l'affichage du nom et numero du patient par ordre 
        
        """
        def revenir3():
            self.fen3.destroy()
            self.master.deiconify()
        ##self.x est l'indice que les listes 'number' et 'patient' prend pour configurer le nom et numéro du patient 
        self.x=0
        
        self.master.withdraw()
        ##self.fen3 est une fenetre sera ouvert  quand on clique sur le boutton 'voir les rendez-vous' dans le fenetre d'acceuil 
        self.fen3=tkinter.Toplevel(self.master)
        self.fen3.geometry("1200x720+0+0")
        self.fen3.resizable(False,False)
        ##self.cadrefen3 est un cadre qui prend l'ecran plein de la fenetre  'self.fen3' dont la couleur du background est 'lightsteelblue'
        self.cadrefen3=Frame(self.fen3,width=1200,height=720,bg='lightsteelblue')
        self.cadrefen3.pack()
        ##self.heading3 est une etiquette qui a pour texte "Rendez-vous" qui represente le titre de la fenetre 
        self.heading3=Label(self.cadrefen3, text="Rendez-vous", font=('arial 60 bold'),fg='green',bg='lightsteelblue')
        self.heading3.place(x=350,y=0)
        ##self.retourner3 est un Boutton pour revenir au fenetre precedent 
        self.retourner3=Button(self.cadrefen3,text="<=",width=5,height=1,bg='steelblue',fg='white',font=('arial 12 bold'),command=revenir3)
        self.retourner3.place(x=0,y=0)
        ##self.change est un Boutton pour faire changer le patient en donnant le patient suivant 
        self.change=Button(self.cadrefen3,text='Le patient Suivant',font=('arial 10 bold'),width=25,height=2,bg='steelblue',fg='white',command=self.func)
        self.change.place(x=500,y=600)
        ##self.n est une étiquette 'Label' indiquant le numero du rendez-vous dont le texte est vide qu'on le configurera et on parlera plutard avec la fonction 'func'
        self.n=Label(self.cadrefen3, text="", font=('arial 210 bold'),bg='lightsteelblue')
        self.n.place(x=490,y=100)
        ##self.pname est une étiquette 'label' indiquant le nom du patient  dont le texte est vide qu'on le configurera  et on parlera plutard avec la fonction 'func'
        self.pname=Label(self.cadrefen3, text="", font=('arial 50 bold'),bg='lightsteelblue')
        self.pname.place(x=500,y=420)
     
   
    def func(self):
        """
        func est une fonction pour parler et modifier le texte  des étiquettes self.n et self.pname qui represente le numero
        du rendez-vous et le nom du patient et pour ce faire on va déclarer deux listes vides 'numbrer' et 'patients' et par
        une requete on prend les colonnes de la table 'appointments' et on remplit les listes 'number' et patients' par les
        colonnes qui contient nom et numero du patient et puis on fait la configuration pour que l'utilisateur puisse voir un
        rendez-vous en cliquant sur le boutton 'le patient suivant'
        """
         
        #liste vide qu'on le remplirera plutard
        number=[]
        patients=[]
        #recupèrer les données de notre base de données pour les mettrent dans les listes
        req="SELECT * FROM appointments"
        res=c.execute(req)
        #remplir les listes 'number' et 'patients' par les données recupérés
        for r in res:
            ident=r[0]
            nom=r[1]
            number.append(ident)
            patients.append(nom) 
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        self.x+=1
        
    def Information(self):
        """
        Information est une fonction avec laquel on crée une fenetre 'self.fen4' dans laquel on donne des informations sur
        ce logiciel concernant necessairement  l'objectif de ce type de logiciel pour que l'utilisateur puisse bien comprendre
        le but,l'utilisation et savoir qui aura le besoin de l'utiliser 
        """
        def revenir4():
            self.fen4.destroy()
            self.master.deiconify()
            
        self.master.withdraw()
        ##self.fen4 est une fenetre ouvrit en cliquant sur le boutton 'plus d'information' dans la fenetre d'acceuil ,elle contient des informations sur ce logiciel
        self.fen4=tkinter.Toplevel(self.master)
        self.fen4.geometry("1200x720+0+0")
        self.fen4.resizable(False,False)
        ##self.cadrefen4 est un cadre qui prend toute la fenetre et lui ajoute une couleur background 'lightsteelblue'
        self.cadrefen4=Frame(self.fen4,width=1200,height=720,bg='lightsteelblue')
        self.cadrefen4.pack()
        ##self.heading4 est une étiquette 'label' qui donne un titre pour la fenetre "Informations sur ce Logiciel"
        self.heading4=Label(self.cadrefen4, text="Informations sur ce Logiciel", font=('arial 40 bold'),fg='green',bg='lightsteelblue')
        self.heading4.place(x=180,y=0)
        ##self.retourner4 est un Boutton pour revenir au fenetre precédent 
        self.retourner4=Button(self.cadrefen4,text="<=",width=5,height=1,bg='steelblue',fg='white',font=('arial 12 bold'),command=revenir4)
        self.retourner4.place(x=0,y=0)
        #Labels contient les informations
        ##self.Inform1 c'est une étiquette qui donne la 1ère information
        self.Inform1=Label(self.cadrefen4, text="-Ce logiciel est écrit en python avec son Interface graphique Tkinter et en utilisant \n la base de donnée par defaut de python 'sqlite3'.", font=('arial 17 bold'),bg='lightsteelblue')
        self.Inform1.place(x=70,y=100)
        ##self.Inform2 c'est une étiquette qui donne la 2ème information
        self.Inform2=Label(self.cadrefen4, text="-Il vise à faciliter le role de secrétaire d'un docteur dans un Cabinet ou un hopital  ", font=('arial 17 bold'),bg='lightsteelblue')
        self.Inform2.place(x=70,y=180)
        ##self.Inform3 c'est une étiquette qui donne la 3ème information 
        self.Inform3=Label(self.cadrefen4, text="Car:- il permet au secrétaire de saisir les informations d'un patient lors d'un rendez-vous\n ainsi que le nom du patient,prenom, age ,date de Naissance etc.. ", font=('arial 17 bold'),bg='lightsteelblue')
        self.Inform3.place(x=75,y=230)
        ##self.Inform4 c'est une étiquette qui donne la 4ème information
        self.Inform4=Label(self.cadrefen4, text="-Il permet aussi de chercher un rendez-vous pour recupèrer facilement ses données,\non peut aussi modifier ces derniers, si par exemple le temp prevu \nest changé par le patient .. ", font=('arial 17 bold'),bg='lightsteelblue')
        self.Inform4.place(x=75,y=300)
        ##self.Inform5 c'est une étiquette qui donne la 5ème information
        self.Inform5=Label(self.cadrefen4, text="-Si un patient decide enfin de ne pas faire son rendez-vous avec notre docteur ,\non peut supprimer facilement son rendez-vous et sera supprimer\n definitivement de notre base de donnée.  ", font=('arial 17 bold'),bg='lightsteelblue')
        self.Inform5.place(x=75,y=400)
        ##self.Inform6 c'est une étiquette qui donne la 6ème information
        self.Inform6=Label(self.cadrefen4, text="-Enfin le but nécessaire de ce logiciel c'est de permettre au secrétaire de savoir à\n chaque fois le patient qui devra entrer chez notre docteur \n en cliquant simplement sur le boutton 'patient suivant'.", font=('arial 17 bold'),bg='lightsteelblue')
        self.Inform6.place(x=75,y=500)
        ##self.Inform7 c'est une étiquette qui donne la 7ème information
        self.Inform7=Label(self.cadrefen4, text="-Plus d'informations Contactez-nous sur les numéros:+22227312828,+22241394440,+22241437664", font=('arial 17 bold'),bg='lightsteelblue')
        self.Inform7.place(x=75,y=600)
        
#creer un objet
root=Tk.Tk()
b=Application(root)
root.geometry("1200x720+0+0")
root.resizable(False,False)
root.mainloop()
