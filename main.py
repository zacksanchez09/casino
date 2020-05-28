"""
Casino - Algoritmo Voraz
Seminario de Solución de Problemas de Algoritmia
Created By: Isaac Eduardo Sánchez Campos
Código: 211172172
"""

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import random
from random import shuffle
from tkinter import messagebox as mb

class Aplicacion:

    def __init__(self):

        self.window=tk.Tk()
        self.window.title("Coins Machine")
        self.crear_botones()
        self.canvas=tk.Canvas(self.window, width=800, height=400, background="black")
        self.canvas.grid(column=0, row=4)
        self.coins = []
        self.images = []
        self.credits = 0
        self.counters = []

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
        print(len(self.coins))
        self.counters = [None] * len(self.coins)
        print(self.counters, len(self.counters))
        for i in range(len(self.coins)):
            self.counters[i-1] = 0
        counter = 0
        while self.credits != 0:
            print(self.coins)
            if self.coins[counter] <= self.credits:
                self.credits = self.credits - self.coins[counter]
                self.counters[counter] = self.counters[counter] + 1;
            else:
                counter += 1
        for i in range(len(self.coins)):
            print(self.coins[i], self.counters[i])
        self.credits_label.configure(text="Creditos: "+ str(self.credits))
        self.credits_change_label.configure(text="Su cambio con : "+ str(self.coins))
        self.counters_change_label.configure(text=str(self.counters) + " monedas respectivamente.")

    def addCredits(self):
        credits = self.credits_input.get()
        self.credits += int(credits)
        self.credits_label.configure(text="Creditos: "+ str(self.credits))
        print(self.credits)
        mb.showinfo("Alerta","Creditos añadidos correctamente. ✅")

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
        self.coins.sort(reverse=True)
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

        self.credits_label=tk.Label(self.labelframe1,text="Creditos:")
        self.credits_label.grid(column=0, row=10)
        self.credits=tk.IntVar()
        self.credits_input=tk.Entry(self.labelframe1, width=25, textvariable=self.credits)
        self.credits_input.grid(column=0, row=12)
        self.add_credits_button=tk.Button(self.labelframe1, text="Añadir", command=self.addCredits)
        self.add_credits_button.grid(column=0, row=14)

        self.credits_change_label=tk.Label(self.labelframe1,text="Su cambio con: ")
        self.credits_change_label.grid(column=0, row=16)

        self.counters_change_label=tk.Label(self.labelframe1, text=" monedas respectivamente.")
        self.counters_change_label.grid(column=0, row=18)

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
