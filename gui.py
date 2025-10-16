import tkinter as tk
from classes import *

root = tk.Tk()
p_e_w_open = False
width= root.winfo_screenwidth()               
height= root.winfo_screenheight() 

def save_product_entries() -> None: 
    entry = {
        "name" : product_entry.get(), 
        "quantity" : product_quantity.get(), 
        "price" : price_entry.get(), 
        "details" : product_details.get("1.0", "end")
    }
    
    wishlistColumn.products.append(entry)
    print(wishlistColumn.products)
     


def product_entry_window() -> None: 
    global p_e_w_open
    if p_e_w_open: 
        return 
    
    p_e_w_open = True
    window = tk.Toplevel(root)
    window.title("Eingabe")
    window_width = 550
    window_height = 300
    window.resizable(False, False)

    # Popup Fenster zentrieren
    x = (width-window_width) // 2
    y = (height-window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def on_close():
        global p_e_w_open
        p_e_w_open = False
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)

    # === Red row container ===
    product_entry_row = Row(width=window_width, height=window_height/3,
                            rowName="product_entry_row", master=window, backgroundcolor="red")

    # Force it to stay at the top and not expand vertically
    product_entry_row.frameRow.pack(side="top", fill="x", anchor="nw")

    # === Inner frame for horizontal layout ===
    top_line = tk.Frame(product_entry_row.frameRow, bg="red")
    top_line.pack(side="top", anchor="nw")  # keeps everything at the top

    # === Widgets aligned horizontally ===
    global product_entry
    product_entry = tk.Entry(top_line, width=35, font=("Calibri", 13))
    product_entry.pack(side="left", padx=9, pady=5)

    global product_quantity
    product_quantity = tk.Spinbox(top_line, width=4, font=("Calibri", 13),
                                  from_=1, to=10, state='readonly')
    product_quantity.pack(side="left", padx=7, pady=5)

    # Funktion, sodass nur Ziffern mit 2 Nachkommastellen möglich sind
    def validate_price(text):
        if text == "":
            return True
        import re
        return bool(re.fullmatch(r"\d+(\.\d{0,2})?", text))

    # Jede Taste der Formalensprache überprüfen (Zahl mit zwei Nachkommastellen)
    vcmd = (window.register(validate_price), "%P")

    # validate="key" : bei jedem Tastendruck
    global price_entry
    price_entry = tk.Entry(top_line, width=10, font=("Calibri", 13), validate="key", validatecommand=vcmd)
    price_entry.pack(side="left", padx=(7, 0), pady=5)
    
    price_label = tk.Label(top_line, width=4, text="€", font=("Calibri", 12), background="grey")
    price_label.pack_propagate(False)
    price_label.pack(side="left")

    send_bt = tk.Button(product_entry_row.frameRow, text="Send -->", width=23, bd=1, font=("Calibri", 11), command=lambda:[save_product_entries(), on_close()])
    send_bt.pack_propagate(False)
    send_bt.pack(pady=10, padx=9, side="right")

    # === Grey detail area below ===
    product_detail_row = Row(width=window_width, height=window_height*2/3,
                             rowName="product_detail_row", master=window, backgroundcolor="grey")

    global product_details
    product_details = tk.Text(product_detail_row.frameRow, font=("Calibri", 13), width=50)
    product_details.pack_propagate(False)
    product_details.pack(pady=10, padx=10, fill="both", expand=True)

def worker_gui() -> None: 

    root.title("Finanzassistent")
    root.configure(background="lightgrey")
    root.geometry(f"{width}x{height}+0+0")

    # Blau
    heaader = Row(width=width, height=height/15, rowName="header", master=root, backgroundcolor="blue")
    # Drei Spalten
    main_body = Row(width=width, height=height*8/15, rowName="main_body", master=root, backgroundcolor="yellow")
    # Grün
    control_row = Row(width=width, height=height*6/15, rowName="control", master=root, backgroundcolor="green")

    # Wunschliste - Braun
    global wishlistColumn
    wishlistColumn = Column(width=width/3, height=main_body.height, columnName="wishlist", master=main_body.frameRow, backgroundcolor="brown")
    wishlistColumn.frameColumn.pack(side="left", expand=True, fill="both")

    add_product_bt = tk.Button(wishlistColumn.frameColumn, text="   +   ", font=("Calibri 12") , width=int(wishlistColumn.width), command=product_entry_window, bd=1)
    add_product_bt.pack_propagate(False)
    add_product_bt.pack()

    # Ausstehende Autorisproduct_entry = Row(width=500)ierung - Rot
    askingForAuthorization = Column(width=width/3, height=main_body.height, columnName="askingForAuthorization", master=main_body.frameRow, backgroundcolor="red")
    askingForAuthorization.frameColumn.pack(side="left", expand=True, fill="both")

    # Autorisierte Produkte - Lila
    authorized = Column(width=width/3, height=main_body.height, columnName="authorized", master=main_body.frameRow, backgroundcolor="purple")
    authorized.frameColumn.pack(side="left", expand=True, fill="both")
    
    root.mainloop()

if __name__ == "__main__": 
    worker_gui()