import tkinter as tk
from tkinter import messagebox
import qrcode

root = tk.Tk()
root.title("METRO SOFTWARE")

fare = 30
from_station = tk.StringVar()
to_station = tk.StringVar()

def on_click_1(): from_station.set("SHIKARGARH")
def on_click_2(): from_station.set("RATANADA")
def on_click_3(): from_station.set("PAOTA")
def on_click_4(): from_station.set("SARDARPURA")
def on_click_5(): from_station.set("BASNI")
def on_click_6(): from_station.set("SHASTRI NAGAR")
def on_click_7(): from_station.set("BANAR")
def on_click_8(): from_station.set("CHOUPASNI")

def on_click_9(): to_station.set("SHIKARGARH")
def on_click_10(): to_station.set("RATANADA")
def on_click_11(): to_station.set("PAOTA")
def on_click_12(): to_station.set("SARDARPURA")
def on_click_13(): to_station.set("BASNI")
def on_click_14(): to_station.set("SHASTRI NAGAR")
def on_click_15(): to_station.set("BANAR")
def on_click_16(): to_station.set("CHOUPASNI")

def on_click_book_ticket():
    try:
        number_passenger = int(no_pass_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of passengers")
        return
    if not from_station.get() or not to_station.get():
        messagebox.showerror("Error", "Please select both FROM and TO stations")
        return
    ticket_data = f"""
        FROM: {from_station.get()} 
        TO: {to_station.get()}
        NUMBER OF PASSENGERS : {number_passenger}
        TOTAL AMOUNT: Rs.{number_passenger * fare}
    """
    with open("Data_1.txt","w") as t:
        t.write(ticket_data)
    messagebox.showinfo("METRO CORPORATION JODHPUR", ticket_data)
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(ticket_data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.show()

heading = tk.Label(root, text="TICKET WINDOW", font=("Arial", 40))
heading.pack(pady=(0,20))

frame = tk.Frame(root)
frame.pack()

from_label = tk.Label(frame,text="From: ")
from_label.grid(row=1,column=0,pady=(0,10))

shikargarh = tk.Button(frame,text="SHIKARGARH", command=on_click_1)
shikargarh.grid(row=2,column=0,pady=(0,10))

ratanada = tk.Button(frame,text="RATANADA",command=on_click_2)
ratanada.grid(row=3,column=0,pady=(0,10))

paota = tk.Button(frame,text="PAOTA", command=on_click_3)
paota.grid(row=4,column=0,pady=(0,10))

sardarpura = tk.Button(frame,text="SARDARPURA",command=on_click_4)
sardarpura.grid(row=5,column=0,pady=(0,10))

basni = tk.Button(frame,text="BASNI",command=on_click_5)
basni.grid(row=6,column=0,pady=(0,10))

shastri_nagar = tk.Button(frame,text="SHASTRI NAGAR",command=on_click_6)
shastri_nagar.grid(row=7,column=0,pady=(0,10))

banar = tk.Button(frame,text="BANAR",command=on_click_7)
banar.grid(row=8,column=0,pady=(0,10))

choupasni = tk.Button(frame,text="CHOUPASNI",command=on_click_8)
choupasni.grid(row=9,column=0,pady=(0,10))

to_label = tk.Label(frame, text="TO: ")
to_label.grid(row=1,column=2,pady=(0,10),padx=150)

shikargarh = tk.Button(frame,text="SHIKARGARH",command=on_click_9)
shikargarh.grid(row=2,column=2,pady=(0,10))

ratanada = tk.Button(frame,text="RATANADA",command=on_click_10)
ratanada.grid(row=3,column=2,pady=(0,10))

paota = tk.Button(frame,text="PAOTA",command=on_click_11)
paota.grid(row=4,column=2,pady=(0,10))

sardarpura = tk.Button(frame,text="SARDARPURA",command=on_click_12)
sardarpura.grid(row=5,column=2,pady=(0,10))

basni = tk.Button(frame,text="BASNI",command=on_click_13)
basni.grid(row=6,column=2,pady=(0,10))

shastri_nagar = tk.Button(frame,text="SHASTRI NAGAR",command=on_click_14)
shastri_nagar.grid(row=7,column=2,pady=(0,10))

banar = tk.Button(frame,text="BANAR",command=on_click_15)
banar.grid(row=8,column=2,pady=(0,10))

choupasni = tk.Button(frame,text="CHOUPASNI",command=on_click_16)
choupasni.grid(row=9,column=2,pady=(0,10))

no_pass = tk.Label(frame, text="NUMBER OF PASSENGERS: ")
no_pass.grid(row=11,column=1,pady=(60,0))

no_pass_entry = tk.Entry(frame)
no_pass_entry.grid(row=11,column=2,pady=(60,0))

book_ticket = tk.Button(frame, text="BOOK TICKET",command=on_click_book_ticket)
book_ticket.grid(row=12,column=1,pady=(50,0))

root.bind('<Return>', lambda event: on_click_book_ticket()) 

root.mainloop()
