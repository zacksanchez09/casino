# # # # # from tkinter import *
# # # # # from tkinter.ttk import *

# # # # # def clicked():
# # # # #     title.configure(text="Coin Selected")
# # # # #     print(one_state.get())
# # # # #     title.grid(column=10, row=220)

# # # # from tkinter import *
# # # # from PIL import ImageTk,Image

# # # # window = Tk()
# # # # # canvas = Canvas(window, width = 300, height = 300)
# # # # # canvas.pack()
# # # # window.title("Coins Machine")

# # # # # img = ImageTk.PhotoImage(Image.open("coins.png"))
# # # # # canvas.create_image(20, 20, anchor=NW, image=img)

# # # # title = Label(window, text="Coins", font=("Arial Bold", 25))
# # # # title.grid(column=10, row=10)

# # # # coins = [1, 2, 5, 10]

# # # # # Disable Coins
# # # # def switchOne():
# # # #     if one["state"] == "normal":
# # # #         one["state"] = "disabled"
# # # #         disableOne["text"] = "enable"
# # # #         coins.pop(0)
# # # #     else:
# # # #         one["state"] = "normal"
# # # #         disableOne["text"] = "disable"
# # # #         coins.append(coin)

# # # # def switchTwo():
# # # #     coin = 2
# # # #     if two["state"] == "normal":
# # # #         two["state"] = "disabled"
# # # #         disableTwo["text"] = "enable"
# # # #         coins.pop(1)
# # # #     else:
# # # #         two["state"] = "normal"
# # # #         disableTwo["text"] = "disable"
# # # #         coins.append(coin)

# # # # def switchFive():
# # # #     coin = 5
# # # #     if five["state"] == "normal":
# # # #         five["state"] = "disabled"
# # # #         disableFive["text"] = "enable"
# # # #         coins.pop(2)
# # # #     else:
# # # #         five["state"] = "normal"
# # # #         disableFive["text"] = "disable"
# # # #         coins.append(coin)

# # # # def switchTen():
# # # #     coin = 10
# # # #     if ten["state"] == "normal":
# # # #         ten["state"] = "disabled"
# # # #         disableTen["text"] = "enable"
# # # #         coins.pop(3)
# # # #     else:
# # # #         ten["state"] = "normal"
# # # #         disableTen["text"] = "disable"
# # # #         coins.append(coin)

# # # # def withdraw():
# # # #     print(coins)

# # # # #--Buttons
# # # # one = Button(window, text="$1", command=switchOne)
# # # # one.grid(column=10, row=15)

# # # # disableOne = Button(text="disable", command=switchOne)
# # # # disableOne.grid(row=15, column=11)

# # # # two = Button(window, text="$2", command=switchTwo)
# # # # two.grid(column=10, row=25)

# # # # disableTwo = Button(text="disable", command=switchTwo)
# # # # disableTwo.grid(row=25, column=11)

# # # # five = Button(window, text="$5", command=switchFive)
# # # # five.grid(column=10, row=35)

# # # # disableFive = Button(text="disable", command=switchFive)
# # # # disableFive.grid(row=35, column=11)

# # # # ten = Button(window, text="$10", command=switchTen)
# # # # ten.grid(column=10, row=45)

# # # # disableTen = Button(text="disable", command=switchTen)
# # # # disableTen.grid(row=45, column=11)

# # # # withdrawButton = Button(window, text="Cobrar", command=withdraw)
# # # # withdrawButton.grid(column=35, row=25)

# # # # # window.geometry("300x300")
# # # # window.mainloop()


# # # # from tkinter import *
# # # # from PIL import ImageTk,Image
# # # # root = Tk()
# # # # root.title("Coins Machine")
# # # # canvas = Canvas(root, width = 1200, height = 600)
# # # # canvas.pack()
# # # # img = ImageTk.PhotoImage(Image.open("coins.png"))
# # # # canvas.create_image(5, 5, anchor=NW, image=img)


# # # # root.mainloop()

# # import tkinter as tk
# # from tkinter import scrolledtext as st
# # import sys
# # import os
# # from os import listdir
# # from tkinter import filedialog as fd
# # from tkinter import messagebox as mb
# # from tkinter import font
# # from tkinter import *
# # from tkinter import ttk
# # import tkinter

# # class Aplicacion:

# #     def __init__(self):

