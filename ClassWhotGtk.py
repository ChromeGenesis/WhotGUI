#import ClassWhotCopy3
import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as tks
from manual import manual
from ImageCopy import images
from random import shuffle
import Main
#import DIY

class WhotGtk(images):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('790x500')
        self.root.title('Whot Game')
        images.__init__(WhotGtk)
        self._frame1 = tk.Frame(self.root, bg='DeepSkyBlue2', width=50, height=45)
        self._frame1.grid(row=0, columnspan=5, sticky='we')
        self._frame1.grid_columnconfigure(0, weight=1)
        self._frame2 = tk.Frame(self.root, bg='aquamarine')
        self._frame2.grid(row=1, column=2)
        self._frame2.grid_columnconfigure(0, weight=1)
        menu_bar = tk.Menu(self.root)
        self.whot = Main.Whot()
        self.whot.InitDepot()
        self.whot.InitPlayerCards()
        self.whot.InitComputerCards()
        self.whot.InitPlayer2Cards()
        self.computer = Main.Computer()
        self.player2 = Main.Player2()
        self._but1ref=[]
        self._but2ref=[]
        self._but3ref=[]
        self._but4ref=[]
        self._but5ref=[]

        self._but1 = tk.Button(self._frame1, image=self.player2.cards()[4][0], command=lambda:self._callback(self._but1ref, self._but1))
        self._but1.grid(row=0, column=0)
        self._but1ref.append(self.player2.cards()[4])
        
        self._but2 = tk.Button(self._frame1, image=self.player2.cards()[0][0], command=lambda:self._callback(self._but2ref, self._but2))
        self._but2.grid(row=0, column=1)
        self._but2ref.append(self.player2.cards()[0])
        
        self._but3 = tk.Button(self._frame1, image=self.player2.cards()[1][0], command=lambda:self._callback(self._but3ref, self._but3))
        self._but3.grid(row=0, column=2)
        self._but3ref.append(self.player2.cards()[1])
        
        self._but4 = tk.Button(self._frame1, image=self.player2.cards()[2][0], command=lambda:self._callback(self._but4ref, self._but4))
        self._but4.grid(row=0, column=3)
        self._but4ref.append(self.player2.cards()[2])
        
        self._but5 = tk.Button(self._frame1, image=self.player2.cards()[3][0], command=lambda:self._callback(self._but5ref, self._but5))
        self._but5.grid(row=0, column=4)
        self._but5ref.append(self.player2.cards()[3])

        self._lab = tk.Label(self._frame2, image=self.whot.PlayedCards()[len(self.whot.PlayedCards())-1][0])
        self._lab.grid(row=1, column=2, sticky='w')


        about_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='About', menu=about_menu)
        about_menu.add_command(label='Manual',accelerator='Ctrl+M', compound='left', command=self.Manual)
        self.root.config(menu=menu_bar)
        self.root.grid_columnconfigure(2, weight=1)
        #self.root.grid_rowconfigure(0, weight=1)
        self.root.bind_all("<Control-m>", self.Manual)
        pass
       
    def _callback(self, butref=None, but=None, event=True):
        if butref:
            if self.player2.play(butref[0]):
                print("play returned true")
                #self.lab.grid_forget()
                self._lab.configure(image=butref[0][0])
                self._lab.grid(row=1, column=2, sticky='w')
                but.grid_remove()
                but = None
                butref.clear()
                #print(event)
            else:
                print("play returned none or false")
        pass
    
    def Manual(self, event=None):
        if self.root:
            text = tk.Toplevel(self.root)
        else:
            text = tk.Toplevel(tk.Tk())
        text.title("<Manual>")
        text.transient(self.root)
        text_lab = tks.ScrolledText(text, wrap='word')
        text_lab.grid(row=0, column=0, sticky=tk.NSEW)
        text_lab.insert(1.0, manual)
        text.grid_rowconfigure(1, weight=1)
        text.grid_columnconfigure(0, weight=1)
        text_lab.configure(state='disabled')
        ttk.Button(text, text="Ok", command=lambda: self._destroy(text)).grid()
    
    def _destroy(self, arg, event=None):
        arg.destroy()

    def _mainloop(self):
        self.root.mainloop()

    def _mart(self):
        for i in [self._but1, self._but2, self._but3, self._but4, self._but5]:
            if i is self._but1:
                if not self._but1:
                    self.player2.gomart()
                    self._but1 = tk.Button(self.root, image=self.player2.cards()[4][0])
                    self._but1.grid(row=0, column=0)
                    self._but1ref.append(self.player2.cards()[4])
        pass




app = WhotGtk()
app._mainloop()
    
