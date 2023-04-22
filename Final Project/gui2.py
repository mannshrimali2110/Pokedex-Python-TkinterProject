from pathlib import Path
from tkinter import *
import tkinter
from PIL import Image, ImageTk
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / \
    Path(r"./assets/frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def gui2(pokename, ofnum, type1, type2, desc):

    window = Toplevel()
    window.geometry("650x675")
    window.configure(bg="#FFFFFF")

    pokemon_var = tkinter.StringVar()
    ofnum_var = tkinter.StringVar()
    Desc_var = tkinter.StringVar()
    type1_var = tkinter.StringVar()
    type2_var = tkinter.StringVar()

    pokemon_var.set(pokename)
    ofnum_var.set(ofnum)
    Desc_var.set(desc)
    type1_var.set(type1)
    type2_var.set(type2)

    def exit_buttonevent():
        window.destroy()
        window.update()
        # gui1()

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=675,
        width=650,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        325.0,
        337.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        308.0,
        79.0,
        image=image_image_2
    )

    canvas.create_rectangle(
        4.97760009765625,
        -3.0,
        11.0,
        674.9998779296875,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        634.0000152587891,
        -3.0,
        640.0223999023438,
        674.9998779296875,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        224.0,
        261.0,
        429.0,
        446.0,
        fill="#00FFE0",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        376.0,
        189.0,
        image=entry_image_1
    )

    entry_1 = Entry(  # Pokemon_name
        window,
        bd=0,
        bg="#FFABAB",
        textvariable=pokemon_var,
        fg="#000716",
        font=('Helvetica 17'),
        highlightthickness=0
    )
    entry_1.place(
        x=256.0,
        y=170.0,
        width=240.0,
        height=36.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        546.5,
        287.5,
        image=entry_image_2
    )
    entry_2 = Entry(  # Type1
        window,
        bd=0,
        textvariable=type1_var,
        bg="#000000",
        fg="white",
        font=('Helvetica 16'),
        highlightthickness=0
    )
    entry_2.place(
        x=492.0,
        y=268.0,
        width=109.0,
        height=37.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        110.5,
        293.0,
        image=entry_image_3
    )
    entry_3 = Entry(  # Official Number
        window,
        bd=0,
        textvariable=ofnum_var,
        bg="#000000",
        fg="white",
        font=('Helvetica 17'),
        highlightthickness=0
    )
    entry_3.place(
        x=68.0,
        y=268.0,
        width=85.0,
        height=48.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        542.5,
        434.5,
        image=entry_image_4
    )
    entry_4 = Entry(  # Type2
        window,
        bd=0,
        textvariable=type2_var,
        bg="#000000",
        fg="white",
        font=('Helvetica 16'),
        highlightthickness=0
    )
    entry_4.place(
        x=488.0,
        y=415.0,
        width=109.0,
        height=37.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        318.5,
        539.5,
        image=entry_image_5
    )

    entry_5 = Text(  # Description
        window,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        font=('Helvetica 17'),
        highlightthickness=0
    )
    entry_5.insert(END, desc)
    entry_5.place(
        x=30.0,
        y=473.0,
        width=577.0,
        height=131.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        window,
        command=exit_buttonevent,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    button_1.place(
        x=247.0,
        y=617.0,
        width=149.0,
        height=46.0
    )

    imgadrs = pokename+".png"

    resizeimg = Image.open(
        "./assets/pokeimg/"+imgadrs)

    resizeimg = resizeimg.resize((150, 150))
    image_image_3 = ImageTk.PhotoImage(resizeimg)

    image_3 = canvas.create_image(
        324.0,
        353.0,
        image=image_image_3
    )

    canvas.create_rectangle(
        -5.0,
        152.0,
        649.0,
        157.0,
        fill="#00FFC1",
        outline="")

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        110.0,
        239.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        133.0,
        186.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        542.0,
        243.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        541.0,
        395.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        118.0,
        423.0,
        image=image_image_8
    )
    window.resizable(False, False)
    window.mainloop()