# #         self.window=tk.Tk()
# #         self.window.title("Coins Machine")
# #         self.appHighlightFont = font.Font(family='Helvetica', size=16, weight='normal')
# #         label_2 = Label(self.window, text="Coins Machine", font=self.appHighlightFont).place(x=480,y=5)
# #         self.canvas=tk.Canvas(self.window, width=900, height=300, background="white")
# #         self.canvas.grid(column=0, row=0)

# #         file_1=tk.PhotoImage(file="coins.png")
# #         self.canvas.create_image(50, 100, image=file_1, anchor="nw")

# #         file_2=tk.PhotoImage(file="coins.png")
# #         self.canvas.create_image(300, 100, image=file_2, anchor="nw")

# #         file_3=tk.PhotoImage(file="coins.png")
# #         self.canvas.create_image(550, 100, image=file_3, anchor="nw")

# #         self.select_1=tk.IntVar()
# #         self.check_1=tk.Checkbutton(self.window,text="$1", variable=self.select_1)
# #         self.check_1.grid(column=30, row=10)
# #         self.select_2=tk.IntVar()
# #         self.check_2=tk.Checkbutton(self.window,text="$2", variable=self.select_2)
# #         self.check_2.grid(column=30, row=15)
# #         self.select_3=tk.IntVar()
# #         self.check_3=tk.Checkbutton(self.window,text="$5", variable=self.select_3)
# #         self.check_3.grid(column=30, row=20)

# #         self.button_1=tk.Button(self.window, text="Jugar", command=self.verifyCoins)
# #         self.button_1.grid(column=30, row=25)

# #         self.label_1=tk.Label(text="Monedas Seleccionadas:")
# #         self.label_1.grid(column=30, row=30)

# #         self.window.mainloop()

# #     def verifyCoins(self):
# #         cant=0
# #         if self.select_1.get()==1:
# #             cant+=1
# #         if self.select_2.get()==1:
# #             cant+=1
# #         if self.select_3.get()==1:
# #             cant+=1
# #         self.label_1.configure(text="cantidad:"+str(cant))

# # application=Aplicacion()


# import tkinter as tk

# class Aplicacion:
#     def __init__(self):
#         self.ventana1=tk.Tk()
#         self.canvas1=tk.Canvas(self.ventana1, width=900, height=500, background="black")
#         self.canvas1.grid(column=0, row=0)
#         archi1=tk.PhotoImage(file="coins.png")
#         self.canvas1.create_image(30, 100, image=archi1, anchor="nw", tags="movil")
#         archi2=tk.PhotoImage(file="cards.png")
#         self.canvas1.create_image(400, 100, image=archi2, anchor="nw", tags="movil")
#         self.canvas1.tag_bind("movil", "<ButtonPress-1>", self.presion_boton)
#         self.canvas1.tag_bind("movil", "<Button1-Motion>", self.mover)
#         self.carta_seleccionada = None
#         self.ventana1.mainloop()

#     def presion_boton(self, evento):
#         carta = self.canvas1.find_withtag(tk.CURRENT)
#         self.carta_seleccionada = (carta, evento.x, evento.y)

#     def mover(self, evento):
#         x, y = evento.x, evento.y
#         carta, x1, y1 = self.carta_seleccionada
#         self.canvas1.move(carta, x - x1, y - y1)
#         self.carta_seleccionada = (carta, x, y)

# aplicacion1=Aplicacion()


import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import random
from random import shuffle

