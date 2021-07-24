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
import pickle
from functools import partial


class WhotGtk(images):
    """Naija Whot Game in Grand Style"""
    def __init__(self):
        self._root = Pmw.initialise()
        self._orig_size = '790x685'
        self._root.geometry(self._orig_size)
        self._root.title('Whot Game')
        super().__init__()
        
        #####################################################################################
        # Open Config File
        #####################################################################################
        try:
            with open('./config.pkl', 'rb') as config_file:
                self._config_file = pickle.load(config_file)
                print('config file :', self._config_file)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            self._file_not_found = True
            self._create_new_config_file()
            print("file wasn't found........")
        else:
            self._file_not_found = False
        #####################################################################################
                #+
        read_name = self._config_file.get('name')
                #+
        self._player2_frame = Pmw.ScrolledFrame(self._root, labelpos='s', usehullsize=1,
                                                hull_width=100,
                                                hull_height=225,
                                                label_text=read_name.upper())
        
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
        #self._but1.grid(row=0, column=1005, padx=6, pady=6)
        self._but_refs[0].append(self._player2.cards()[0])

        self._but2 = self._p2_buts[1]
        self._but2.config(image=self._player2.cards()[1][0], command=lambda: self._play2(self._but_refs[1], self._but2))
        #self._but2.grid(row=0, column=1004, padx=6, pady=6)
        self._but_refs[1].append(self._player2.cards()[1])

        self._but3 = self._p2_buts[2]
        self._but3.config(image=self._player2.cards()[2][0], command=lambda: self._play2(self._but_refs[2], self._but3))
        #self._but3.grid(row=0, column=1003, padx=6, pady=6)
        self._but_refs[2].append(self._player2.cards()[2])

        self._but4 = self._p2_buts[3]
        self._but4.config(image=self._player2.cards()[3][0], command=lambda: self._play2(self._but_refs[3], self._but4))
        #self._but4.grid(row=0, column=1002, padx=6, pady=6)
        self._but_refs[3].append(self._player2.cards()[3])

        self._but5 = self._p2_buts[4]
        self._but5.config(image=self._player2.cards()[4][0], command=lambda: self._play2(self._but_refs[4], self._but5))
        #self._but5.grid(row=0, column=1001, padx=6, pady=6)
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
        #    self._complab_ref[i].grid(row=0, column=i, padx=6, pady=6)
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
        #game_menu.add_command(label='Change name', accelerator='Ctrl+N', compound='left', command=self._get_name)
        
        settings_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='Setting', menu=settings_menu)
        settings_menu.add_command(label='Settings', accelerator='Ctrl+S', compound='left', command=self._settings)
        
        ##############################################################################################################
        # Theme Init
        ##############################################################################################################
        self._theme_var = tk.IntVar()
        
        self._theme_colors = ['yellow', 'blue1', 'blue2', 'red', 'aquamarine', 'green1', 'green2', 'magenta', 'gold',
                              'dark violet', 'pink', 'black', 'Default']
        if self._file_not_found:
            for o, i in enumerate(self._theme_colors):
                if i == "Default":
                    self._theme_var.set(o)
        
        self._mode_var = tk.StringVar()
        
        self._root.config(menu=menu_bar)
        ####################################################################################
        # Grids
        ####################################################################################
        self._player2_frame.grid(row=3, columnspan=4, sticky='we')
        self._comp_frame.grid(row=1, columnspan=4, sticky='we')
        self._played_cards_frame.grid(row=2, column=2)
        #*
        #self._played.grid(row=1, column=1, sticky='e', )
        #
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
        
        #################################################################################################################
        # Turn Indicators
        #################################################################################################################
        self._p2_turn_indicator = tk.Label(self._root, text='player', font='Consolas 15 italic')
        self._comp_turn_indicator = tk.Label(self._root, text='computer', font='Consolas 15 italic')
        
        self._p2_turn_indicator.grid(row=4, column=2, sticky='e')
        self._comp_turn_indicator.grid(row=0, column=2, sticky='e')

        ##################################################################################
        # Binding's
        ##################################################################################
        self._root.bind_all("<Control-m>", self.Manual)
        self._root.bind_all("<Control-r>", self.__restart)
        self._root.bind("<Control-s>", self._settings)
        self._root.bind("<Return>", self._p2_mark)
        self._root.bind_all("<F11>", self._toggle_on_fullscreen)
        self._root.bind_all("<Escape>", self._toggle_off_fullscreen)
        #self._root.bind_all("<Control-t>", self._choose_theme)
        self.__full_size = self._root.maxsize()
        ####################################################################################
        # Balloon Bindings and Inits
        ####################################################################################
        _ball_mark = Pmw.Balloon(self._root)
        _ball_lab = Pmw.Balloon(self._played_cards_frame)
        _ball_p2 = Pmw.Balloon(self._p2_frame_int)
        _ball_comp = Pmw.Balloon(self._comp_frame_int)
        for i in self._buts2:
            _ball_p2.bind(i, self._config_file.get('name')+"('s)"+' Cards')
        for i in self._labs_comp:
            _ball_comp.bind(i, "Computer's Cards")
        _ball_mark.bind(self._mark_but, "Click To Go To Mart (Enter key does the same thing)")
        _ball_lab.bind(self._played, "Played Cards")
        #####################################################################################
        
        ####################################################################################
        # Who Plays First and Turn Indicator
        ####################################################################################
        who_plays_first = ('player2', 'computer')
        final_choice = (choice(who_plays_first))
        if final_choice == 'player2':
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)
            self._update_turn_indicator()
        else:
            self.__checkcomp_played.insert(0, 0)
            self.__check2_played.insert(0, 1)
            self._update_turn_indicator()
        print("choice is :" +str(final_choice))
        pass
        ####################################################################################
        # Grid Counter, Game Started and Show Setting At Startup Variables
        ####################################################################################
        self._p2_btn_grid_pos = 1000
        self._comp_lab_grid_pos = 1000
        self._game_started = False
        self._show_setting_at_startup = tk.BooleanVar()
        ####################################################################################
        # Update n Run
        ####################################################################################
        if self._config_file.get('show_setting'):
            self._settings()
        self._mode_var.set(self._config_file.get('mode'))
        
        self._root.after(5800, self.__CompPlayEngine)
        self._root.after(1200, self._arrange_cards)
        self._get_theme_conf()
        ####################################################################################
        # END
        ####################################################################################
        #self._root.overrideredirect(True)
        #self._toggle_on_fullscreen()
        self._popup_message("Loading...", "Loading Cards...", 4500)
        
    def _arrange_cards(self):
        cards = [self._but1, self._but2, self._but3, self._but4, self._but5]
        
        
        #for o, i in enumerate(cards):
        #    print('in card....'+str(i)+'.....'+str(self._p2_btn_grid_pos))
        #    self._root.after(50+500, lambda: i.grid(row=0, column=o, padx=6, pady=6))
        #    i.grid(row=0, column=, padx=6, pady=6)
        #    self._p2_btn_grid_pos -= 1
        self._root.after(50, lambda: self._but1.grid(row=0, column=1005, padx=6, pady=6))
        self._root.after(450, lambda: self._but2.grid(row=0, column=1004, padx=6, pady=6))
        self._root.after(650, lambda: self._but3.grid(row=0, column=1003, padx=6, pady=6))
        self._root.after(850, lambda: self._but4.grid(row=0, column=1002, padx=6, pady=6))
        self._root.after(1050, lambda: self._but5.grid(row=0, column=1001, padx=6, pady=6))
        
        self._root.after(1500, lambda: self._played.grid(row=1, column=1, sticky='e'))
        
        self._root.after(2000, lambda: self._complab_ref[0].grid(row=0, column=1005, padx=6, pady=6))
        self._root.after(2400, lambda: self._complab_ref[1].grid(row=0, column=1004, padx=6, pady=6))
        self._root.after(2600, lambda: self._complab_ref[2].grid(row=0, column=1003, padx=6, pady=6))
        self._root.after(2800, lambda: self._complab_ref[3].grid(row=0, column=1002, padx=6, pady=6))
        self._root.after(3000, lambda: self._complab_ref[4].grid(row=0, column=1001, padx=6, pady=6))
        
        #for i in range(5):
        #    self._root.after(2000, lambda: self._complab_ref[i].grid(row=0, column=self._comp_lab_grid_pos, padx=6, pady=6))
        #    self._comp_lab_grid_pos -=1
        pass
    
            
    def _create_new_config_file(self):
        """Creates a new config file if and when the original one has been deleted/Truncated"""
        if self._file_not_found:
            config_data = {'name': 'Chrome', 'theme': 'Default', 'mode': 'easy', 'show_setting' :True}
            with open('./config.pkl', 'wb+') as config_file:
                pickle.dump(config_data, config_file)
            try:
                with open('./config.pkl', 'rb') as config_file:
                    self._config_file = pickle.load(config_file)
                    print("New File Generated...............")
            except IOError as e:
                tmb.showerror("Input/Error", e)

    
    #def _write_config(self, data_type, data):
    #    """Write to the config file and load data from it"""
    #    with open('./config.pkl', 'rb') as config_file:
    #        config_dict = pickle.load(config_file)
    #        config_dict[data_type] = data
    #    with open('./config.pkl', 'wb') as config_file:
    #        pickle.dump(config_dict, config_file)
    #    with open('./config.pkl', 'rb') as config_file:
    #        self._config_file = pickle.load(config_file)
    #    print('New config file is: ', self._config_file)


    def _write_config(self, data_type, data):
        """Write to the config file and load data from it"""
        with open('./config.pkl', 'rb') as config_file:
            config_dict = pickle.load(config_file)
            config_dict[data_type] = data
        try:
            with open('./config.pkl', 'wb') as config_file:
                pickle.dump(config_dict, config_file)
        except IOError as e:
            tmb.showerror("Input/Output Error", e)
            print(e)
        with open('./config.pkl', 'rb') as config_file:
            self._config_file = pickle.load(config_file)
        print('New config file is: ', self._config_file)
        
    def _settings(self, event=None):
        """Settings for whot game"""
        top = tk.Toplevel(self._root)
        top.transient(self._root)
        top.title('Whot Game - Settings')
        
        w, h = int(self._root.winfo_screenwidth() / 6), int(self._root.winfo_screenheight() / 4)
        #if event:
        #    x, y = event.x, event.y
        #else:
        x, y = self._root.winfo_x(), self._root.winfo_y()
        top.geometry('{}x{}+{}+{}'.format(350, 420, x+w, y+h))
        #top.geometry('{}x{}+{}+{}'.format(350, 400, 300, 80))
        top.resizable(False, False)
            
        root_tab = ttk.Notebook(top)
            
        theme_tab = ttk.Frame(root_tab)
        name_tab = ttk.Frame(root_tab)
        mode_tab = ttk.Frame(root_tab)
            
        root_tab.add(theme_tab, text='Themes')
        root_tab.add(name_tab, text='Name')
        root_tab.add(mode_tab, text='Mode')
        
        #root_tab.config(bg='black')
            
        #root_tab.pack(expand=1, fill='both')
        root_tab.grid(row=0, column=0, sticky='nsew')
            
        self._choose_theme(theme_tab)
        self._get_name(name_tab)
        self._choose_mode(mode_tab)
        
        show_setting = ttk.Checkbutton(top, text='Show Setttings at startup', variable=self._show_setting_at_startup,
                                       command=lambda: self._write_config('show_setting',
                                                                          self._show_setting_at_startup.get()))
        self._show_setting_at_startup.set(self._config_file.get('show_setting'))
        show_setting.grid(row=6, column=0, sticky='w')
        ttk.Button(top, text='Ok', command=lambda: self._check_game_started(top)).grid(row=7, column=0, sticky='e')
            
        top.focus_set()
        top.protocol('WM_DELETE_WINDOW', lambda: self._check_game_started(top))
        top.grab_set()
        pass
    
    def _check_game_started(self, window):
        self._game_started = True
        window.grab_release()
        window.destroy()
    
    def _choose_mode(self, window):
        """To choose the mode of the game, whether easy or hard"""
        
        hard_radbtn = tk.Radiobutton(window, text='Hard', var=self._mode_var, value='hard',
                                command=lambda: self._write_config('mode', self._mode_var.get()))
            
        medium_radbtn = tk.Radiobutton(window, text='Medium', var=self._mode_var, value='medium',
                                    command=lambda: self._write_config('mode', self._mode_var.get()))
            
        easy_radbtn = tk.Radiobutton(window, text='Easy', var=self._mode_var, value='easy',
                                  command=lambda: self._write_config('mode', self._mode_var.get()))
        
        hard_radbtn.grid(row=1, column=0, sticky='w')
        medium_radbtn.grid(row=2, column=0, sticky='w')
        easy_radbtn.grid(row=3, column=0, sticky='w')
        tk.Label(window, text='Choose Desired Mode').grid(row=0, column=0)
        tk.Label(window, text="Can only be set once during a particular game session").grid(
            row=4, column=0, sticky='s')
        window.focus_set()
        
        if self._game_started:
            for i in [hard_radbtn, medium_radbtn, easy_radbtn]:
                i.config(state='disabled')  
        
    def _choose_theme(self, window):
        """For choosing desired theme from the themes list"""        
        theme_radbtns = []
        radbtns_dict = {}
        for o, i in enumerate(self._theme_colors):
            theme_radbtns.append(tk.Radiobutton(window, text=str(i).upper(), var=self._theme_var,
                                            value=o, command=self._parse_theme))
            
        for i in range(len(self._theme_colors)):
            radbtns_dict[i] = theme_radbtns[i]
            
        for i in range(len(self._theme_colors)):
            radbtns_dict[i].grid(row=1+i, column=0, sticky='w')
        tk.Label(window, text="Choose Your Desired Theme").grid(row=0, column=0, sticky='e')
        window.bind("<Down>", partial(self._scroll_theme, 'down'))
        window.bind("<Up>", partial(self._scroll_theme, 'up'))
        window.focus_set()
        
    def _scroll_theme(self, action, event=None):
        value = self._theme_var.get()
        if value <= len(self._theme_colors)-2 and action == 'down':
            self._theme_var.set(value+1)
            self._parse_theme()
            
        if not value <= 0 and action == 'up':
            self._theme_var.set(value-1)
            self._parse_theme()
        pass
    
    def _parse_theme(self):
        """To retreive (Parse) the chosen theme from the IntVar (self._theme_var) and pass it to the themes method"""
        for o, i in enumerate(self._theme_colors):
            if o == self._theme_var.get():
                self._set_theme(str(i))
                break
            
    def _get_theme_conf(self):
        """Gets the theme configuration and updates the theme var"""
        theme = self._config_file.get('theme')
        for o, i in enumerate(self._theme_colors):
            if theme == i:
                self._set_theme(theme)
                self._theme_var.set(o)
        return None
        
    def _set_theme(self, color):
        """Set theme for the game windows"""
        self._themes_dict = {'green1':'green yellow', 'green2':'#000fff000', 'blue1':'royal blue', 'blue2':'dodger blue',
                             'aquamarine': 'Aquamarine', 'Default':'#d9d9d9',
                             'yellow':'yellow', 'magenta':'magenta', 'gold':'gold', 'red':'red', 'dark violet':'dark violet',
                             'pink':'pink', 'black':'black'}
        
        if color in self._themes_dict:
            try:
                for i in self._labs_comp:
                    i.config(bg=self._themes_dict.get(color))
                for i in self._buts2:
                    i.config(bg=self._themes_dict.get(color))
                self._played.config(bg=self._themes_dict.get(color))
                self._mark_but.config(bg=self._themes_dict.get(color))
                self._hover_comp.config(fg=self._themes_dict.get(color))
                self._hover_p2.config(fg=self._themes_dict.get(color))
                if color == 'Default':
                    self._hover_comp.config(fg='#000000')
                    self._hover_p2.config(fg='#000000')
                self._write_config('theme', color)
                
            except tk.TclError as e:
                print(e)
        else:
            self._write_config('theme', 'Default')

    def _popup_message(self, title, text, time=None):
        """Displays popup message for 1 sec approx containing instruction on what to after
            a powerup has been played by the opponent"""
        top = tk.Toplevel(self._root)
        top.grab_set()
        top.focus_set()
        top.transient(self._root)
        top.title(title.upper())
        
        theme = self._config_file.get('theme')
        if theme == 'Default':
            theme = '#000000'
            
        tk.Label(top, text=text, fg=theme, font='Consolas 13 italic',
                 padx=20, pady=20).pack()
        w, h = int(self._root.winfo_screenwidth() / 6), int(self._root.winfo_screenheight() / 4)
        x, y = self._root.winfo_x(), self._root.winfo_y()
        top.geometry('{}x{}+{}+{}'.format(250, 50, x+w, y+h))
        #top.geometry('{}x{}+{}+{}'.format(250, 50, 500, 300))
        if not time:
            top.after(900, top.destroy)
        else:
            top.after(time, top.destroy)
    
    def _get_name(self, window):
        """Gets desired name from player"""
        ent_var = tk.StringVar()
        tk.Label(window, text='Enter Your Desired Name Here').pack()
        name_entry = tk.Entry(window, width=50, textvariable=ent_var)
        name_entry.pack()
        ok_button = ttk.Button(window, text='Ok', command=partial(self._set_name, ent_var, window))
        ok_button.pack()
        tk.Label(window, text='Restart to initiate changes...').pack()
        name_entry.bind("<Return>", partial(self._set_name, ent_var, window))
        try:
            former_name = self._config_file.get('name')
            ent_var.set(former_name)
        except:
            pass
        name_entry.focus_set()
            
    def _set_name(self, name, window=None, event=None):
        """Sets (Registers) the desired name to the configuration file"""
        if name and name.get() != '':
            self._write_config('name', name.get())
            if window:
                saved = tk.Label(window, text=name.get()+' has been saved successfully...')
                saved.pack()
                saved.after(400, saved.pack_forget)

    def _clicked_card(self, card, window):
        """Registers player2's Desired card and calls player1 (computer) to respond to the request"""
        if window:
            window.destroy()
            for i in self._buts2:
                i.config(state='normal')
            self._mark_but.config(state='normal')
        if card:
            self._player2_request = card
            self.__checkcomp_played.insert(0, 0)
            self.__check2_played.insert(0, 1)
            self._root.after(500, self._Comp_response_to_20)
        window.grab_release()
        #self._root.bind("<Return>", self._p2_mark)

    def _p2_ask_for_a_card(self):
        """Player2 (actual player) demands a particular card from computer after playing whot 20"""
        _toplev = tk.Toplevel(self._root)
        _toplev.transient(self._root)
        x, y = self._root.winfo_x(), self._root.winfo_y()
        _toplev.geometry('{}x{}+{}+{}'.format(230, 480, x, y))
        #_toplev.geometry('{}x{}+{}+{}'.format(230, 480, 400, 100)) 
        _toplev.title("Ask for a card")
        _toplev.resizable(False, False)

        theme = self._config_file.get('theme')

        if theme == 'Default':
            if not sys.platform == 'linux':
                theme_but = 'SystemButtonFace'
                theme_lab = 'SystemButtonText'
            else:
                theme_but = '#d9d9d9'
                theme_lab = '#d9d9d9'
        else:
            theme_but = theme
            theme_lab = theme

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
        
        _toplev.protocol('WM_DELETE_WINDOW', lambda: self._clicked_card(None, _toplev))
        _toplev.focus_set()
        _toplev.grab_set()
    
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
                
    def _update_turn_indicator(self):
        if self._player_turn('p2') and not self._player_turn('comp'):
            self._p2_turn_indicator.config(fg='#000fff000')
            self._comp_turn_indicator.config(fg='red')
            
        elif self._player_turn('comp') and not self._player_turn('p2'):
            self._p2_turn_indicator.config(fg='red')
            self._comp_turn_indicator.config(fg='#000fff000')

    def _display_comp_no_of_cards(self, event=None):
        """check number of cards left/remaining for the computer, update and display"""
        if len(self._computer.cards()) == 1:
            self._hover_comp.config(text="Last Card.....")
        else:
            self._hover_comp.config(text="Number of computer cards :" + str(len(self._computer.cards())))
        return None

    def _display_p2_no_of_cards(self, event=None):
        """check number of cards left/remaining for player2, update and display"""
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
                                self._p2_ask_for_a_card()

                        self._played.configure(image=butref[0][0])
                        but.after(500, self.__CompPlayEngine)
                        but.grid_forget()
                        butref.clear()
                        self._display_p2_no_of_cards()
                        self._comp_hold_on()
                        self._comp_pick_two()
                        self._comp_go_gen_mart()
                        self._comp_suspension()
                        #*
                        self._update_turn_indicator()
                        #*
                        self._checkmate()
                        #self._root.title('Whot Game')
                except Main.WhotException as e:
                    tmb.showwarning(title="INVALID MOVE", message=str(e).upper())
            else:
                tmb.showinfo("Not Your Turn", "Its not your turn to play")

    def _p2_pick_two(self):
        """makes player2 to pick two cards mandatorily if computer gives him/her any card with
        the number '2' in it"""
        if self._computer.comp_powerup_2[0] == 2:
            #tmb.showinfo("Pick Two", "PICK TWO CARDS FROM THE MART")
            self._popup_message("pick two", "pick two cards from the mart")
            self._root.title("Whot Game - PICK TWO")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(command=self._check_p2)
            self._root.unbind("<Return>")
            self._root.bind("<Return>", self._check_p2)
            self._computer.comp_powerup_2.insert(0, 0)

    def _p2_go_gen_mart(self):
        """makes player2 to go to general market (which is to pick one card only from the mart) mandatorily
        if and when the computer gives him/her any card with the number '14' in it"""
        if self._computer.comp_powerup_14[0] == 14:
            #tmb.showinfo("General Market", "GO TO MART ONCE")
            self._popup_message("general market", "Go to mart once")
            self._root.title("Whot Game - GENERAL MARKET")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(command=self._check_p1)
            self._root.unbind("<Return>")
            self._root.bind("<Return>", self._check_p1)
            self._computer.comp_powerup_14.insert(0, 0)

    def _p2_hold_on(self):
        """makes player2 to hold on until the computer plays another card or goes to the mart mandatorily
        if the computer gives him/her any card with the number '1' in it"""
        if self._computer.comp_powerup_1[0] == 1:
            #tmb.showinfo("Hold On", "HOLD ON......")
            self._popup_message("hold on", "hold on....")
            self._root.title("Whot Game - HOLD ON")
            
            #self.__checkcomp_played.insert(0, 0)
            #self.__check2_played.insert(0, 1)
            self._computer.comp_powerup_1.insert(0, 0)
            self._checkmate()
            #self._root.after(500, self.__CompPlayEngine)
            #*
            self._root.after(500, lambda: self._card_streak(1))
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)
            #*
            #self._update_turn_indicator()
            #*
            #self.__CompPlayEngine()
            #self._root.after(500, lambda:self._popup_message("Continue", "Continue...."))

    def _p2_suspension(self):
        """Just like hold on, it suspends player2 until the computer plays another card or goes to mart"""
        if self._computer.comp_powerup_8[0] == 8:
            #tmb.showinfo("Hold On", "SUSPENSION")
            self._popup_message("hold on", "suspension")
            self._root.title("Whot Game - SUSPENSION")
            #self.__checkcomp_played.insert(0, 0)
            #self.__check2_played.insert(0, 1)
            self._computer.comp_powerup_8.insert(0, 0)
            self._checkmate()
            #self._root.after(500, self.__CompPlayEngine)
            #*
            self._root.after(500, lambda: self._card_streak(8))
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)
            #*
            #self._update_turn_indicator()
            #*
            #self.__CompPlayEngine()
            #self._root.after(500, lambda:self._popup_message("Continue", "Continue...."))

    def _check_p2(self, event=None):
        """Checks whether player2 clicked the mart button twice (in other words, checks whether player2 has
        picked two cards) and then unfreezes player2 cards (buttons) - for PICK TWO"""
        self._p2_mark(2)
        self.__checkcomp_played.insert(0, 1)
        self.__check2_played.insert(0, 0)
        #*
        self._update_turn_indicator()
        #*
        self._root.title("Whot Game - PICK TWO")
        if self._check2 == 2:
            self.__check2_played.insert(0, 1)
            self.__checkcomp_played.insert(0, 0)
            for i in self._buts2:
                i.config(state='normal')
            self._check2 = 0
            self._mark_but.config(command=self._p2_mark)
            self._root.bind("<Return>", self._p2_mark)
            self._root.title('Whot Game')
            #*
            self._update_turn_indicator()
            #*

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
            self._root.bind("<Return>", self._p2_mark)
            #*
            self._update_turn_indicator()
            #*
            
    def _make_hard(self):
        if self._mode_var.get() == 'hard':
            powerups = [1,2,8,14,20]
            chosen = choice(powerups)
            print("mode var is hard and chosen is: ", chosen)
            if self._computer.search_and_append(chosen):
                self._comp_mark(True)
            else:
                self._comp_mark()
        else:
            self._comp_mark()
    
    def _make_medium(self):
        if self._mode_var.get() == 'medium':
            powerups = [1,2,8,14,20]
            chosen = choice(powerups)
            print("mode var is medium and chosen is: ", chosen)
            if self._computer.search_and_append(chosen):
                self._comp_mark(True)
            else:
                self._comp_mark()
        else:
            self._comp_mark()
            
    def _card_streak(self, arg_num):
        print("Inside card_streak function...")
        if not self.__check_checkmate and not self._player2.check_requested:
        #if not self.__check_checkmate:
            print('ready.....')
            found_arg_num = []
            try:
                for o, i in enumerate(self._labs_refs):
                    if not i:
                        pass
                    else:
                        if i[0][1][1] == arg_num:
                            found_arg_num.append([o, i])
                            self._labs_refs.insert(o, [])
                            self._labs_refs.pop(self._labs_refs.index(i))
                            print("found an arg...")
                            break
            except IndexError:
                pass
            self.__checkcomp_played.insert(0, 0)
            self.__check2_played.insert(0, 1)
            #*
            self._update_turn_indicator()
            #*
            if found_arg_num:
                for i in found_arg_num:
                    self._play_comp(i[1][0], self._complab_ref.get(i[0]), found_arg_num)
                    break
            else:
                self._root.after(400, lambda:self._popup_message("Continue", "Continue...."))
                self.__checkcomp_played.insert(0, 1)
                self.__check2_played.insert(0, 0)
                #*
                self._update_turn_indicator()
                #*
                
        elif self._player2.check_requested:
            self._root.after(500, self.__CompPlayEngine())

    def __CompPlayEngine(self, event=None):
        """Engine for determining and getting what valid cards the computer has and can play....
        if after all and no valid card is found, the computer goes to market"""
        if self._player_turn('comp') and not self.__check_checkmate:
            try:
                for o, i in enumerate(self._labs_refs):
                    if not i:
                        pass
                    else:
                        if self._player2.check_requested:
                            if i[0][1][0] == self._player2.request:
                                self._found_request.append([o, i])
                                self._labs_refs.insert(o, [])
                                self._labs_refs.pop(self._labs_refs.index(i))
                                break
                                    
                        elif i[0][1][1] == 20:
                            print("self._labs_refs :", self._labs_refs, "\n")
                            print("i[0][1][1] : " , i[0][1][1], "\n")
                            self._found_20.append([o, i])
                            print([o, i], "has been appended to self._found_20 \n")
                            self._labs_refs.insert(o, [])
                            print(self._labs_refs.index(i), "has been inserted to self._labs_refs")
                            self._labs_refs.pop(self._labs_refs.index(i))
                            break

                        if not self._found_20:
                            if i[0][1][1] == self._whot.PlayedCards()[len(self._whot.PlayedCards()) - 1][1][1]:
                                self._found_num.append([o, i])
                                self._labs_refs.insert(o, [])
                                self._labs_refs.pop(self._labs_refs.index(i))
                                break

                        if not self._found_num and not self._found_20:
                            if i[0][1][0] == self._whot.PlayedCards()[len(self._whot.PlayedCards()) - 1][1][0]:
                                self._found_str.append([o, i])
                                self._labs_refs.insert(o, [])
                                self._labs_refs.pop(self._labs_refs.index(i))
                                break
                        
            except IndexError as e:
                print(e)
                pass
            #*
            self._update_turn_indicator()
            #*

            if self._found_20:
                try:
                    for i in self._found_20:
                        if i:
                            self._play_comp(i[1][0], self._complab_ref.get(i[0]), self._found_20)
                            break
                except IndexError:
                    pass

            elif self._found_num:
                try:
                    for i in self._found_num:
                        if i[1][0][1][1] == self._whot.PlayedCards()[len(self._whot.PlayedCards()) - 1][1][1]:
                            self._play_comp(i[1][0], self._complab_ref.get(i[0]), self._found_num)
                            break
                except IndexError as e:
                    pass

            elif self._found_str:
                try:
                    for i in self._found_str:
                        if i[1][0][1][0] == self._whot.PlayedCards()[len(self._whot.PlayedCards()) - 1][1][0]:
                            self._play_comp(i[1][0], self._complab_ref.get(i[0]), self._found_str)
                            break
                except IndexError as e:
                    pass
                
            elif self._found_request:
                for i in self._found_request:
                    self._play_comp(i[1][0], self._complab_ref.get(i[0]), self._found_request)
                    break
            else:
                #*
                self._make_hard()
                #*
            #self._root.title("Whot Game")
        else:
            print("It's not your turn to play")

    def _comp_play_20(self):
        found_1, found_2, found_8, found_14, found_none = [], [], [], [], []
        for o, i in enumerate(self._labs_refs):
            if not i:
                pass
            else:
                if i[0][1][1] == 1:
                    found_1.append(i[0][1][0])
                    break
                if not found_1:
                    if i[0][1][1] == 2:
                        found_2.append(i[0][1][0])
                        break
                if not found_1 and not found_2:
                    if i[0][1][1] == 8:
                        found_8.append(i[0][1][0])
                        break
                    if not found_8:
                        if i[0][1][1] == 14:
                            found_14.append(i[0][1][0])
                            break
                        if not found_14:
                            if i[0][1][0] != 'whot':
                                found_none.append(i[0][1][0])

        if found_1 or found_2 or found_8 or found_14:
            print('setting self._player2.check_requested to True...')
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
                    for o, i in enumerate(self._labs_refs):
                        if not i:
                            pass
                        else:
                            if i[0][1][0] == card:
                                self._found_20.append([o, i])
                                self._labs_refs.insert(o, [])
                                self._labs_refs.pop(self._labs_refs.index(i))
                                break
                except IndexError:
                    pass
                #*
                self._update_turn_indicator()
                #*

            if self._found_20:
                for i in self._found_20:
                    self._play_comp(i[1][0], self._complab_ref.get(i[0]), self._found_20)
                    break

            else:
                print("don't have the card going to mart")
                #*
                self._make_medium()
                #*
                
            print("not yet time to play")

    def _play_comp(self, labref=None, lab=None, found=None):
        """Plays any cards that are valid, from CompPlayEngine"""
        if labref and lab:
            print('inside play_comp function....')
            if self._player_turn('comp') and not self.__check_checkmate:
                if self._computer.play(labref):
                    self._played.configure(image=labref[0])
                    lab.grid_forget()
                    if found:
                        found.clear()
                    if labref[1][1] == 20 and len(self._computer.cards()) != 0:
                        self._comp_play_20() 
                    if labref[1][0] == self._player2.request:
                        self._player2.check_requested = None
                        self._player2.request = None   
                    self._display_comp_no_of_cards()
                    self._p2_pick_two()
                    self._p2_go_gen_mart()
                    self._p2_hold_on()
                    self._p2_suspension()
                    self.__checkcomp_played.insert(0, 1)
                    self.__check2_played.insert(0, 0)
                    #*
                    self._update_turn_indicator()
                    #*
                    self._checkmate()
                    #self._root.title('Whot Game')
            else:
                print("Computer please chill its not your turn to play....")
            pass

    def _comp_pick_two(self, times=1):
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
                #self._comp_mark()
                #*
                self._make_hard()
                #self._update_turn_indicator()
                #*
                self.__checkcomp_played.insert(0, 0)
                self.__check2_played.insert(0, 1)
            self._player2.p2_powerup_2.insert(0, 0)
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)
            #*
            #self._update_turn_indicator()
            #*

    def _comp_go_gen_mart(self):
        """Responsible for making the computer to pick one card - GENERAL MARKET"""
        if self._player_turn('comp'):
            if self._player2.p2_powerup_14[0] == 14:
                print("Going to gen mart")
                #self._comp_mark()
                #*
                self._make_medium()
                #*
                self._player2.p2_powerup_14.insert(0, 0)
                self.__checkcomp_played.insert(0, 1)
                self.__check2_played.insert(0, 0)
                #*
                #self._update_turn_indicator()
                #*

    def _comp_hold_on(self):
        """Responsible for making the computer to hold on while player2 plays again or goes to mart"""
        if self._player2.p2_powerup_1[0] == 1:
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)
            self._player2.p2_powerup_1.insert(0, 0)
            #*
            #self._update_turn_indicator()
            #*

    def _comp_suspension(self):
        """Responsible for suspending the computer while player2 plays again or goes to mart"""
        if self._player2.p2_powerup_8[0] == 8:
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)
            self._player2.p2_powerup_8.insert(0, 0)
            #*
            #self._update_turn_indicator()
            #*

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
        ttk.Button(text, text="Ok", command=text.destroy).grid()
        
    def _toggle_on_fullscreen(self, event=None):
        self._root.geometry('{}x{}+0+0'.format(*self.__full_size))

    def _toggle_off_fullscreen(self, event=None):
        self._root.geometry(self._orig_size)

    def _checkmate(self):
        """Freezes all the buttons and stops the computer or player2 from playing again
        if any one of the players cards finishes"""
        if len(self._player2.cards()) == 0:
            print("Last Card Has Been Played from you....")
            self.__checkcomp_played.insert(0, 1)
            self.__check_checkmate = True
            self._root.unbind("<Return>")
            tmb.showinfo("Checkmate", "You are the winner")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(state='disabled')
            self._root.title('Whot Game - Checkmate')
            self.__restart()

        elif len(self._computer.cards()) == 0:
            print("Last Card Has Been Played from computer....")
            self.__check2_played.insert(0, 1)
            self.__check_checkmate = True
            self._root.unbind("<Return>")
            tmb.showinfo("Checkmate", "The Computer is the winner")
            for i in self._buts2:
                i.config(state='disabled')
            self._mark_but.config(state='disabled')
            self._root.title('Whot Game - Checkmate')
            self.__restart()
            
    def __restart(self, event=None):
        """Restart the Whot Game"""
        ask = tmb.askyesnocancel("Restart Game", "Do you want to restart the game?")
        if ask:
            if sys.platform == 'linux':
                os.execv(sys.executable, ['python3'] + sys.argv)
            elif sys.platform == 'win32':
                os.execv(sys.executable, ['python'] + sys.argv)
        elif ask is None:
            pass
        else:
            sys.exit()
            
    def _norm_cards(self):
        """Adds one more container/Button/Label after they have been all used up or exhausted"""
        full_containers = []
        for o, i in enumerate(self._but_refs):
            if i:
                full_containers.append(i)
        
        if len(full_containers) == len(self._but_refs):
            self._but_refs.append([])
            self._labs_refs.append([])
            self._buts2.append(tk.Button(self._p2_frame_int))
            self._labs_comp.append(tk.Label(self._comp_frame_int))
            
            pos = len(self._but_refs) - 1
            print('pos is :', pos)
            self._p2_buts[pos] = self._buts2[pos]
            self._complab_ref[pos] = self._labs_comp[pos]
            self._set_theme(self._config_file.get('theme'))
            
            print("appended successfully....")
        pass

    def _mainloop(self):
        """calls tk mainloop"""
        self._root.focus_set()
        self._root.mainloop()

    def _p2_mark(self, power=None, event=None, arg=None):
        """Responsible for making player2 to go to market (pick a card from the mart)"""
        if self._player_turn('p2') and not self.__check_checkmate:
            if power:
                if power == 2:
                    self._check2 += 1
                elif power == 1:
                    self._check1 += 1

            for o, i in enumerate(self._but_refs):
                if not i:
                    if not arg:
                        self._player2.gomart()
                    self._but_refs[o].append(self._player2.cards()[len(self._player2.cards()) - 1])
                    new_but = self._p2_buts.get(o)
                    #
                    self._mark_but.grid_forget()
                    self._but = tk.Button(self._root, image=self._player2.cards()[len(self._player2.cards()) - 1][0])
                    #self._but.grid(row=2, column=0, sticky='w')
                    self._testing(2, self._but)
                    #self._testing(2, self._mark_but)
                    self._root.after(250, lambda:self._mark_but.grid(row=2, column=0, sticky='w'))
                    #
                    new_but.config(image=self._player2.cards()[len(self._player2.cards()) - 1][0],
                                command=lambda: self._play2(self._but_refs[o], self._p2_buts[o]))
                    #print('self._p2_btn_grid_pos is: ', self._p2_btn_grid_pos)
                    #new_but.grid(row=0, column=self._p2_btn_grid_pos, padx=6, pady=6)
                    #*
                    self._root.after(250, lambda:new_but.grid(row=0, column=self._p2_btn_grid_pos, padx=6, pady=6))
                    #*
                    self._p2_btn_grid_pos-=1
                    new_but.after(500, self.__CompPlayEngine)
                    #self._root.after(250, lambda:self._mark_but.grid(row=2, column=0, sticky='w'))
                    break
            self._display_p2_no_of_cards()
            self.__checkcomp_played.insert(0, 0)
            self.__check2_played.insert(0, 1)
            #*
            self._update_turn_indicator()
            #*
            self._norm_cards()
            if self._check2 == 1:
                self._root.title('Whot Game - PICK TWO')
            elif self._check2 == 0 or not self._check2:
                self._root.title('Whot Game')
            else:
                self._root.title('Whot Game')

    def _comp_mark(self, arg=None):
        """Responsible for making the computer to go to market (pick a card from the mart)
        The 'arg' argument checks whether the computer has already gone to mart before if the
        (self._computer.gomart()) has beeen called before"""
        if self._player_turn('comp') and not self.__check_checkmate:
            for o, i in enumerate(self._labs_refs):
                if not i:
                    if not arg:
                        self._computer.gomart()
                    else:
                        print("Cheat done....")
                    self._labs_refs[o].append(self._computer.cards()[len(self._computer.cards()) - 1])
                    new_lab = self._complab_ref.get(o)
                    #*
                    #self._testing(o)
                    #print('in comp mark o is :', o)
                    #*
                    new_lab.config(image=self._misc_whot1)
                    new_lab.grid(row=0, column=self._comp_lab_grid_pos, padx=6, pady=6)
                    self._comp_lab_grid_pos -=1
                    break
            self._display_comp_no_of_cards()
            self.__checkcomp_played.insert(0, 1)
            self.__check2_played.insert(0, 0)
            #*
            self._update_turn_indicator()
            self._norm_cards()
            #*
            self._root.title('Whot Game')
            
    def _Mtesting(self, i):
        #if i <= 3:
        self._mark_but.grid_forget()
        self._but = tk.Button(self._root, image=self._misc_whot)
        self._but.grid(row=2, column=0, sticky='w')
        #self._mark_but.grid(row=3, column=0, sticky='w')
        self._root.after(500, lambda:self._mark_but.grid(row=2, column=0, sticky='w'))
        #    i +=1
        pass
    
    def _testing(self, i, btn):
        if i <= 2:
            btn.grid(row=i, column=0, sticky='w')
            btn.after(160, lambda: self._testing(i, btn))
            i += 1
        else:
            print('.........====')
            btn.grid_forget()
            #self._mark_but.grid(row=2, column=0, sticky='w')
            
    #*
    def gather(self, player, num):
        self._whot.gather_requested(player, num)
        if player == 'p2':
            self.__checkcomp_played.insert(0,1)
            self._p2_mark(True)
        elif player == 'comp':
            self.__check2_played.insert(0, 1)
            self._comp_mark(True)


if __name__ == '__main__':
    app = WhotGtk()
    app._mainloop()