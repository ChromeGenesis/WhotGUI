#!/usr/bin/python3

from tkinter import ttk
import tkinter as tk
import tkinter.scrolledtext as tks
from manual import manual
from GameImages import images
from random import choice
import Main
import Pmw
import tkinter.messagebox as tmb
import os, sys


class WhotGtk(images):
    """Naija Whot Game in Grand Style"""
    def __init__(self):
        self._root = Pmw.initialise()
        #self._root.geometry('1367x685')
        self._root.geometry('790x685')
        self._root.title('Whot Game')
        super().__init__()
        read_name = None
        try:
            read_name = open('./name_config.gen', 'r').read()
            if not read_name == '':
                self._player2_frame = Pmw.ScrolledFrame(self._root, labelpos='s', usehullsize=1,
                                                hull_width=100,
                                                hull_height=225,
                                                label_text=read_name.upper())
        except Exception as e:
            print(e)
            self._player2_frame = Pmw.ScrolledFrame(self._root, labelpos='s', usehullsize=1,
                                                hull_width=100,
                                                hull_height=225,
                                                label_text='PLAYER =>')      

            
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
        
        ##################################################################
        # Check Pick two, General market and checkmate
        ##################################################################
        self.__check_checkmate = False

        self._check2 = 0
        self._check1 = 0
        ###################################################################
        # Player2 Butrefs
        ###################################################################
        self._but_refs = []
        for i in range(30):
            self._but_refs.append([])
        #####################################################################

        #####################################################################
        # Computer Labrefs
        #####################################################################
        self._labs_refs = []
        for i in range(30):
            self._labs_refs.append([])
        ####################################################################
            
        ####################################################################
        # Computer Engine's (CompPlayEngine) containers
        ####################################################################

        self._found_str = []
        self._found_num = []
        self._found_20 = []
        self._found_request = []
        
        ####################################################################
        # Request
        #####################################################################
        self._player2_request = None
        #####################################################################

        ######################################################################
        # Initialisation of Buttons and Labels
        ######################################################################
        self._labs_comp = []
        for i in range(30):
            self._labs_comp.append(tk.Label(self._comp_frame_int))

        self._buts2 = []
        for i in range(30):
            self._buts2.append(tk.Button(self._p2_frame_int))
        #######################################################################

        #############################################################################################################
        # Initialize and Display Player2 Buttons and Sync with their Button references (Butrefs)
        #############################################################################################################
        self._p2_buts = {}
        for i in range(30):
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
        # Display Played card and Mark card Image
        #####################################################################################
        self._played = tk.Label(self._played_cards_frame,
                                image=self._whot.PlayedCards()[len(self._whot.PlayedCards()) - 1][0])

        self._mark_but = tk.Button(self._root, image=self._misc_whot, command=self._p2_mark)

        #####################################################################################

        ####################################################################################
        # Initialize and Display Computer Labels and Sync with their Label references (Labrefs)
        ####################################################################################
        self._complab_ref = {}

        for i in range(30):
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
        
        game_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='Game', menu=game_menu)
        game_menu.add_command(label='Restart Game', accelerator='Ctrl+R', compound='left', command=self.__restart)
        game_menu.add_command(label='Change name', accelerator='Ctrl+N', compound='left', command=self._set_name)
        
        theme_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='Themes', menu=theme_menu)
        self._theme_var = tk.IntVar()
        
        self._theme_colors = ['yellow', 'blue', 'red', 'aquamarine', 'green', 'magenta', 'gold',
                              'dark violet', 'pink', 'black', 'none']
        #for i in self._theme_colors:
        #    theme_menu.add_radiobutton(command=lambda: self._themes(str(i)), label=str(i), var=self._theme_var, value=int(0+1))
        
        theme_menu.add_radiobutton(label='yellow', command=lambda: self._themes('yellow'), var=self._theme_var,
                                   value=1)
        theme_menu.add_radiobutton(label='blue', command=lambda: self._themes('blue'), var=self._theme_var,
                                   value=2)
        theme_menu.add_radiobutton(label='red', command=lambda: self._themes('red'), var=self._theme_var,
                                   value=3)
        theme_menu.add_radiobutton(label='aquamarine', command=lambda: self._themes('aquamarine'), var=self._theme_var,
                                   value=4)
        theme_menu.add_radiobutton(label='green', command=lambda: self._themes('green'), var=self._theme_var,
                                   value=5)        
        theme_menu.add_radiobutton(label='magenta', command=lambda: self._themes('magenta'), var=self._theme_var,
                                   value=6)
        theme_menu.add_radiobutton(label='gold', command=lambda: self._themes('gold'), var=self._theme_var,
                                   value=7)        
        theme_menu.add_radiobutton(label='dark violet', command=lambda: self._themes('dark violet'), var=self._theme_var,
                                   value=8)
        theme_menu.add_radiobutton(label='pink', command=lambda: self._themes('pink'), var=self._theme_var,
                                   value=9)
        theme_menu.add_radiobutton(label='black', command=lambda: self._themes('black'), var=self._theme_var,
                                   value=10)
        theme_menu.add_radiobutton(label='Default', command=lambda: self._themes('none'), var=self._theme_var,
                                   value=11)
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
        
        ################################################################################################################
        # Hover
        ################################################################################################################
        self._hover_comp = tk.Label(self._root, text="Number of computer cards: 5", font='Consolas 15 italic')
        self._hover_p2 = tk.Label(self._root, text="Number of your cards: 5", font='Consolas 15 italic')
        self._hover_p2.grid(row=4, column=0, sticky='w')
        self._hover_comp.grid(row=0, column=0)

        ##################################################################################
        # Binding's
        ##################################################################################
        self._root.bind_all("<Control-m>", self.Manual)
        self._root.bind_all("<Control-r>", self.__restart)
        self._root.bind_all("<Control-n>", self._set_name)
        self._root.bind_all("<Return>", self._p2_mark)
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
        _ball_mark.bind(self._mark_but, "Click To Go To Mart (Enter key does the exact same thing)")
        _ball_lab.bind(self._played, "Played Cards")
        #####################################################################################
        
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
        self._root.after(900, self.__CompPlayEngine)
        self._read_theme_conf()
        
    def _themes(self, color):
        """Change the theme of the game windows"""
        self._themes_dict = {'green':'green yellow', 'blue':'DeepSkyBlue2', 'aquamarine': 'Aquamarine', 'none':'SystemButtonFace',
                             'yellow':'yellow', 'magenta':'magenta', 'gold':'gold', 'red':'red', 'dark violet':'dark violet',
                             'pink':'pink', 'black':'black'}
        
        if color in self._themes_dict:
            for i in self._labs_comp:
                i.config(bg=self._themes_dict.get(color))
            for i in self._buts2:
                i.config(bg=self._themes_dict.get(color))
            self._played.config(bg=self._themes_dict.get(color))
            self._mark_but.config(bg=self._themes_dict.get(color))
            self._hover_comp.config(fg=self._themes_dict.get(color))
            self._hover_p2.config(fg=self._themes_dict.get(color))
            if color == 'none':
                self._hover_comp.config(fg='#000000')
                self._hover_p2.config(fg='#000000')
            self._write_to_theme_conf(color)
        else:
            self._write_to_theme_conf('none')
        
    def _write_to_theme_conf(self, theme):
        with open('./theme_config.gen', 'w+') as conf:
            conf.write(str(theme))
        return None
    
    def _read_theme_conf(self):
        try:
            with open('./theme_config.gen', 'r') as conf:
                theme = conf.read()
                for i in self._theme_colors:
                    if theme == i:
                        self._themes(theme)
                        self._theme_var.set(self._theme_colors.index(i)+1)
                
        except:
            pass
        return None
    
    def _set_name(self, event=None):
        top = tk.Toplevel(self._root)
        top.title("Set Name")
        ent_var = tk.StringVar()
        name_entry = tk.Entry(top, width=50, textvariable=ent_var)
        name_entry.pack()
        ok_button = ttk.Button(top, text='Ok', command=lambda: self._destroy(top, ent_var))
        ok_button.pack()
        tk.Label(top, text='Restart to initiate changes...').pack()
        name_entry.focus_set()
    
    def _clicked_card(self, card, event=None):
        event.destroy()
        for i in self._buts2:
            i.config(state='normal')
        self._mark_but.config(state='normal')
        self._player2_request = card
        self.__checkcomp_played.insert(0, 0)
        self.__check2_played.insert(0, 1)
        self._root.after(500, self._Comp_response_to_20)

    def _popup_window(self):
        _toplev = tk.Toplevel(self._root)
        _toplev.transient(self._root)
        _toplev.geometry('{}x{}+{}+{}'.format(230, 480, 400, 100)) 
        _toplev.title("Ask for a card")
        _toplev.resizable(False, False)
        try:
            file = open('./theme_config.gen', 'r')
            theme = file.read()
            if theme == 'none':
                theme_but = 'SystemButtonFace'
                theme_lab = 'SystemButtonText'
            else:
                theme_but = theme
                theme_lab = theme
        except:
            pass
        cross_bt = tk.Button(_toplev, image=self._cross_icon)
        cross_bt.config(command=lambda: self._clicked_card('cross', _toplev), bg=theme_but)
        cross_bt.grid(row=0, column=0, pady=3)

        circle_bt = tk.Button(_toplev, image=self._circle_icon)
        circle_bt.config(command=lambda: self._clicked_card('circle', _toplev), bg=theme_but)
        circle_bt.grid(row=1, column=0, pady=3)

        star_bt = tk.Button(_toplev, image=self._star_icon)
        star_bt.config(command=lambda: self._clicked_card('star', _toplev), bg=theme_but)
        star_bt.grid(row=2, column=0, pady=3)

        triangle_bt = tk.Button(_toplev, image=self._triangle_icon)
        triangle_bt.config(command=lambda: self._clicked_card('triangle', _toplev), bg=theme_but)
        triangle_bt.grid(row=3, column=0, pady=3)

        square_bt = tk.Button(_toplev, image=self._square_icon)
        square_bt.config(command=lambda: self._clicked_card('square', _toplev), bg=theme_but)
        square_bt.grid(row=4, column=0, pady=3)

        tk.Label(_toplev, text='cross', fg=theme_lab).grid(row=0, column=1,)
        tk.Label(_toplev, text='circle', fg=theme_lab).grid(row=1, column=1,)
        tk.Label(_toplev, text='star', fg=theme_lab).grid(row=2, column=1,)
        tk.Label(_toplev, text='triangle', fg=theme_lab).grid(row=3, column=1,)
        tk.Label(_toplev, text='square', fg=theme_lab).grid(row=4, column=1,)
        
        lab = tk.Label(_toplev, text='click your desired button\n to choose a card'.upper(), fg=theme_lab)
        lab.grid(row=5, column=1, sticky='e')
        for i in self._buts2:
            i.config(state='disabled')
        self._mark_but.config(state='disabled')
        _toplev.protocol('WM_DELETE_WINDOW', lambda: self._destroy(_toplev))
        _toplev.focus_set()
        file.close()

    def _destroy(self, root=None, name=None):
        if name and name.get() != '':
            with open('./name_config.gen', 'w+') as f:
                f.write(name.get())
        for i in self._buts2:
            i.config(state='normal')
        self._mark_but.config(state='normal')
        root.destroy()
    
    def _player_turn(self, player):
        """Return bool value for the valid player to play first or next"""
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
        """check number of cards left/remaining for the computer and update"""
        if len(self._computer.cards()) == 1:
            self._hover_comp.config(text="Last Card.....")
        else:
            self._hover_comp.config(text="Number of computer cards :" + str(len(self._computer.cards())))
        return None

    def _check_p2_num(self, event=None):
        """check number of cards left/remaining for player2 and update"""
        if len(self._player2.cards()) == 1:
            self._hover_p2.config(text="Last Card.....")
        else:
            self._hover_p2.config(text="Number of your cards :" + str(len(self._player2.cards())))
        return None

    def _play2(self, butref=None, but=None, event=None):
        """For player2 (actual player) to play his or her valid card"""
        if butref and but:
            if self._player_turn('p2') and not self.__check_checkmate:
                try:
                    if self._player2.play(butref[0]):
                        self.__checkcomp_played.insert(0, 0)
                        self.__check2_played.insert(0, 1)

                        if butref[0][1][1] == 20:
                            self.__checkcomp_played.insert(0, 1)
                            self.__check2_played.insert(0, 0)
                            if not len(self._player2.cards()) == 0:
                                self._popup_window()

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
                        self._root.title('Whot Game')
                except Main.WhotException as e:
                    tmb.showwarning(title="INVALID MOVE", message=str(e).upper())
            else:
                tmb.showinfo("Not Your Turn", "Its not your turn to play")

    def _p2_two(self):
        """makes player2 to pick two cards mandatorily if computer gives him/her any card with
        the number '2' in it"""
        if self._computer.comp_powerup_2[0] == 2:
            tmb.showinfo("Pick Two", "PICK TWO CARDS FROM THE MART")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(command=self._check_p2)
            self._root.unbind_all("<Return>")
            self._root.bind_all("<Return>", self._check_p2)
            self._computer.comp_powerup_2.insert(0, 0)

    def _p2_one(self):
        """makes player2 to go to general market (which is to pick one card only from the mart) mandatorily
        if and when the computer gives him/her any card with the number '14' in it"""
        if self._computer.comp_powerup_14[0] == 14:
            tmb.showinfo("General Market", "GO TO MART ONCE")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(command=self._check_p1)
            self._root.unbind_all("<Return>")
            self._root.bind_all("<Return>", self._check_p1)
            self._computer.comp_powerup_14.insert(0, 0)

    def _p2_hold_on(self):
        """makes player2 to hold on until the computer plays another card or goes to the mart mandatorily
        if the computer gives him/her any card with the number '1' in it"""
        if self._computer.comp_powerup_1[0] == 1:
            tmb.showinfo("Hold On", "HOLD ON......")
            self.__checkcomp_played.insert(0, 0)
            self.__check2_played.insert(0, 1)
            self._computer.comp_powerup_1.insert(0, 0)
            self._checkmate()
            self.__CompPlayEngine()

    def _p2_suspension(self):
        """Just like hold on, it suspends player2 until the computer plays another card or goes to mart"""
        if self._computer.comp_powerup_8[0] == 8:
            tmb.showinfo("Hold On", "SUSPENSION")
            self.__checkcomp_played.insert(0, 0)
            self.__check2_played.insert(0, 1)
            self._computer.comp_powerup_8.insert(0, 0)
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
            for i in self._buts2:
                i.config(state='normal')
            self._check2 = 0
            self._mark_but.config(command=self._p2_mark)
            self._root.bind_all("<Return>", self._p2_mark)

    def _check_p1(self, event=None):
        """Checks whether player2 clicked the mart button once (in other words, checks whether player2 has
        picked one card) and then unfreezes player2 cards (buttons) - for GENERAL MARKET"""
        self._p2_mark(1)
        if self._check1 == 1:
            self.__check2_played.insert(0, 1)
            self.__checkcomp_played.insert(0, 0)
            for i in self._buts2:
                i.config(state='normal')
            self._check1 = 0
            self._mark_but.config(command=self._p2_mark)
            self._root.bind_all("<Return>", self._p2_mark)

    def __CompPlayEngine(self, event=None):
        """Engine for determining and getting what valid cards the computer has and can play....
        if after all and no valid card is found, the computer goes to market"""
        if self._player_turn('comp') and not self.__check_checkmate:
            try:
                for i in enumerate(self._labs_refs):
                    if not i[1]:
                        pass
                    else:
                        if self._player2.check_requested:
                            if i[1][0][1][0] == self._player2.request:
                                self._found_request.append([i[0], i[1]])
                                self._labs_refs.insert(self._labs_refs.index(i[1]), [])
                                self._labs_refs.pop(self._labs_refs.index(i[1]))
                                break
                                    
                        elif i[1][0][1][1] == 20:
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

                        if not self._found_num and not self._found_20:
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
                    pass

            elif self._found_str:
                try:
                    for i in self._found_str:
                        if i[1][0][1][0] == self._whot.PlayedCards()[len(self._whot.PlayedCards()) - 1][1][0]:
                            self._play_comp(i[1][0], self._get_pos(i[0]), self._found_str)
                            break
                except IndexError as e:
                    pass
                
            elif self._found_request:
                for i in self._found_request:
                    self._play_comp(i[1][0], self._get_pos(i[0]), self._found_request)
                    break
            else:
                self._comp_mark()
        else:
            print("It's not your turn to play")

    def _get_pos(self, element):
        """gets the position of the computer label in the self._complab_ref dict"""
        for i in range(30):
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
            print('found_1 =', found_1, 'found_2 = ', found_2, 'found_8 = ', found_8,
                  'found_14 = ', found_14)
            self._player2.check_requested = True

        if found_1:
            tmb.showinfo("Request", "I NEED " + found_1[0].upper())
            self._player2.request = found_1[0]
            self._root.title('Whot Game - Request '+found_1[0].upper())

        elif found_2:
            tmb.showinfo("Request", "I NEED " + found_2[0].upper())
            self._player2.request = found_2[0]
            self._root.title('Whot Game - Request '+found_2[0].upper())

        elif found_8:
            tmb.showinfo("Request", "I NEED " + found_8[0].upper())
            self._player2.request = found_8[0]
            self._root.title('Whot Game - Request '+found_8[0].upper())

        elif found_14:
            tmb.showinfo("Request", "I NEED " + found_14[0].upper())
            self._player2.request = found_14[0]
            self._root.title('Whot Game - Request '+found_14[0].upper())
            
        else:
            tmb.showinfo("Request", "I NEED " + found_none[0].upper())
            self._player2.request = found_none[0]
            self._root.title('Whot Game - Request '+found_none[0].upper())

    def _Comp_response_to_20(self):
        card = self._player2_request
        if self._player_turn('comp') and not self.__check_checkmate:
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
                    if labref[1][0] == self._player2.request:
                        self._player2.check_requested = None
                        self._player2.request = None   
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
        if self._player2.p2_powerup_2[0] == 2:
            #self.__checkcomp_played.insert(0, 0)
            #self.__check2_played.insert(0, 1)
            #print("pickin 2")
            #self._comp_mark()
            #self.__checkcomp_played.insert(0, 0)
            #self.__check2_played.insert(0, 1)
            #self._comp_mark()
            #self._root.after(100, self._comp_mark)
            #self.__checkcomp_played.insert(0, 0)
            #self.__check2_played.insert(0, 1)
            #self._root.after(100, self._comp_mark)
            for i in range(2):
                print('picking two '+str(i))
                self._comp_mark()
                self.__checkcomp_played.insert(0, 0)
                self.__check2_played.insert(0, 1)
            self._player2.p2_powerup_2.insert(0, 0)
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)

    def _comp_one(self):
        """Responsible for making the computer to pick one card - GENERAL MARKET"""
        if self._player_turn('comp'):
            if self._player2.p2_powerup_14[0] == 14:
                print("Going to gen mart")
                self._comp_mark()
                self._player2.p2_powerup_14.insert(0, 0)
                self.__checkcomp_played.insert(0, 1)
                self.__check2_played.insert(0, 0)

    def _comp_hold_on(self):
        """Responsible for making the computer to hold on while player2 plays again or goes to mart"""
        if self._player2.p2_powerup_1[0] == 1:
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)
            self._player2.p2_powerup_1.insert(0, 0)

    def _comp_suspension(self):
        """Responsible for suspending the computer while player2 plays again or goes to mart"""
        if self._player2.p2_powerup_8[0] == 8:
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)
            self._player2.p2_powerup_8.insert(0, 0)

    def _comp_20(self):
        if self._player2.p2_powerup_20[0] == 20:
            self._CompPlay20()
            self._player2.p2_powerup_20.insert(0, 0)

    def Manual(self, event=None):
        """See the Manual of the Game"""
        if self._root:
            text = tk.Toplevel(self._root)
        else:
            text = tk.Toplevel(tk.Tk())
        text.title("<Manual>")
        text.transient(self._root)
        text.resizable(False, False)
        text_lab = tks.ScrolledText(text, wrap='word')
        text_lab.grid(row=0, column=0, sticky=tk.NSEW)
        text_lab.insert(1.0, manual)
        text.grid_rowconfigure(1, weight=1)
        text.grid_columnconfigure(0, weight=1)
        text_lab.configure(state='disabled')
        ttk.Button(text, text="Ok", command=lambda: self._destroy(text)).grid()

    def _checkmate(self):
        """Freezes all the buttons and stops the computer or player2 from playing again
        if any one of the players cards finishes"""
        if len(self._player2.cards()) == 0:
            self.__checkcomp_played.insert(0, 1)
            self.__check_checkmate = True
            self._root.unbind_all("<Return>")
            tmb.showinfo("Checkmate", "You are the winner")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(state='disabled')
            self._root.title('Whot Game - Checkmate')
            #if self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][1] == 20:
            #    self._checkmate()
            self.__restart()

        elif len(self._computer.cards()) == 0:
            self.__check2_played.insert(0, 1)
            self.__check_checkmate = True
            self._root.unbind_all("<Return>")
            tmb.showinfo("Checkmate", "The Computer is the winner")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(state='disabled')
            self._root.title('Whot Game - Checkmate')
            #if self._whot.PlayedCards()[len(self._whot.PlayedCards())-1][1][1] == 20:
            #    self._checkmate()
            self.__restart()
            
    def __restart(self, event=None):
        ask = tmb.askyesnocancel("Restart Game", "Do you want to restart the game?")
        if ask:
            if sys.platform == 'linux':
                os.execv(sys.executable, ['python3'] + sys.argv)
            elif sys.platform == 'win32':
                os.execv(sys.executable, ['python'] + sys.argv)
        elif ask is None:
            pass
        else:
            exit()

    def _mainloop(self):
        """calls tk mainloop"""
        self._root.mainloop()

    def _p2_mark(self, power=None, event=None):
        """Responsible for making player2 to go to market (pick a card from the mart)"""
        if self._player_turn('p2') and not self.__check_checkmate:
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
                    for o in range(30):
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
            self._root.title('Whot Game')

    def _comp_mark(self):
        """Responsible for making the computer to go to market (pick a card from the mart)"""
        if self._player_turn('comp') and not self.__check_checkmate:
            for i in self._labs_refs:
                if not i:
                    empty_container = self._labs_refs.index(i)
                    self._computer.gomart()
                    self._labs_refs[empty_container].append(self._computer.cards()[len(self._computer.cards()) - 1])
                    for o in range(30):
                        if o == empty_container:
                            new_lab = self._complab_ref.get(o)
                            new_lab.config(image=self._misc_whot1)
                            new_lab.grid(row=0, column=empty_container, padx=6, pady=6)
                            break
                    break
            self._check_comp_num()
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)
            self._root.title('Whot Game')


if __name__ == '__main__':
    app = WhotGtk()
    app._mainloop()