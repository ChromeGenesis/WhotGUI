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
import simpleaudio as sa


class WhotGtk(images):
    '''Naija Whot Game in Grand Style'''

    def __init__(self):
        self._root = Pmw.initialise()
        self._root.geometry('790x670')
        self._root.title('Whot Game')
        super().__init__()
        self._player2_frame = Pmw.ScrolledFrame(self._root, labelpos='s', usehullsize=1,
                                                hull_width=100,
                                                hull_height=225,
                                                label_text='PLAYER  =>')

        self._played_cards_frame = tk.Frame(self._root, bg='aquamarine')

        self._comp_frame = Pmw.ScrolledFrame(self._root, labelpos='n', usehullsize=1,
                                             hull_width=100,
                                             hull_height=225,
                                             label_text='COMPUTER  =>')

        self._comp_frame_int = self._comp_frame.interior()
        self._p2_frame_int = self._player2_frame.interior()

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
        self.__check2_played = []
        self.__checkcomp_played = []
        ##################################################################
        self.__check_checkmate = False

        self._check2 = 0
        self._check1 = 0
        self._values = ['star', 'circle', 'cross', 'square', 'triangle']

        ###################################################################
        # Player2 Butrefs
        ###################################################################
        self._but_refs = []
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
            self._labs_comp.append(tk.Label(self._comp_frame_int))

        self._buts2 = []
        for i in range(20):
            self._buts2.append(tk.Button(self._p2_frame_int))
        #######################################################################

        #############################################################################################################
        # Player2 Buttons, Butrefs And Callbacks
        #############################################################################################################
        self._p2_buts = {}
        for i in range(20):
            self._p2_buts[i] = self._buts2[i]

        self._but1 = self._p2_buts[0]
        self._but1.config(image=self._player2.cards()[0][0], command=lambda: self._play2(self._but_refs[0], self._but1))
        self._but1.grid(row=0, column=0, padx=6, pady=6)
        self._but_refs[0].append(self._player2.cards()[0])

        self._but2 = self._p2_buts[1]
        self._but2.config(image=self._player2.cards()[1][0], command=lambda: self._play2(self._but_refs[1], self._but2))
        self._but2.grid(row=0, column=1, padx=6, pady=6)
        self._but_refs[1].append(self._player2.cards()[1])

        self._but3 = self._p2_buts[2]
        self._but3.config(image=self._player2.cards()[2][0], command=lambda: self._play2(self._but_refs[2], self._but3))
        self._but3.grid(row=0, column=2, padx=6, pady=6)
        self._but_refs[2].append(self._player2.cards()[2])

        self._but4 = self._p2_buts[3]
        self._but4.config(image=self._player2.cards()[3][0], command=lambda: self._play2(self._but_refs[3], self._but4))
        self._but4.grid(row=0, column=3, padx=6, pady=6)
        self._but_refs[3].append(self._player2.cards()[3])

        self._but5 = self._p2_buts[4]
        self._but5.config(image=self._player2.cards()[4][0], command=lambda: self._play2(self._but_refs[4], self._but5))
        self._but5.grid(row=0, column=4, padx=6, pady=6)
        self._but_refs[4].append(self._player2.cards()[4])
        ###########################################################################################################

        #####################################################################################
        # Played card and Mark card Image
        #####################################################################################
        self._played = tk.Label(self._played_cards_frame,
                                image=self._whot.PlayedCards()[len(self._whot.PlayedCards()) - 1][0])

        self._mark_but = tk.Button(self._root, image=self._misc_whot, command=self._p2_mark)

        #####################################################################################

        ####################################################################################
        # Computer Labs
        ####################################################################################
        self._complab_ref = {}

        for i in range(20):
            self._complab_ref[i] = self._labs_comp[i]

        for i in range(5):
            self._complab_ref[i].config(image=self._misc_whot1)
            self._complab_ref[i].grid(row=0, column=i, padx=6, pady=6)
            self._labs_refs[i].append(self._computer.cards()[i])
        #####################################################################################

        #####################################################################################
        # Menu
        #####################################################################################
        menu_bar = tk.Menu(self._root)
        about_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='About', menu=about_menu)
        about_menu.add_command(label='Manual', accelerator='Ctrl+M', compound='left', command=self.Manual)
        self._root.config(menu=menu_bar)

        ####################################################################################
        # Grids
        ####################################################################################
        self._player2_frame.grid(row=3, columnspan=4, sticky='we')
        self._comp_frame.grid(row=1, columnspan=4, sticky='we')
        self._played_cards_frame.grid(row=2, column=2)
        self._played.grid(row=1, column=1, sticky='e', )
        self._mark_but.grid(row=2, column=0, sticky='w')

        self._root.grid_columnconfigure(2, weight=1)
        self._played_cards_frame.grid_columnconfigure(0, weight=1)
        self._var = tk.StringVar()

        self._hover_comp = tk.Label(self._root, text="Number of computer cards:5")
        self._hover_p2 = tk.Label(self._root, text="Number of your cards :5")
        self._hover_p2.grid(row=4, column=0, sticky='w')
        self._hover_comp.grid(row=0, column=0)

        ##################################################################################
        # Binding's
        ##################################################################################
        self._root.bind_all("<Control-m>", self.Manual)
        # self._root.bind_all("<Return>", self._p2_mark)
        ####################################################################################
        # Balloon Bindings and Inits
        ####################################################################################
        _ball_mark = Pmw.Balloon(self._root)
        _ball_lab = Pmw.Balloon(self._played_cards_frame)
        _ball_p2 = Pmw.Balloon(self._p2_frame_int)
        _ball_comp = Pmw.Balloon(self._comp_frame_int)
        for i in self._buts2:
            _ball_p2.bind(i, "Player2 Cards" + str(i))
        for i in self._labs_comp:
            _ball_comp.bind(i, "Computer Cards" + str(i))
        _ball_mark.bind(self._mark_but, "Click to go to Market (Add a card to your Deck)")
        _ball_lab.bind(self._played, "Played Cards")
        #####################################################################################

        # Music
        wave_obj = sa.WaveObject.from_wave_file('./Gryffin & Carly Rae Jepsen - OMG (Lyrics) Anki Remix-Ou92y60LzFI.wav')
        play_obj = wave_obj.play()
        
        ####################################################################################
        # Who Plays First
        ####################################################################################
        who_plays_first = ('player2', 'computer')
        final_choice = (choice(who_plays_first))
        if final_choice == 'player2':
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)
        else:
            self.__checkcomp_played.insert(0, 0)
            self.__check2_played.insert(0, 1)
        print(final_choice)
        pass
        ####################################################################################

        self.__CompPlayEngine()

    # @dec(self, player)
    def _player_turn(self, player):
        '''Return bool value for the valid player to play first or next'''
        if player:
            if player == 'comp':
                if self.__check2_played[0]:
                    return True
                else:
                    return False
            elif player == 'p2':
                if self.__checkcomp_played[0]:
                    return True
                else:
                    return False

    def _check_comp_num(self, event=None):
        '''check number of cards left/remaining for the computer and update'''
        if len(self._computer.cards()) == 1:
            self._hover_comp.config(text="Last Card....")
        else:
            self._hover_comp.config(text="Number of computer cards :" + str(len(self._computer.cards())))
        return None

    def _check_p2_num(self, event=None):
        '''check number of cards left/remaining for player2 and update'''
        if len(self._player2.cards()) == 1:
            self._hover_p2.config(text="Last Card.....")
        else:
            self._hover_p2.config(text="Number of your cards :" + str(len(self._player2.cards())))
        return None

    def _play2(self, butref=None, but=None, event=True):
        '''For player2 (actual player) to play his or her valid card'''
        if butref and but:
            # if self.__check_requested:
            #    if butref[0][1][0] == self._requested:
            if self._player_turn('p2') and not self.__check_checkmate:
                try:
                    if self._player2.play(butref[0]):
                        self.__checkcomp_played.insert(0, 0)
                        self.__check2_played.insert(0, 1)

                        if butref[0][1][1] == 20:
                            self.Window('whot')
                            self.__checkcomp_played.insert(0, 1)
                            self.__check2_played.insert(0, 0)

                        self._played.configure(image=butref[0][0])
                        but.after(500, self.__CompPlayEngine)
                        but.grid_forget()
                        butref.clear()
                        self._check_p2_num()
                        self._comp_hold_on()
                        self._comp_two()
                        self._comp_one()
                        self._comp_suspension()
                        self._checkmate()
                except Main.WhotException:
                    tmb.showwarning("Invalid Move", "PLAY A VALID CARD")
            else:
                tmb.showinfo("Not Your Turn", "Its not your turn to play")

    def _p2_two(self):
        '''makes player2 to pick two cards mandatorily if computer gives him/her any card with
        the number '2' in it'''
        # if self.__checkcomp_played[0]:
        if self._computer.compup2[0] == 2:
            tmb.showinfo("Pick Two", "PICK TWO CARDS FROM THE MART")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(command=self._check_p2)
            self._computer.compup2.insert(0, 0)

    def _p2_one(self):
        """makes player2 to go to general market (which is to pick one card only from the mart) mandatorily
        if and when the computer gives him/her any card with the number '14' in it"""
        # if self._player_turn('p2'):
        if self._computer.compup14[0] == 14:
            tmb.showinfo("General Market", "GO TO MART ONCE")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(command=self._check_p1)
            self._computer.compup14.insert(0, 0)

    def _p2_hold_on(self):
        """makes player2 to hold on until the computer plays another card or goes to the mart mandatorily
        if the computer gives him/her any card with the number '1' in it"""
        # if self._player_turn('p2'):
        if self._computer.compup1[0] == 1:
            tmb.showinfo("Hold On", "HOLD ON......")
            self.__checkcomp_played.insert(0, 0)
            self.__check2_played.insert(0, 1)
            self._computer.compup1.insert(0, 0)
            self._checkmate()
            self.__CompPlayEngine()

    def _p2_suspension(self):
        """Just like hold on, it suspends player2 until the computer plays another card or goes to mart"""
        # if self._player_turn('p2'):
        if self._computer.compup8[0] == 8:
            tmb.showinfo("Hold On", "SUSPENSION")
            self.__checkcomp_played.insert(0, 0)
            self.__check2_played.insert(0, 1)
            self._computer.compup8.insert(0, 0)
            self._checkmate()
            self.__CompPlayEngine()

    def _check_p2(self, event=None):
        """Checks whether player2 clicked the mart button twice (in other words, checks whether player2 has
        picked two cards) and then unfreezes player2 cards (buttons) - for PICK TWO"""
        self._p2_mark(2)
        self.__checkcomp_played.insert(0, 1)
        self.__check2_played.insert(0, 0)
        if self._check2 == 2:
            self.__check2_played.insert(0, 1)
            self.__checkcomp_played.insert(0, 0)
            # self.__CompPlayEngine()
            for i in self._buts2:
                i.config(state='normal')
            self._check2 = 0
            self._mark_but.config(command=self._p2_mark)

    def _check_p1(self, event=None):
        """Checks whether player2 clicked the mart button once (in other words, checks whether player2 has
        picked one card) and then unfreezes player2 cards (buttons) - for GENERAL MARKET"""
        self._p2_mark(1)
        if self._check1 == 1:
            self.__check2_played.insert(0, 1)
            self.__checkcomp_played.insert(0, 0)
            # self.__CompPlayEngine()
            for i in self._buts2:
                i.config(state='normal')
            self._check1 = 0
            self._mark_but.config(command=self._p2_mark)

    def __CompPlayEngine(self, event=None):
        """Engine for determining what valid cards the computer has and can play....
        if after all and no valid card is found, the computer is forced to go to market"""
        if self.__check2_played[0] and not self.__check_checkmate:
            try:
                for i in enumerate(self._labs_refs):
                    if not i[1]:
                        pass
                    else:
                        if i[1][0][1][1] == 20:
                            self._found_20.append([i[0], i[1]])
                            self._labs_refs.insert(self._labs_refs.index(i[1]), [])
                            self._labs_refs.pop(self._labs_refs.index(i[1]))
                            break

                        if not self._found_20:
                            if i[1][0][1][1] == self._whot.PlayedCards()[len(self._whot.PlayedCards()) - 1][1][1]:
                                self._found_num.append([i[0], i[1]])
                                self._labs_refs.insert(self._labs_refs.index(i[1]), [])
                                self._labs_refs.pop(self._labs_refs.index(i[1]))
                                break

                        if not self._found_num:
                            if i[1][0][1][0] == self._whot.PlayedCards()[len(self._whot.PlayedCards()) - 1][1][0]:
                                self._found_str.append([i[0], i[1]])
                                self._labs_refs.insert(self._labs_refs.index(i[1]), [])
                                self._labs_refs.pop(self._labs_refs.index(i[1]))
                                break

            except IndexError as e:
                print(e)
                pass

            if self._found_20:
                try:
                    for i in self._found_20:
                        if i:
                            self._play_comp(i[1][0], self._get_pos(i[0]), self._found_20)
                            break
                except IndexError:
                    pass

            elif self._found_num:
                try:
                    for i in self._found_num:
                        if i[1][0][1][1] == self._whot.PlayedCards()[len(self._whot.PlayedCards()) - 1][1][1]:
                            self._play_comp(i[1][0], self._get_pos(i[0]), self._found_num)
                            break
                except IndexError as e:
                    print(2, ':', e)
                    pass

            elif self._found_str:
                try:
                    for i in self._found_str:
                        if i[1][0][1][0] == self._whot.PlayedCards()[len(self._whot.PlayedCards()) - 1][1][0]:  # \
                            # or self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][0] == 20:
                            self._play_comp(i[1][0], self._get_pos(i[0]), self._found_str)
                            break
                except IndexError as e:
                    print(1, ':', e)
                    pass

            else:
                self._comp_mark()

        else:
            print("It's not your turn to play")

    def _get_pos(self, element):
        """gets the position of the computer label in the self._complab_ref dict"""
        for i in range(20):
            if i == element:
                comp_lab = self._complab_ref.get(i)
                return comp_lab

    def _comp_play_20(self):
        found_1, found_2, found_8, found_14, found_none = [], [], [], [], []
        for i in enumerate(self._labs_refs):
            if not i[1]:
                pass
            else:
                if i[1][0][1][1] == 1:
                    found_1.append(i[1][0][1][0])
                    break
                if not found_1:
                    if i[1][0][1][1] == 2:
                        found_2.append(i[1][0][1][0])
                        break
                if not found_1 and not found_2:
                    if i[1][0][1][1] == 8:
                        found_8.append(i[1][0][1][0])
                        break
                    if not found_8:
                        if i[1][0][1][1] == 14:
                            found_14.append(i[1][0][1][0])
                            break
                        if not found_14:
                            if i[1][0][1][0] != 'whot':
                                found_none.append(i[1][0][1][0])

        if found_1 or found_2 or found_8 or found_14:
            self._player2.check_requested = True

        if found_1:
            tmb.showinfo("Request", "I NEED " + found_1[0].upper())
            self._player2.request = found_1[0]

        elif found_2:
            tmb.showinfo("Request", "I NEED " + found_2[0].upper())
            self._player2.request = found_2[0]

        elif found_8:
            tmb.showinfo("Request", "I NEED " + found_8[0].upper())
            self._player2.request = found_8[0]

        elif found_14:
            tmb.showinfo("Request", "I NEED " + found_14[0].upper())
            self._player2.request = found_14[0]
        else:
            tmb.showinfo("Request", "I NEED " + found_none[0].upper())
            self._player2.request = found_none[0]
            print("found none: "+found_none[0])

    def _Comp_response_to_20(self):
        card = self._var.get()
        if self.__check2_played[0] and not self.__check_checkmate:
            if self._player_turn('comp'):
                try:
                    for i in enumerate(self._labs_refs):
                        if not i[1]:
                            pass
                        else:
                            if i[1][0][1][0] == card:
                                self._found_20.append([i[0], i[1]])
                                self._labs_refs.insert(self._labs_refs.index(i[1]), [])
                                self._labs_refs.pop(self._labs_refs.index(i[1]))
                                break
                except IndexError:
                    pass

            if self._found_20:
                for i in self._found_20:
                    self._play_comp(i[1][0], self._get_pos(i[0]), self._found_20)
                    break

            else:
                print("don't have the card going to mart")
                self._comp_mark()
        else:
            print("not yet time to play")

    def _play_comp(self, labref=None, lab=None, found=None):
        """Plays any cards that are valid, from CompPlayEngine"""
        if labref and lab:
            # if self.__check2_played[0]:
            if self._player_turn('comp') and not self.__check_checkmate:
                if self._computer.play(labref):
                    self._played.configure(image=labref[0])
                    lab.grid_forget()
                    if found:
                        found.clear()
                    if labref[1][1] == 20:
                        self._comp_play_20()
                    self._check_comp_num()
                    self._p2_two()
                    self._p2_one()
                    self._p2_hold_on()
                    self._p2_suspension()
                    self.__checkcomp_played.insert(0, 1)
                    self.__check2_played.insert(0, 0)
                    self._checkmate()
            else:
                print("Computer please chill its not your turn to play....")
            pass

    def _comp_two(self):
        """Responsible for making the computer to pick two cards - PICK TWO"""
        if self._player2.player2up2[0] == 2:
            # self._root.after(400, self._comp_mark)
            # self.__checkcomp_played.insert(0, 0)
            # self.__check2_played.insert(0, 1)
            # self._root.after(400, self._comp_mark)
            for i in range(2):
                print('picking two')
                self._comp_mark()
                self.__checkcomp_played.insert(0, 0)
                self.__check2_played.insert(0, 1)
            self._player2.player2up2.insert(0, 0)
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)

    def _comp_one(self):
        """Responsible for making the computer to pick one card - GENERAL MARKET"""
        if self._player_turn('comp'):
            if self._player2.player2up14[0] == 14:
                print("Going to gen mart")
                self._comp_mark()
                self._player2.player2up14.insert(0, 0)
                self.__checkcomp_played.insert(0, 1)
                self.__check2_played.insert(0, 0)

    def _comp_hold_on(self):
        """Responsible for making the computer to hold on while player2 plays again or goes to mart"""
        if self._player2.player2up1[0] == 1:
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)
            self._player2.player2up1.insert(0, 0)

    def _comp_suspension(self):
        """Responsible for suspending the computer while player2 plays again or goes to mart"""
        if self._player2.player2up8[0] == 8:
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)
            self._player2.player2up8.insert(0, 0)

    def _comp_20(self):
        if self._player2.player2up20[0] == 20:
            self._CompPlay20()
            self._player2.player2up20.insert(0, 0)

    def _popup(self, event=None):
        event.destroy()
        for i in self._buts2:
            i.config(state='normal')
        self._mark_but.config(state='normal')

        self.__checkcomp_played.insert(0, 0)
        self.__check2_played.insert(0, 1)
        self._Comp_response_to_20()
        # return self._var.get()

    def Window(self, arg):
        if arg == 'whot':
            _toplev = tk.Toplevel(self._root)
            _toplev.transient(self._root)
            _toplev.title("Ask for a card")
            _toplev.grid()
            com = ttk.Combobox(_toplev, textvariable=self._var, values=self._values)
            self._var.set('choose a card')
            button = ttk.Button(_toplev, text='Ok', command=lambda: self._popup(_toplev))
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(state='disabled')
            com.grid()
            button.grid()
            _toplev.protocol('WM_DELETE_WINDOW', lambda: self._destroy(_toplev))

    def _destroy(self, root=None):
        for i in self._buts2:
            i.config(state='normal')
        self._mark_but.config(state='normal')
        root.destroy()

    def Manual(self, event=None):
        """See the Manual of the Game"""
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

    def _checkmate(self):
        """Freezes all the buttons and stops the computer or player2 from playing again
        if any one of the player's cards finishes"""
        if len(self._player2.cards()) == 0:
            self.__checkcomp_played.insert(0, 1)
            # self.__check2_played.insert(0,1)
            self.__check_checkmate = True
            tmb.showinfo("Checkmate", "You are the winner")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(state='disabled')
            self._root.title('Whot Game - Checkmate')

        elif len(self._computer.cards()) == 0:
            self.__check2_played.insert(0, 1)
            # self.__checkcomp_played.insert(0,1)
            self.__check_checkmate = True
            tmb.showinfo("Checkmate", "The Computer is the winner")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(state='disabled')
            self._root.title('Whot Game - Checkmate')

    def _mainloop(self):
        """calls tk mainloop"""
        self._root.mainloop()

    def _p2_mark(self, power=None, event=None):
        """Responsible for making player2 to go to market (pick a card from the mart)"""
        if self.__checkcomp_played[0] and not self.__check_checkmate:
            if power:
                if power == 2:
                    self._check2 += 1
                elif power == 1:
                    self._check1 += 1

            for i in self._but_refs:
                if not i:
                    g = self._but_refs.index(i)
                    self._player2.gomart()
                    self._but_refs[g].append(self._player2.cards()[len(self._player2.cards()) - 1])
                    for o in range(20):
                        if o == g:
                            new_but = self._p2_buts.get(o)
                            new_but.config(image=self._player2.cards()[len(self._player2.cards()) - 1][0],
                                           command=lambda: self._play2(self._but_refs[o], self._p2_buts[o]))
                            new_but.grid(row=0, column=g, padx=6, pady=6)
                            new_but.after(500, self.__CompPlayEngine)
                            break
                    break
            self._check_p2_num()
            self.__checkcomp_played.insert(0, 0)
            self.__check2_played.insert(0, 1)

    def _comp_mark(self):
        """Responsible for making the computer to go to market (pick a card from the mart)"""
        if self.__check2_played[0] and not self.__check_checkmate:
            for i in self._labs_refs:
                if not i:
                    g = self._labs_refs.index(i)
                    self._computer.gomart()
                    self._labs_refs[g].append(self._computer.cards()[len(self._computer.cards()) - 1])
                    for o in range(20):
                        if o == g:
                            new_lab = self._complab_ref.get(o)
                            new_lab.config(image=self._misc_whot1)
                            new_lab.grid(row=0, column=g, padx=6, pady=6)
                            break
                    break
            self._check_comp_num()
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)


if __name__ == '__main__':
    app = WhotGtk()
    app._mainloop()
