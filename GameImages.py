import tkinter as tk
import os

class images:
    def __init__(self):
        image_dir = os.path.join(os.getcwd(), "DIY")
        card_dir = os.path.join(os.getcwd(), "cards")

        circle = self.create_image_data(os.path.join(image_dir, "Circle"))
        triangle = self.create_image_data(os.path.join(image_dir, "Triangle"))
        square = self.create_image_data(os.path.join(image_dir, "Square"))
        cross = self.create_image_data(os.path.join(image_dir, "Cross"))
        star = self.create_image_data(os.path.join(image_dir, "Star"))

        whot_dir = os.path.join(image_dir, "Whot")
        whot_dir_list = os.listdir(whot_dir)
        whot = [
            (
                tk.PhotoImage(file=os.path.join(whot_dir, filename)),
                (os.path.basename(whot_dir), 20)
            )
            for filename in whot_dir_list
        ]

        self._cross_icon = tk.PhotoImage(file=os.path.join(card_dir, "cross.png"))
        self._circle_icon = tk.PhotoImage(file=os.path.join(card_dir, "circle.png"))
        self._triangle_icon = tk.PhotoImage(file=os.path.join(card_dir, "triangle.png"))
        self._square_icon = tk.PhotoImage(file=os.path.join(card_dir, "square.png"))
        self._star_icon = tk.PhotoImage(file=os.path.join(card_dir, "star.png"))

        misc_dir = os.path.join(image_dir, "Misc")
        self._misc_whot = tk.PhotoImage(file=os.path.join(misc_dir, "Misc_whot1.png"))
        self._misc_whot1 = tk.PhotoImage(file=os.path.join(misc_dir, "Misc_whot2.png"))

        self._DepotMarket = circle + triangle + square + cross + star + whot
        # print('DepotMarket -->', self._DepotMarket)
        # print('length -->', len(self._DepotMarket))
        
    def create_image_data(self, directory: str) -> list[tuple[tk.PhotoImage, tuple[str, int]]]:
        dir_list = os.listdir(directory)
        return [
            (
                # tk.PhotoImage(file=f"{directory}/{filename}"),
                tk.PhotoImage(file=os.path.join(directory, filename)),
                (os.path.basename(directory), int(filename.split('_')[-1].split('.')[0]))
            )
            for filename in dir_list
        ]
            
if __name__ == '__main__':
    root = tk.Tk()
    app = images()