class Aplicacion:

    def __init__(self):

        self.window=tk.Tk()
        self.window.title("Coins Machine")
        self.crear_botones()
        self.canvas=tk.Canvas(self.window, width=800, height=400, background="black")
        self.canvas.grid(column=0, row=4)
        self.coins = []
        self.images = []

        self.file_1=tk.PhotoImage(file="coins.png")
        self.file_2=tk.PhotoImage(file="cards.png")
        self.file_3=tk.PhotoImage(file="game-coins.png")
        self.file_4=tk.PhotoImage(file="cubes.png")
        self.file_5=tk.PhotoImage(file="sevens.png")

        self.window.mainloop()

    def play(self):
        x = [[i] for i in range(6)]
        shuffle(x)
        for n in x:
            self.images.append(n)
            print(n)
        print(self.images)
        self.canvas.create_image(50, 100, image=self.file_1, anchor="nw")
        self.canvas.create_image(300, 100, image=self.file_2, anchor="nw")
        self.canvas.create_image(550, 100, image=self.file_4, anchor="nw")

    def changeCredits(self):
        print(self.coins)

    def verifyCoins(self):
        cant = 0
        value = 0
        if self.select_1.get() == 1:
            value = 1
            if value in self.coins:
                pass
            else:
                self.coins.append(value)
        elif self.select_1.get() == 0:
            value = 1
            if value in self.coins:
                self.coins.remove(value)
        if self.select_2.get() == 1:
            value = 2
            if value in self.coins:
                pass
            else:
                self.coins.append(value)
        elif self.select_2.get() == 0:
            value = 2
            if value in self.coins:
                self.coins.remove(value)
        if self.select_3.get() == 1:
            value = 5
            if value in self.coins:
                pass
            else:
                self.coins.append(value)
        elif self.select_3.get() == 0:
            value = 5
            if value in self.coins:
                self.coins.remove(value)
        if self.select_4.get() == 1:
            value = 10
            if value in self.coins:
                pass
            else:
                self.coins.append(value)
        elif self.select_4.get() == 0:
            value = 10
            if value in self.coins:
                self.coins.remove(value)
        if self.select_5.get() == 1:
            value = 20
            if value in self.coins:
                pass
            else:
                self.coins.append(value)
        elif self.select_5.get() == 0:
            value = 20
            if value in self.coins:
                self.coins.remove(value)
        print(self.coins)
        self.label_1.configure(text="Cambio con: "+ str(self.coins))

    def crear_botones(self):
        self.labelframe1=ttk.LabelFrame(self.window, text="Coins Machine")
        self.select_1=tk.IntVar()
        self.check_1=tk.Checkbutton(self.labelframe1, text="$1", variable=self.select_1)
        self.check_1.grid(column=1, row=2, padx=5)

        self.select_2=tk.IntVar()
        self.check_2=tk.Checkbutton(self.labelframe1, text="$2", variable=self.select_2)
        self.check_2.grid(column=2, row=2, padx=5)

        self.select_3=tk.IntVar()
        self.check_3=tk.Checkbutton(self.labelframe1, text="$5", variable=self.select_3)
        self.check_3.grid(column=3, row=2, padx=5)

        self.select_4=tk.IntVar()
        self.check_4=tk.Checkbutton(self.labelframe1, text="$10", variable=self.select_4)
        self.check_4.grid(column=4, row=2, padx=5)

        self.select_5=tk.IntVar()
        self.check_5=tk.Checkbutton(self.labelframe1, text="$20", variable=self.select_5)
        self.check_5.grid(column=5, row=2, padx=5)

        self.button_1=tk.Button(self.labelframe1, text="Guardar", command=self.verifyCoins)
        self.button_1.grid(column=30, row=25)

        self.button_2=tk.Button(self.labelframe1, text="Jugar", command=self.play)
        self.button_2.grid(column=30, row=35)

        self.button_3=tk.Button(self.labelframe1, text="Cambiar Creditos", command=self.changeCredits)
        self.button_3.grid(column=30, row=45)

        self.label_1=tk.Label(self.labelframe1, text="Monedas Seleccionadas:")
        self.label_1.grid(column=0, row=4)

        self.label_same=tk.Label(self.labelframe1, text="2 Iguales: 5")
        self.label_same.grid(column=35, row=1, padx=5)

        self.label_coins=tk.Label(self.labelframe1, text="3 Monedas: 10")
        self.label_coins.grid(column=35, row=2, padx=5)

        self.label_naipes=tk.Label(self.labelframe1, text="3 Naipes: 15")
        self.label_naipes.grid(column=35, row=3, padx=5)

        self.label_fichas=tk.Label(self.labelframe1, text="3 Fichas: 20")
        self.label_fichas.grid(column=35, row=4, padx=5)

        self.label_cubes=tk.Label(self.labelframe1, text="3 Dados: 25")
        self.label_cubes.grid(column=35, row=5, padx=5)

        self.label_sevens=tk.Label(self.labelframe1, text="3 Sietes: 30")
        self.label_sevens.grid(column=35, row=6, padx=5)

        self.labelframe1.grid(column=0, row=0, sticky="w", padx=5, pady=5)

    def borrar_todos(self):
        self.canvas.delete(tk.ALL)

aplicacion1=Aplicacion()
