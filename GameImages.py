import tkinter as tk
class images:
    def __init__(self):
        self._circle1 = tk.PhotoImage(file=".//DIY//Circle//Circle_1.png")
        self._circle2 = tk.PhotoImage(file=".//DIY//Circle//Circle_2.png")
        self._circle3 = tk.PhotoImage(file=".//DIY//Circle//Circle_3.png")
        self._circle4 = tk.PhotoImage(file=".//DIY//Circle//Circle_4.png")
        self._circle5 = tk.PhotoImage(file=".//DIY//Circle//Circle_5.png")
        self._circle7 = tk.PhotoImage(file=".//DIY//Circle//Circle_7.png")
        self._circle8 = tk.PhotoImage(file=".//DIY//Circle//Circle_8.png")
        self._circle10 = tk.PhotoImage(file=".//DIY//Circle//Circle_10.png")
        self._circle11 = tk.PhotoImage(file=".//DIY//Circle//Circle_11.png")
        self._circle12 = tk.PhotoImage(file=".//DIY//Circle//Circle_12.png")
        self._circle13 = tk.PhotoImage(file=".//DIY//Circle//Circle_13.png")
        self._circle14 = tk.PhotoImage(file=".//DIY//Circle//Circle_14.png")
    

        self._triangle1 = tk.PhotoImage(file=".//DIY//Triangle/Triangle_1.png")
        self._triangle2 = tk.PhotoImage(file=".//DIY//Triangle/Triangle_2.png")
        self._triangle3 = tk.PhotoImage(file=".//DIY//Triangle/Triangle_3.png")
        self._triangle4 = tk.PhotoImage(file=".//DIY//Triangle/Triangle_4.png")
        self._triangle5 = tk.PhotoImage(file=".//DIY//Triangle/Triangle_5.png")
        self._triangle7 = tk.PhotoImage(file=".//DIY//Triangle/Triangle_7.png")
        self._triangle8 = tk.PhotoImage(file=".//DIY//Triangle/Triangle_8.png")
        self._triangle10 = tk.PhotoImage(file=".//DIY//Triangle/Triangle_10.png")
        self._triangle11 = tk.PhotoImage(file=".//DIY//Triangle/Triangle_11.png")
        self._triangle12 = tk.PhotoImage(file=".//DIY//Triangle/Triangle_12.png")
        self._triangle13 = tk.PhotoImage(file=".//DIY//Triangle/Triangle_13.png")
        self._triangle14 = tk.PhotoImage(file=".//DIY//Triangle/Triangle_14.png")

        self._square1 = tk.PhotoImage(file=".//DIY//Square/Square_1.png")
        self._square2 = tk.PhotoImage(file=".//DIY//Square/Square_2.png")
        self._square3 = tk.PhotoImage(file=".//DIY//Square/Square_3.png")
        self._square5 = tk.PhotoImage(file=".//DIY//Square/Square_5.png")
        self._square7 = tk.PhotoImage(file=".//DIY//Square/Square_7.png")
        self._square14 = tk.PhotoImage(file=".//DIY//Square/Square_14.png")
        self._square10 = tk.PhotoImage(file=".//DIY//Square/Square_10.png")
        self._square11 = tk.PhotoImage(file=".//DIY//Square/Square_11.png")
        self._square13 = tk.PhotoImage(file=".//DIY//Square/Square_13.png") 

        self._cross1 = tk.PhotoImage(file=".//DIY//Cross/Cross_1.png")
        self._cross2 = tk.PhotoImage(file=".//DIY//Cross/Cross_2.png")
        self._cross3 = tk.PhotoImage(file=".//DIY//Cross/Cross_3.png")
        self._cross5 = tk.PhotoImage(file=".//DIY//Cross/Cross_5.png")
        self._cross7 = tk.PhotoImage(file=".//DIY//Cross/Cross_7.png")
        self._cross10 = tk.PhotoImage(file=".//DIY//Cross/Cross_10.png")
        self._cross11 = tk.PhotoImage(file=".//DIY//Cross/Cross_11.png")
        self._cross13 = tk.PhotoImage(file=".//DIY/Cross/Cross_13.png")
        self._cross14 = tk.PhotoImage(file=".//DIY//Cross/Cross_14.png")
        
        self._star1 = tk.PhotoImage(file=".//DIY//Star//Star_1.png")
        self._star2 = tk.PhotoImage(file=".//DIY//Star//Star_2.png")
        self._star3 = tk.PhotoImage(file=".//DIY//Star//Star_3.png")
        self._star4 = tk.PhotoImage(file=".//DIY//Star//Star_4.png")
        self._star5 = tk.PhotoImage(file=".//DIY//Star//Star_5.png")
        self._star7 = tk.PhotoImage(file=".//DIY//Star//Star_7.png")
        self._star8 = tk.PhotoImage(file=".//DIY//Star//Star_8.png")
        
        self._whot1 = tk.PhotoImage(file=".//DIY//Whot//Whot_1.png")
        self._whot2 = tk.PhotoImage(file=".//DIY//Whot//Whot_2.png")
        self._whot3 = tk.PhotoImage(file=".//DIY//Whot//Whot_3.png")
        self._whot4 = tk.PhotoImage(file=".//DIY//Whot//Whot_4.png")
        self._whot5 = tk.PhotoImage(file=".//DIY//Whot//Whot_5.png")

        self._misc_whot = tk.PhotoImage(file=".//DIY//Misc//Misc_whot1.png")
        self._misc_whot1 = tk.PhotoImage(file=".//DIY//Misc//Misc_whot2.png")
        
        self._cross_icon = tk.PhotoImage(file='.//cards//cross.png')
        self._circle_icon = tk.PhotoImage(file='.//cards//circle.png')
        self._triangle_icon = tk.PhotoImage(file='.//cards//triangle.png')
        self._square_icon = tk.PhotoImage(file='.//cards//square.png')
        self._star_icon = tk.PhotoImage(file='.//cards//star.png')

        circle=[(self._circle1, ('circle',1)),(self._circle2, ('circle',2)), (self._circle3, ('circle',3)),
                (self._circle4, ('circle',4)), (self._circle5, ('circle',5)), (self._circle7, ('circle',7)),
                  (self._circle8, ('circle',8)), (self._circle10, ('circle',10)), (self._circle11, ('circle',11)),
                  (self._circle12, ('circle',12)), (self._circle13, ('circle',13)), (self._circle14, ('circle',14))]

        triangle=[(self._triangle1, ('triangle',1)), (self._triangle2, ('triangle',2)), (self._triangle3, ('triangle',3)),
          (self._triangle4, ('triangle',4)), (self._triangle5, ('triangle',5)), (self._triangle7, ('triangle',7)),
          (self._triangle8, ('triangle',8)), (self._triangle10, ('triangle',10)), (self._triangle11, ('triangle',11))]

        square=[(self._square1, ('square',1)), (self._square2, ('square',2)), (self._square3, ('square',3)), (self._square5, ('square',5)),
                (self._square7, ('square',7)), (self._square10, ('square',10)), (self._square11, ('square',11)), (self._square13, ('square',13)), 
                (self._square14, ('square',14)),]

        cross=[(self._cross1, ('cross',1)), (self._cross2, ('cross',2)), (self._cross3, ('cross',3)), (self._cross5, ('cross',5)),
               (self._cross7, ('cross',7)), (self._cross10, ('cross',10)), (self._cross11, ('cross',11)), (self._cross13, ('cross',13)),
               (self._cross14, ('cross',14))]

        star=[(self._star1, ('star',1)), (self._star2, ('star',2)), (self._star3, ('star',3)), (self._star4, ('star',4)),
      (self._star5, ('star',5)), (self._star7, ('star',7)), (self._star8, ('star',8))]


        whot=[(self._whot1, ('whot',20)), (self._whot2, ('whot',20)), (self._whot3, ('whot',20)), (self._whot4, ('whot',20)),
              (self._whot5, ('whot',20))]
        
        
        self._DepotMarket = circle+triangle+square+cross+star+whot
            
if __name__ == '__main__':
    root = tk.Tk()
    app = images()
