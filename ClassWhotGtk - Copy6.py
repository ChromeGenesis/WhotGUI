#!/usr/bin/python3

from tkinter import ttk
import tkinter as tk
import tkinter.scrolledtext as tks
from manual import manual
from ImageCopy import images
from random import choice
import Main
import Pmw
import tkinter.messagebox as tmb
from time import sleep
#from playsound import playsound
#from muzic import PlayMusic
from birdseye import eye

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

        ###################################################################
        # Music
        ###################################################################
        #self._music = playsound(".//PEP - FAST (Bass Boosted)-DqMUfr-1RSU.wav")
        #self._music.load_play()

        ##################################################################
        # To Check who played last
        ##################################################################
        self.__check2_played=[]
        self.__checkcomp_played=[]
        ##################################################################
        
        self._check2 = 0
        self._check1 = 0
        self._check20 = None
        self._values = ['star', 'circle', 'cross', 'square', 'triangle']

        ###################################################################
        # Player2 Butrefs
        ###################################################################
        self._but_refs=[]
        for i in range(20):
            self._but_refs.append([])
        #####################################################################

        #####################################################################
        # Computer Labrefs
        #####################################################################
        self._labs_refs = []
        for i in range(20):
            self._labs_refs.append([])
            
        self._found_str = []
        self._found_num = []
        self._found_20 = []
        #####################################################################

        

        ######################################################################
        # Initialisation of Buts and Labs
        ######################################################################
        self._labs_comp = []
        for i in range(20):
            self._labs_comp.append(tk.Label(self._frame3))

        self._buts2 = []
        for i in range(20):
            self._buts2.append(tk.Button(self._frame1))
        #######################################################################

            

        #############################################################################################################
        # Player2 Buttons, Butrefs And Callbacks
        #############################################################################################################
        self._p2_buts={0:self._buts2[0], 1:self._buts2[1], 2:self._buts2[2], 3:self._buts2[3],
                       4:self._buts2[4], 5:self._buts2[5], 6:self._buts2[6], 7:self._buts2[7],
                       8:self._buts2[8], 9:self._buts2[9], 10:self._buts2[10], 11:self._buts2[11],
                       12:self._buts2[12], 13:self._buts2[13], 14:self._buts2[14], 15:self._buts2[15],
                       16:self._buts2[16], 17:self._buts2[17], 18:self._buts2[18], 19:self._buts2[19],} 
        
        self._but1 = self._p2_buts[0]
        self._but1.config(image=self._player2.cards()[0][0], command=lambda:self._play2(self._but_refs[0], self._but1))
        self._but1.grid(row=0, column=0,padx=6, pady=6)
        self._but_refs[0].append(self._player2.cards()[0])
        
        self._but2 = self._p2_buts[1]
        self._but2.config(image=self._player2.cards()[1][0], command=lambda:self._play2(self._but_refs[1], self._but2))
        self._but2.grid(row=0, column=1, padx=6, pady=6)
        self._but_refs[1].append(self._player2.cards()[1])
        
        self._but3 = self._p2_buts[2]
        self._but3.config(image=self._player2.cards()[2][0], command=lambda:self._play2(self._but_refs[2], self._but3))
        self._but3.grid(row=0, column=2, padx=6, pady=6)
        self._but_refs[2].append(self._player2.cards()[2])
        
        self._but4 = self._p2_buts[3]
        self._but4.config(image=self._player2.cards()[3][0], command=lambda:self._play2(self._but_refs[3], self._but4))
        self._but4.grid(row=0, column=3, padx=6, pady=6)
        self._but_refs[3].append(self._player2.cards()[3])
        
        self._but5 = self._p2_buts[4]
        self._but5.config(image=self._player2.cards()[4][0], command=lambda:self._play2(self._but_refs[4], self._but5))
        self._but5.grid(row=0, column=4, padx=6, pady=6)
        self._but_refs[4].append(self._player2.cards()[4])
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

        self._complab_ref={0:self._labs_comp[0], 1:self._labs_comp[1], 2:self._labs_comp[2],
                           3:self._labs_comp[3], 4:self._labs_comp[4], 5:self._labs_comp[5],
                           6:self._labs_comp[6], 7:self._labs_comp[7], 8:self._labs_comp[8],
                           9:self._labs_comp[9], 10:self._labs_comp[10], 11:self._labs_comp[11],
                           12:self._labs_comp[12], 13:self._labs_comp[13], 14:self._labs_comp[14],
                           15:self._labs_comp[15], 16:self._labs_comp[16], 17:self._labs_comp[17],
                           18:self._labs_comp[18], 19:self._labs_comp[19],}
        
        for i in range(5):
            self._complab_ref[i].config(image=self._misc_whot1)
            self._complab_ref[i].grid(row=0, column=i, padx=6, pady=6)
            self._labs_refs[i].append(self._computer.cards()[i])
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
        #self._root.bind_all("<Return>", self._mark)
        self._root.bind("<Any-ButtonRelease>", self.__CompPlayEngine)
        #self._root.bind_all("<Any-ButtonRelease>", self._Checkmate)
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
        #self._mark_but.bind("<Any-ButtonRelease>", self.__CompPlayEngine)
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
                        #self.Window('whot')
                        pass
                    elif self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][1] == 20:
                        print('equal to 20')
                        #print(self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][1])
                        if self._var.get() in self._values:
                            if butref[0][1][0] != self._var.get():
                                #raise Main.WhotException('Concur to your opponents wishes or you use the mart')
                                print("Not Implemented")
                                pass
                            elif butref[0][1][0] not in self._values:
                                print(self._values)
                                pass
                    self._played.configure(image=butref[0][0])
                    but.grid_forget()
                    butref.clear()
                    self._Comphold_on()
                    self._Comptwo()
                    self._Compone()
                    self._Compsuspension()
                    self._Checkmate()
                except Main.WhotException:
                    tmb.showinfo("Invalid Move", "PLAY A VALID CARD")
            else:
                tmb.showinfo("Not Your Turn", "Its not your turn to play")

    def _P2two(self):
        #if self.__checkcomp_played[0]:
        if self._computer._compup2[0] == 2:
            tmb.showinfo("Pick Two", "PICK TWO CARDS FROM THE MART")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(command=self._check_p2)
            self._computer._compup2.insert(0,0)
    def _P2one(self):
        #if self.__checkcomp_played[0]:
        if self._computer._compup14[0] == 14:
            tmb.showinfo("General Market", "GO TO MART ONCE")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(command=self._check_p1)
            self._computer._compup14.insert(0,0)
    def _P2hold_on(self):
        #if self.__checkcomp_played[0]:
        if self._computer._compup1[0] == 1:
            tmb.showinfo("Hold On", "HOLD ON......")
            self.__checkcomp_played.insert(0,0)
            self.__check2_played.insert(0,1)
            self._computer._compup1.insert(0,0)
            self.__CompPlayEngine()
    def _P2suspension(self):
        if self._computer._compup8[0] == 8:
            tmb.showinfo("Hold On", "SUSPENSION")
            self.__checkcomp_played.insert(0,0)
            self.__check2_played.insert(0,1)
            self._computer._compup8.insert(0,0)
            self.__CompPlayEngine()
    def _P2whot_20(self):
        if self._computer._compup20[0] == 20:
            
            #tmb.
            pass    
    def _check_p2(self, event=None):
        self._mark(2)
        self.__checkcomp_played.insert(0,1)
        self.__check2_played.insert(0,0)
        if self._check2 == 2:
            self.__check2_played.insert(0,1)
            self.__checkcomp_played.insert(0,0)
            #self.__CompPlayEngine()
            for i in self._buts2:
                i.config(state='normal')
            self._check2 = 0
            self._mark_but.config(command=self._mark)
        
    
    def _check_p1(self, event=None):
        self._mark(1)
        if self._check1 == 1:
            self.__check2_played.insert(0,1)
            self.__checkcomp_played.insert(0,0)
            #self.__CompPlayEngine()
            for i in self._buts2:
                i.config(state='normal')
            self._check1 = 0
            self._mark_but.config(command=self._mark)

    #@eye
    def __CompPlayEngine(self, event=None):
        if self.__check2_played[0]:
            try:
                for i in enumerate(self._labs_refs):
                    if i[1] == []:
                        pass
                    else:
                        if i[1][0][1][0] == self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][0]:
                            self._found_str.append([i[0], i[1]])
                            self._labs_refs.insert(self._labs_refs.index(i[1]), [])
                            self._labs_refs.pop(self._labs_refs.index(i[1]))
                            break
                        
                        elif not self._found_str:
                            if i[1][0][1][1] == self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][1]:
                                self._found_num.append([i[0], i[1]])
                                self._labs_refs.insert(self._labs_refs.index(i[1]), [])
                                self._labs_refs.pop(self._labs_refs.index(i[1]))
                                break
                
            except IndexError as e:
                print(e)
                pass
            
            print('found_str :',self._found_str, '\n','found_num :',self._found_num,)# '\n', 'found_20 :',
                  #self._found_20)

           
            if self._found_str:
                try:
                    for i in self._found_str:
                        if i[1][0][1][0] == self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][0]:
                            self._play_comp(i[1][0], self.foo(i[0]), self._found_str)
                            break
                except IndexError as e:
                    print(1,':',e)
                    
            elif self._found_num:
                try:
                    for i in self._found_num:
                        if i[1][0][1][1] == self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][1]:
                            self._play_comp(i[1][0], self.foo(i[0]), self._found_num)
                            break
                except IndexError as e:
                    print(2,':',e)

            #elif self._found_20:
            #    for i in self._found_20:
            #        if i:
            #            self._play_comp(i, self._labs_comp[4], self._found_20)
            #            break
                    
            else:
                self._compMark()
                
        else:
            print("It's not your turn to play")

    #@eye        
    def foo(self, element):
        for i in range(20):
            if i == element:
                comp_lab = self._complab_ref.get(i)
                return comp_lab
            
    def _CompPlay20(self):
        card = self._var.get()
        if self.__check2_played[0]:
            if card in self._values:
                try:
                    for i in self._labs_refs:
                        if i == []:
                            pass
                        else:
                            if i[0][1][0] == card:
                                self._found_20.append(i[0])
                                i.clear()
                                break
                except IndexError:
                    pass
            
            print("\nself._found_20 :", self._found_20)
            if self._found_20:
                for i in self._found_20:
                    self._play_comp(i, self._labs_comp[0], self._found_20)
                    break
            
            else:
                self._compMark()
        else:
            print("not yet time to play")
            
    def _play_comp(self, labref=None, lab=None, found=None):#, event=None):
        if labref and lab:
            self._Comptwo()
            self._Compone()
            self._Comphold_on()
            self._Compsuspension()
            #self._Comp_whot_20()
            if self.__check2_played[0]:
                if self._computer.play(labref):
                    #try:
                    #    if labref[1][1] == 20:
                    #        self.Window('whot')
                    #    elif self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][1] == 20:
                    #        if self._var.get() in self._values:
                    #            if labref[1][0] != self._var.get():
                    #                print("Not Implemented")
                    #except IndexError:
                    #    pass
                    self._played.configure(image=labref[0])
                    lab.grid_forget()
                    #sleep(0.5234)
                    if found:
                        print('clearing',lab, 'now....')
                        found.clear()
                    self._P2two()
                    self._P2one()
                    self._P2hold_on()
                    self._P2suspension()
                    self.__checkcomp_played.insert(0,1)
                    self.__check2_played.insert(0,0)
                    self._Checkmate()
                    
                #labref.clear() 
            else:
                print("Computer please chill its not your turn to play....")
            pass

    def _Comptwo(self):
        if self._player2._player2up2[0] == 2:
            for i in range(2):
                print('picking two')
                self._compMark()
                self.__checkcomp_played.insert(0,0)
                self.__check2_played.insert(0,1)
            self._player2._player2up2.insert(0,0)
            self.__checkcomp_played.insert(0,1)
            self.__check2_played.insert(0,0)
            
    def _Compone(self):
        if self._player2._player2up14[0] == 14:
            print("Going to gen mart")
            self._compMark()
            self._player2._player2up14.insert(0,0)
            self.__checkcomp_played.insert(0,1)
            self.__check2_played.insert(0,0)

    def _Comphold_on(self):
        if self._player2._player2up1[0] == 1:
            self.__checkcomp_played.insert(0,1)
            self.__check2_played.insert(0,0)
            self._player2._player2up1.insert(0,0)
            
    def _Compsuspension(self):
        if self._player2._player2up8[0] == 8:
            self.__checkcomp_played.insert(0,1)
            self.__check2_played.insert(0,0)
            self._player2._player2up8.insert(0,0)
            
    def _Comp_whot_20(self):
        if self._player2._player2up20[0] == 20:
            self._CompPlay20()
            self._player2._player2up20.insert(0,0)
            
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

    def _Checkmate(self):
        if len(self._player2.cards()) == 0:
            tmb.showinfo("Checkmate", "You are the winner")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(state='disabled')
            #self.__checkcomp_played.insert(0,1)
            #self.__check2_played.insert(0,1)
            
        elif len(self._computer.cards()) == 0:
            tmb.showinfo("Checkmate", "The Computer is the winner")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(state='disabled')
            #self.__check2_played.insert(0,1)
            #self.__checkcomp_played.insert(0,1)

    def _mainloop(self):
        self._root.mainloop()

    #@eye    
    def _mark(self, power=None):
        if power:
            if power == 2:
                self._check2 +=1
            elif power == 1:
                self._check1 +=1

        for i in self._but_refs:
            if i == []:
                g=self._but_refs.index(i)
                self._player2.gomart()
                self._but_refs[g].append(self._player2.cards()[len(self._player2.cards())-1])
                for o in range(20):
                    if o == g:
                        new_but = self._p2_buts.get(o)
                        new_but.config(image=self._player2.cards()[len(self._player2.cards())-1][0], command=lambda:self._play2(self._but_refs[o], self._p2_buts[o]))
                        new_but.grid(row=0, column=g, padx=6, pady=6)
                        break
                break

        self.__checkcomp_played.insert(0,0)
        self.__check2_played.insert(0,1)
            

    def _compMark(self):
        if self.__check2_played[0]:
            for i in self._labs_refs:
                if i == []:
                    g=self._labs_refs.index(i)
                    self._computer.gomart()
                    self._labs_refs[g].append(self._computer.cards()[len(self._computer.cards())-1])
                    for o in range(20):
                        if o == g:
                            new_lab = self._complab_ref.get(o)
                            new_lab.config(image=self._misc_whot1)
                            new_lab.grid(row=0, column=g, padx=6, pady=6)
                            break
                    break

            self.__checkcomp_played.insert(0,1)
            self.__check2_played.insert(0,0)


if __name__ == '__main__':
    app = WhotGtk()
    #app._mainloop()
