#!/usr/bin/python3

import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as tks
from manual import manual
from ImageCopy import images
from random import choice
import Main
import Pmw
import tkinter.messagebox as tmb
from time import sleep

class WhotGtk(images):
    def __init__(self):
        self._root = Pmw.initialise()
        self._root.geometry('790x630')
        self._root.title('Whot Game')
        super().__init__()
        self._frame = Pmw.ScrolledFrame(self._root, labelpos='s', usehullsize=1,
                                        hull_width = 100,
                                        hull_height = 225,
                                        label_text = 'PLAYER  =>')
        self._frame1 = self._frame.interior()
        self._frame2 = tk.Frame(self._root, bg='aquamarine')
        self._frame2.grid(row=1, column=2)
        self._frame2.grid_columnconfigure(0, weight=1)
        self._main_frame3 = Pmw.ScrolledFrame(self._root, labelpos='n', usehullsize=1,
                                              hull_width = 100,
                                              hull_height = 225,
                                              label_text = 'COMPUTER  =>')
        self._frame3 = self._main_frame3.interior()

        ###################################################################
        # Main Initialisations
        ###################################################################
        self._whot = Main.Whot()
        self._whot.InitDepot()
        self._whot.InitPlayerCards()
        self._whot.InitComputerCards()
        self._whot.InitPlayer2Cards()
        self._computer = Main.Computer()
        self._player2 = Main.Player2()
        self._whot.NormCards()
        ###################################################################
        

        ##################################################################
        # To Check who played last
        ##################################################################
        self.__check2_played=[]
        self.__checkcomp_played=[]
        ##################################################################
        
        self._check2 = 0
        self._check1 = 0
        self._values = ['star', 'circle', 'cross', 'square', 'triangle']

        ###################################################################
        # Player2 Butrefs
        ###################################################################
        self._butref1=[]
        self._butref2=[]
        self._butref3=[]
        self._butref4=[]
        self._butref5=[]
        self._butref6=[]

        self._butref7=[]
        self._butref8=[]
        self._butref9=[]
        self._butref10=[]
        self._butref11=[]
        self._butref12=[]
        #####################################################################

        #####################################################################
        # Computer Labrefs
        #####################################################################
        self._labref1=[]
        self._labref2=[]
        self._labref3=[]
        self._labref4=[]
        self._labref5=[]
        self._labref6=[]
        self._labref7=[]
        self._labref8=[]
        self._labref9=[]
        self._labref10=[]
        self._labref11=[]
        self._labref12=[]

        self._labs_refs = [self._labref1, self._labref2, self._labref3, self._labref4,
        self._labref5, self._labref6, self._labref7, self._labref8, self._labref9,
        self._labref10, self._labref11, self._labref12]

        #####################################################################

        

        ######################################################################
        # Initialisation of Buts and Labs
        ######################################################################
        self._labs_comp = []
        for i in range(12):
            self._labs_comp.append(tk.Label(self._frame3))

        self._buts2 = []
        for i in range(12):
            self._buts2.append(tk.Button(self._frame1))
        #######################################################################

            

        #############################################################################################################
        # Player2 Buttons, Butrefs And Callbacks
        #############################################################################################################
        self._but1 = self._buts2[7]
        self._but1.config(image=self._player2.cards()[0][0], command=lambda:self._play2(self._butref1, self._but1))
        self._but1.grid(row=0, column=0,padx=6, pady=6)
        self._butref1.append(self._player2.cards()[0])
        
        self._but2 = self._buts2[8]
        self._but2.config(image=self._player2.cards()[1][0], command=lambda:self._play2(self._butref2, self._but2))
        self._but2.grid(row=0, column=1, padx=6, pady=6)
        self._butref2.append(self._player2.cards()[1])
        
        self._but3 = self._buts2[9]
        self._but3.config(image=self._player2.cards()[2][0], command=lambda:self._play2(self._butref3, self._but3))
        self._but3.grid(row=0, column=2, padx=6, pady=6)
        self._butref3.append(self._player2.cards()[2])
        
        self._but4 = self._buts2[10]
        self._but4.config(image=self._player2.cards()[3][0], command=lambda:self._play2(self._butref4, self._but4))
        self._but4.grid(row=0, column=3, padx=6, pady=6)
        self._butref4.append(self._player2.cards()[3])
        
        self._but5 = self._buts2[11]
        self._but5.config(image=self._player2.cards()[4][0], command=lambda:self._play2(self._butref5, self._but5))
        self._but5.grid(row=0, column=4, padx=6, pady=6)
        self._butref5.append(self._player2.cards()[4])
        ###########################################################################################################

        
        #####################################################################################
        # Played card and Mark card Image
        #####################################################################################
        self._played = tk.Label(self._frame2, image=self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][0])
        self._played.grid(row=1, column=1, sticky='e',)

        self._mark_but = tk.Button(self._root, image=self._misc_whot, command=self._mark)
        self._mark_but.grid(row=1, column=0,)
        #####################################################################################


        ####################################################################################
        # Computer Labs
        ####################################################################################
        self._lab1 = self._labs_comp[0]
        self._lab1.config(image=self._misc_whot1)
        self._lab1.grid(row=0, column=0, padx=6, pady=6)
        self._labref1.append(self._computer.cards()[0])

        self._lab2 = self._labs_comp[1]
        self._lab2.config(image=self._misc_whot2)
        self._lab2.grid(row=0, column=1, padx=6, pady=6)
        self._labref2.append(self._computer.cards()[1])

        self._lab3 = self._labs_comp[2]
        self._lab3.config(image=self._misc_whot3)
        self._lab3.grid(row=0, column=3, padx=6, pady=6)
        self._labref3.append(self._computer.cards()[2])

        self._lab4 = self._labs_comp[3]
        self._lab4.config(image=self._misc_whot4)
        self._lab4.grid(row=0, column=4, padx=6, pady=6)
        self._labref4.append(self._computer.cards()[3])

        self._lab5 = self._labs_comp[4]
        self._lab5.config(image=self._misc_whot5)
        self._lab5.grid(row=0, column=5, padx=6, pady=6)
        self._labref5.append(self._computer.cards()[4])

        self._LABS = []
        for i in [self._lab1, self._lab2, self._lab3, self._lab4, self._lab5]:
            self._LABS.append(i)
        #####################################################################################


        #####################################################################################
        # Menu's, Bindings, and Grids
        #####################################################################################
        menu_bar = tk.Menu(self._root)
        about_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='About', menu=about_menu)
        about_menu.add_command(label='Manual',accelerator='Ctrl+M', compound='left', command=self.Manual)
        self._root.config(menu=menu_bar)
        self._root.grid_columnconfigure(2, weight=1)
        self._root.bind_all("<Control-m>", self.Manual)
        self._root.bind_all("<Return>", self._mark)
        self._root.bind("<Any-ButtonRelease>", self.__CompPlayEngine)
        self._root.bind_all("<Any-ButtonRelease>", self._Checkmate)
        self._var = tk.StringVar()
        self._frame.grid(row=2, columnspan=4, sticky='we')
        self._main_frame3.grid(row=0, columnspan=4, sticky='we')

        ####################################################################################
        # Balloon Bindings and Inits
        ####################################################################################
        _ball_mark = Pmw.Balloon(self._root)
        _ball_lab = Pmw.Balloon(self._frame2)
        _ball_p2 = Pmw.Balloon(self._frame1)
        _ball_comp = Pmw.Balloon(self._frame3)
        for i in self._buts2:
            _ball_p2.bind(i, "Player1 Cards"+str(i))
        for i in self._labs_comp:
            _ball_comp.bind(i, "Computer Cards"+str(i))
        _ball_mark.bind(self._mark_but, "Click to go to Market (Add a card to your Deck)")
        _ball_lab.bind(self._played, "Played Cards")
        #####################################################################################

        #for i in self._buts2:
        #    i.bind("<Any-ButtonRelease>", self.__CompPlayEngine)
        ####################################################################################
        # Who Plays First
        ####################################################################################
        who_plays_first = ('player2', 'computer')
        final_choice = (choice(who_plays_first))
        if final_choice == 'player2':
            self.__checkcomp_played.insert(0,1)
            self.__check2_played.insert(0,0)
        else:
            self.__checkcomp_played.insert(0,0)
            self.__check2_played.insert(0,1)
        print(final_choice)
        pass
        ####################################################################################

        self.__CompPlayEngine()
       
    def _play2(self, butref=None, but=None, event=True):
        if butref and but:
            self._P2two()
            self._P2one()
            if self.__checkcomp_played[0]:
                try:
                    if self._player2.play(butref[0]):
                        self.__checkcomp_played.insert(0,0)
                        self.__check2_played.insert(0,1)
                            
                    if butref[0][1][1] == 20:
                        self.Window('whot')
                        
                    #elif self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][1] == 20:
                    #    print('equal to 20')
                        #print(self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][1])
                    #    if self._var.get() in self._values:
                    #        if butref[0][1][0] != self._var.get():
                    #            #raise Main.WhotException('Concur to your opponents wishes or you use the mart')
                    #            print("Not Implemented")
                    #            pass
                    #        elif butref[0][1][0] not in self._values:
                    #            print(self._values)
                    #            pass
                    self._played.configure(image=butref[0][0])
                    but.grid_forget()
                    butref.clear()
                except Main.WhotException:
                    tmb.showinfo("Invalid Move", "PLAY A VALID CARD")
            else:
                tmb.showinfo("Not Your Turn", "Its not your turn to play")

    def _P2two(self):
        if self.__checkcomp_played[0]:
            if self._computer._compup2[0] == 2:
                tmb.showinfo("Pick Two", "PICK TWO CARDS FROM THE MART")
                for i in self._buts2:
                    i.config(state='disabled')
                self._mark_but.config(command=self._check_p2)
                self._computer._compup2.insert(0,0)
    def _P2one(self):
        if self.__checkcomp_played[0]:
            if self._computer._compup14[0] == 14:
                tmb.showinfo("General Market", "GO TO MART ONCE")
                for i in self._buts2:
                    i.config(state='disabled')
                self._mark_but.config(command=self._check_p1)
                self._computer._compup14.insert(0,0)
    def _P2hold_on(self):
        if self.__checkcomp_played[0]:
            if self._computer._compup1[0] == 1:
                tmb.showinfo("Hold On", "HOLD ON......")
                self.__checkcomp_played.insert(0,0)
                self.__check2_played.insert(0,1)
                self._computer._compup1.insert(0,0)
                self.__CompPlayEngine()

    def _P2whot_20(self):
        if self.__checkcomp_played[0]:
            if self._computer._compup20[0] == 20:
                
                pass
                
    def _check_p2(self, event=None):
        self._mark(2)
        self.__checkcomp_played.insert(0,1)
        self.__check2_played.insert(0,0)
        if self._check2 == 2:
            for i in self._buts2:
                i.config(state='normal')
            self._check2 = 0
            self._mark_but.config(command=self._mark)
        else:
            pass

    def _check_p1(self, event=None):
        self._mark(1)
        if self._check1 == 1:
            for i in self._buts2:
                i.config(state='normal')
            self._check1 = 0
            self._mark_but.config(command=self._mark)
        pass
            

    def __CompPlayEngine(self, event=None):
        found_str=[0]
        found_num=[0]
        found_20=[0]
        if self.__check2_played[0]:
            try:
                for i in self._labs_refs:
                    if i == []:
                        pass
                    else:
                        if i[0][1][0] == self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][0]:
                            found_str.insert(0, i[0])
                            if i[0] in found_str:
                                self._labs_refs.pop(self._labs_refs.index(i))
                                break
                            print(i[0][1][0])
                            
                        elif i[0][1][1] == self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][1]:
                                found_num.insert(0, i[0])
                                if i[0] in found_num:
                                    self._labs_refs.pop(self._labs_refs.index(i))
                                    break
                                print(i[0][1][1])
                                
                        elif i[0][1][1] == 20:
                            found_20.insert(0,i[0])
                            if i[0] in found_20:
                                self._labs_refs.pop(self._labs_refs.index(i))
                                break
                        else:
                            if i[0][1][0] != self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][0]\
                                 or i[0][1][1] != self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][1]:
                                #print("Going to mart")
                                pass
                                
            except IndexError as e:
                print(e)
                pass
            
            print(found_str[0], '\n',found_num[0])
            if found_num[0]:
                self._play_comp(found_num[0], self._labs_comp[0])
                found_num.insert(0,0)
                
            elif not found_str[0] or found_num[0]:
                #sleep(0.5533)
                self._compMark()
                found_str.insert(0,0)
                found_num.insert(0,0)
                
            elif found_str[0]:
                self._play_comp(found_str[0], self._labs_comp[2])
                found_str.insert(0,0)

            elif found_20[0]:
                self._play_comp(found_20[0], self._labs_comp[1])
                
        else:
            print("It's not your turn to play")
            
    def __CompPlay20(self):
        found_word=[]
        card = self._var.get()
        
        if self.__check2_played[0]:
            if card in self._values
                try:
                    for i in self._labs_refs:
                        if i == []:
                            pass
                        else:
                            if i[0][1][0] in card:
                                found_word.insert(0,i[0])
                                if i[0] in found_word:
                                    self._labs_refs.pop(self._labs_refs.index(i))
                                    break

                if found_word[0]:
                    self._play_comp(found_num[0], self._labs_comp[3])

                else:
                    self._compMark()
        else:
            print("Not yet time to play")

    def _play_comp(self, labref=None, lab=None):
        if labref and lab:
            self._Comptwo()
            self._Compone()
            self._Comphold_on()
            if self.__check2_played[0]:
                if self._computer.play(labref):
                    self.__checkcomp_played.insert(0,1)
                    self.__check2_played.insert(0,0)
                    #try:
                        #self._P2two()
                        #self._P2one()
                        #self._P2hold_on()
                        if labref[1][1] == 20:
                        #    self.Window('whot')
                        #elif self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][1] == 20:
                        #    if self._var.get() in self._values:
                        #        if labref[1][0] != self._var.get():
                        #            print("Not Implemented")
                    #except IndexError:
                    #    pass
                    self._played.configure(image=labref[0])
                    lab.grid_forget()
                    #sleep(0.5234)
                    self._P2two()
                    self._P2one()
                    self._P2hold_on()
                #labref.clear()
            pass

    def _Comptwo(self):
        if self._player2._player2up2[0] == 2:
            for i in range(2):
                print('Picking 2.....')
                self._compMark()
            self._player2._player2up2.insert(0,0)
            
    def _Compone(self):
        if self._player2._player2up14[0] == 14:
            print("Going to gen mart")
            self._compMark()
            self._player2._player2up14.insert(0,0)

    def _Comphold_on(self):
        if self._player2._player2up1[0] == 1:
            self.__checkcomp_played.insert(0,1)
            self.__check2_played.insert(0,0)
            self._player2._player2up1.insert(0,0)

    def _Comp_whot20(self):
        if self._player2._player2up20[0] == 20:
            self.__CompPlay20()
            self._player2._player2up20.insert(0,0)
            pass

    def _popup(self, event=None):
        event.destroy()
        #print("player2 is asking for", self._var.get())
        return self._var.get()

    def Window(self, arg):
        if arg == 'whot':
            _toplev = tk.Toplevel(self._root)
            _toplev.transient(self._root)
            _toplev.title("Ask for a card")
            _toplev.grid()
            com = ttk.Combobox(_toplev, textvariable=self._var, values=self._values)
            self._var.set('choose a card')
            button = ttk.Button(_toplev, text='Ok',command=lambda: self._popup(_toplev))
            com.grid()
            button.grid()
    
    def Manual(self, event=None):
        "See the Manual of the Game"
        if self._root:
            text = tk.Toplevel(self._root)
        else:
            text = tk.Toplevel(tk.Tk())
        text.title("<Manual>")
        text.transient(self._root)
        text_lab = tks.ScrolledText(text, wrap='word')
        text_lab.grid(row=0, column=0, sticky=tk.NSEW)
        text_lab.insert(1.0, manual)
        text.grid_rowconfigure(1, weight=1)
        text.grid_columnconfigure(0, weight=1)
        text_lab.configure(state='disabled')
        ttk.Button(text, text="Ok", command=lambda: self._destroy(text)).grid()
    
    def _destroy(self, arg, event=None):
        arg.destroy()

    def _Checkmate(self, event=None):
        if len(self._player2.cards()) == 0:
            tmb.showinfo("Checkmate", "You are the winner")
            exit("Checkmate")
        elif len(self._computer.cards()) == 0:
            tmb.showinfo("Checkmate", "The Computer is the winner")
            exit("Checkmate")

    def _mainloop(self):
        self._root.mainloop()

    def _mark(self, power=None):
        if power:
            if power == 2:
                self._check2 +=1
            elif power == 1:
                self._check1 +=1

        
        if self._butref1 == []:
            self._player2.gomart()
            self._but1.config(image=self._player2.cards()[len(self._player2.cards())-1][0])
            self._butref1.append(self._player2.cards()[len(self._player2.cards())-1])
            self._but1.grid(row=0, column=0, padx=6, pady=6)
            
        elif self._butref2 == []:
            self._player2.gomart()
            self._but2.config(image=self._player2.cards()[len(self._player2.cards())-1][0])
            self._butref2.append(self._player2.cards()[len(self._player2.cards())-1])
            self._but2.grid(row=0, column=1, padx=6, pady=6)

        elif self._butref3 == []:
            self._player2.gomart()
            self._but3.config(image=self._player2.cards()[len(self._player2.cards())-1][0])
            self._butref3.append(self._player2.cards()[len(self._player2.cards())-1])
            self._but3.grid(row=0, column=2, padx=6, pady=6)

        elif self._butref4 == []:
            self._player2.gomart()
            self._but4.config(image=self._player2.cards()[len(self._player2.cards())-1][0])
            self._butref4.append(self._player2.cards()[len(self._player2.cards())-1])
            self._but4.grid(row=0, column=3, padx=6, pady=6)

        elif self._butref5 == []:
            self._player2.gomart()
            self._but5.config(image=self._player2.cards()[len(self._player2.cards())-1][0])
            self._butref5.append(self._player2.cards()[len(self._player2.cards())-1])
            self._but5.grid(row=0, column=4, padx=6, pady=6)
        
        elif self._butref6 == []:
            self._player2.gomart()
            but6 = self._buts2[0]
            but6.config(image=self._player2.cards()[len(self._player2.cards())-1][0], command=lambda:self._play2(self._butref6, but6))
            self._butref6.append(self._player2.cards()[len(self._player2.cards())-1])
            but6.grid(row=0, column=5,padx=6, pady=6)

        elif self._butref7 == []:
            self._player2.gomart()
            but7 = self._buts2[1]
            but7.config(image=self._player2.cards()[len(self._player2.cards())-1][0], command=lambda:self._play2(self._butref7, but7))
            self._butref7.append(self._player2.cards()[len(self._player2.cards())-1])
            but7.grid(row=0, column=6, padx=6, pady=6)
            pass

        elif self._butref8 == []:
            self._player2.gomart()
            but8 = self._buts2[2]
            but8.config(image=self._player2.cards()[len(self._player2.cards())-1][0], command=lambda:self._play2(self._butref8, but8))
            self._butref8.append(self._player2.cards()[len(self._player2.cards())-1])
            but8.grid(row=0, column=7, padx=6, pady=6)

        elif self._butref9 == []:
            self._player2.gomart()
            but9 = self._buts2[3]
            but9.config(image=self._player2.cards()[len(self._player2.cards())-1][0], command=lambda:self._play2(self._butref9, but9))
            self._butref9.append(self._player2.cards()[len(self._player2.cards())-1])
            but9.grid(row=0, column=8, padx=6, pady=6)

        elif self._butref10 == []:
            self._player2.gomart()
            but10 = self._buts2[4]
            but10.config(image=self._player2.cards()[len(self._player2.cards())-1][0], command=lambda:self._play2(self._butref10, but10))
            self._butref10.append(self._player2.cards()[len(self._player2.cards())-1])
            but10.grid(row=0, column=9, padx=6, pady=6)

        elif self._butref11 == []:
            self._player2.gomart()
            but11 = self._buts2[5]
            but11.config(image=self._player2.cards()[len(self._player2.cards())-1][0], command=lambda:self._play2(self._butref11, but11))
            self._butref11.append(self._player2.cards()[len(self._player2.cards())-1])
            but11.grid(row=0, column=10, padx=6, pady=6)

        elif self._butref12 == []:
            self._player2.gomart()
            but12 = self._buts2[6]
            but12.config(image=self._player2.cards()[len(self._player2.cards())-1][0], command=lambda:self._play2(self._butref12, but12))
            self._butref12.append(self._player2.cards()[len(self._player2.cards())-1])
            but12.grid(row=0, column=11, padx=6, pady=6)

        self.__checkcomp_played.insert(0,0)
        self.__check2_played.insert(0,1)
            

    def _compMark(self):
        self.__checkcomp_played.insert(0,1)
        self.__check2_played.insert(0,0)
        
        if self._labref1 == []:
            self._computer.gomart()
            self._lab1.config(image=self._misc_whot1)
            self._labref1.append(self._computer.cards()[len(self._computer.cards())-1])
            self._lab1.grid(row=0, column=1, padx=6, pady=6)

        elif self._labref2 == []:
            self._computer.gomart()
            self._lab2.config(image=self._misc_whot2)
            self._labref2.append(self._computer.cards()[len(self._computer.cards())-1])
            self._lab2.grid(row=0, column=2, padx=6, pady=6)

        elif self._labref3 == []:
            self._computer.gomart()
            self._lab3.config(image=self._misc_whot3)
            self._labref3.append(self._computer.cards()[len(self._computer.cards())-1])
            self._lab3.grid(row=0, column=3, padx=6, pady=6)

        elif self._labref4 == []:
            self._computer.gomart()
            self._lab4.config(image=self._misc_whot4)
            self._labref4.append(self._computer.cards()[len(self._computer.cards())-1])
            self._lab4.grid(row=0, column=4, padx=6, pady=6)

        elif self._labref5 == []:
            self._computer.gomart()
            self._lab5.config(image=self._misc_whot5)
            self._labref5.append(self._computer.cards()[len(self._computer.cards())-1])
            self._lab5.grid(row=0, column=5, padx=6, pady=6)
                
        else:
            if self._labref6 == []:
                self._computer.gomart()
                self._lab6 = self._labs_comp[5]
                self._lab6.config(image=self._misc_whot6)
                self._labref6.append(self._computer.cards()[len(self._computer.cards())-1])
                self._lab6.grid(row=0, column=6, padx=6, pady=6)

            elif self._labref7 == []:
                self._computer.gomart()
                self._lab7 = self._labs_comp[6]
                self._lab7.config(image=self._misc_whot7)
                self._labref7.append(self._computer.cards()[len(self._computer.cards())-1])
                self._lab7.grid(row=0, column=7, padx=6, pady=6)

            elif self._labref8 == []:
                self._computer.gomart()
                self._lab8 = self._labs_comp[7]
                self._lab8.config(image=self._misc_whot8)
                self._labref8.append(self._computer.cards()[len(self._computer.cards())-1])
                self._lab8.grid(row=0, column=8, padx=6, pady=6)

            elif self._labref9 == []:
                self._computer.gomart()
                self._lab9 = self._labs_comp[8]
                self._lab9.config(image=self._misc_whot9)
                self._labref9.append(self._computer.cards()[len(self._computer.cards())-1])
                self._lab9.grid(row=0, column=9, padx=6, pady=6)

            elif self._labref10 == []:
                self._computer.gomart()
                self._lab10 = self._labs_comp[9]
                self._lab10.config(image=self._misc_whot9)
                self._labref10.append(self._computer.cards()[len(self._computer.cards())-1])
                self._lab10.grid(row=0, column=10, padx=6, pady=6)

            elif self._labref11 == []:
                self._computer.gomart()
                self._lab11 = self._labs_comp[10]
                self._lab11.config(image=self._misc_whot10)
                self._labref11.append(self._computer.cards()[len(self._computer.cards())-1])
                self._lab11.grid(row=0, column=11, padx=6, pady=6)
                    
                pass
            
            pass




app = WhotGtk()
app._mainloop()
    
