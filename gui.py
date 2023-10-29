

from pathlib import Path
import serial
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import json


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")
window = Tk()
window.geometry("796x610")
window.configure(bg = "#FFFFFF")

ser = None

MSG_FONT_SIZE = 20

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def read_data():
    try:
        data = ser.readline().decode('utf-8').strip()
        window.after(1000, read_data)  # Update every 1 second
        jsonData=json.loads(data)
        print(jsonData)
        update_gui(jsonData)
    except Exception as e:
        print(f"Error reading data: {e}")

def update_gui(data):
    canvas.itemconfig(humidityMsgID,text=data["humidity"]["msg"])
    canvas.itemconfig(soilMoistMsgID,text=data["moisture"]["msg"])
    canvas.itemconfig(tempMsgID,text=data["temp"]["msg"])

    canvas.itemconfig(humidityValueID,text=str(data["humidity"]["value"]) + " %")
    canvas.itemconfig(soilMoistValueID,text=str(data["moisture"]["value"]) + " %")
    canvas.itemconfig(tempValueID,text=str(data["temp"]["value"]) + "° C")



def main():
    try:
        global ser
        ser = serial.Serial('/dev/ttyACM0', 9600) 
        read_data()
        window.resizable(False, False)
        window.mainloop()
    except Exception as e:
        print(f"Error opening serial port: {e}")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 610,
    width = 796,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    1.0,
    80.0,
    797.0,
    610.0,
    fill="#F8FBF0",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    398.0,
    40.0,
    image=image_image_1
)

canvas.create_text(
    40.0,
    22.0,
    anchor="nw",
    text="Plant Language Translator",
    fill="#8ABB18",
    font=("MochiyPopOne Regular", 24 * -1)
)

timeID = canvas.create_text(
    669.0,
    27.0,
    anchor="nw",
    text="14:26 pm",
    fill="#98B747",
    font=("MochiyPopOne Regular", 18 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    397.0,
    186.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    392.0,
    201.0,
    image=image_image_3
)

tempMsgID = canvas.create_text(
    81.0,
    186.0,
    anchor="nw",
    text="",
    fill="#7BA618",
    font=("Livvic Regular", MSG_FONT_SIZE * -1)
)

canvas.create_text(
    72.0,
    139.0,
    anchor="nw",
    text="Temperature",
    fill="#628610",
    font=("Livvic Medium", 24 * -1)
)

tempValueID = canvas.create_text(
    657.0,
    145.0,
    anchor="nw",
    text="",
    fill="#71824A",
    font=("Poppins Regular", 16 * -1),
    justify="right"
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    398.0,
    352.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    393.0,
    367.0,
    image=image_image_5
)

soilMoistMsgID = canvas.create_text(
    82.0,
    354.0,
    anchor="nw",
    text="",
    fill="#7BA618",
    font=("Livvic Regular", MSG_FONT_SIZE * -1)
)

canvas.create_text(
    73.0,
    305.0,
    anchor="nw",
    text="Soil Moisture",
    fill="#628610",
    font=("Livvic Medium", 24 * -1)
)

soilMoistValueID = canvas.create_text(
    657.0,
    311.0,
    anchor="nw",
    text="",
    fill="#3B5107",
    font=("Poppins Regular", 16 * -1),
    justify="right"
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    398.0,
    518.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    393.0,
    533.0,
    image=image_image_7
)

humidityMsgID = canvas.create_text(
    82.0,
    520.0,
    anchor="nw",
    text="",
    fill="#7BA618",
    font=("Livvic Regular", MSG_FONT_SIZE * -1)
)

canvas.create_text(
    73.0,
    471.0,
    anchor="nw",
    text="Humidity",
    fill="#628610",
    font=("Livvic Medium", 24 * -1)
)

humidityValueID =  canvas.create_text(
    657.0,
    477.0,
    anchor="nw",
    text="",
    fill="#3B5107",
    font=("Poppins Regular", 16 * -1),
    justify="right"
)


main()







