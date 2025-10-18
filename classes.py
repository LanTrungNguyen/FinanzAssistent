import tkinter as tk
#hello
class Row(): 
    def __init__(self, width, height, rowName, master, positionX=0, positionY=0, backgroundcolor="white") -> None: 
        self.width = width
        self.height = height
        self.rowName = rowName
        self.master = master
        self.backgroundcolor = backgroundcolor
        self.product = None

        self.frameRow = tk.Frame(self.master, width=self.width, height=self.height)
        self.frameRow.configure(background=self.backgroundcolor)
        self.frameRow.pack_propagate(False)
        self.frameRow.pack()
        # label = tk.Label(self.frameRow, text=f"this is {rowName}").pack(padx=20, pady=20)

"""
Was muss eine Spalte können?: 
    1. Existieren (Breite, Höhe)
    2. Produkte speichern 
    3. Produkte anzeigen
    4. Produkte hinzufügen 
    5. Produkte Löschen 
"""
class Column(): 
    def __init__(self, width, height, columnName, master, backgroundcolor="white") -> None:
        self.width = width
        self.height = height
        self.columnName = columnName
        self.master = master
        self.backgroundcolor = backgroundcolor
        self.products = []

        self.frameColumn = tk.Frame(master, width=self.width, height=self.height)
        self.frameColumn.configure(background=backgroundcolor)
        self.frameColumn.pack_propagate(False)
        self.frameColumn.pack()
        # label = tk.Label(self.frameColumn, text=f"this is {columnName}").pack(padx=20, pady=20)

    def add_product(self): 
        pass

    def remove_product(self): 
        pass