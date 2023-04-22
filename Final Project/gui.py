from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter
from gui2 import *
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / \
    Path(r"./assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def gui1():

    def button_event():
        # DATABASE
        pokename = entry_1.get()

        # Creating the connection object
        conn_obj = mysql.connector.connect(
            host="localhost", user="root", passwd="mannshrimali2003", database="PYcapstone")

        # creating the cursor object
        cur_obj = conn_obj.cursor()

        try:
            cur_obj.execute("Select * from pokedata where name='"+pokename+"'")

        except:
            # it is used if the operation is failed then it will not reflect in your database
            conn_obj.rollback()

        ofnum = ""
        desc = ""
        type1 = ""
        type2 = ""

        for info in cur_obj:
            ofnum = info[0]
            desc = info[2]
            type1 = info[3]
            type2 = info[4]

        conn_obj.close()

        poke_input.set("")

        gui2(pokename, ofnum, type1, type2, desc)
        # Button Event Ends Here

    window = tkinter.Tk()
    window.geometry("550x550")
    window.configure(bg="#FFFFFF")
    window.title("Capstone Project in Python by Mann Shrimali")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=550,
        width=550,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        550.0,
        550.0,
        fill="#D9D9D9",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        275.0,
        275.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        265.0,
        80.0,
        image=image_image_2
    )

    canvas.create_rectangle(
        29.0,
        -1.0,
        34.089202880859375,
        549.9993286132812,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        27.0,
        -3.0,
        34.089202880859375,
        549.9993286132812,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        512.0,
        -3.0,
        516.0,
        550.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        0.0,
        0.0,
        550.0,
        21.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        29.0,
        135.0,
        515.0,
        142.0,
        fill="#3200FF",
        outline="")

    canvas.create_rectangle(
        9.0,
        303.0,
        12.0,
        550.0,
        fill="#0038FF",
        outline="")

    canvas.create_rectangle(
        532.0,
        303.0,
        535.0,
        550.0,
        fill="#0038FF",
        outline="")

    poke_input=tkinter.StringVar()

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        362.0,
        190.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFD5D5",
        fg="#000716",
        textvariable=poke_input,
        font=('Helvetica 17'),
        highlightthickness=0
    )
    entry_1.place(
        x=237.0,
        y=173.0,
        width=250.0,
        height=33.0
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        434.0,
        427.0,
        image=image_image_3
    )

    canvas.create_rectangle(
        248.0,
        248.0,
        316.0,
        330.0,
        fill="#000000",
        outline="")

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        280.0,
        290.0,
        image=image_image_4
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        # command=lambda: print("button_1 clicked"),
        command=button_event,
        relief="flat"
    )
    button_1.place(
        x=496.0,
        y=176.0,
        width=39.0,
        height=31.0
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        133.0,
        191.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        127.0,
        337.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        196.0,
        452.0,
        image=image_image_7
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        550.0,
        21.0,
        fill="#FFCE31",
        outline="")
    window.resizable(False, False)

    window.mainloop()


gui1()
