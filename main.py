import time
from pynput.keyboard import Listener
import pydirectinput
import threading
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import ttk 
import sys
import os

OUTPUT_PATH = sys.path[0]
ASSETS_PATH = os.path.join(OUTPUT_PATH, "build")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

Keys = ("Left click", "Right click", "Middle click", 'space', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright')

PressableKeys = (
	'space', 'esc', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 
	'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
	'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
	't', 'u', 'v', 'w', 'x', 'y', 'z', 
	'tab', 'backspace','delete','capslock', 'enter', 'shift', 'shiftr', 'ctrll', 'cmd', 'altl', 'altgr', 'cmdr', 'menu', 'ctrlr',
	'-', '=', '`', '/', '*','[', ']', '\\', ';', "'",',', '.', 
)

TimeTypes = ("ms", "s", "m", "h")

window = Tk()

window.geometry("419x340")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 340,
    width = 419,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    419.0,
    340.0,
    fill="#212121",
    outline="")

StartRectangle = canvas.create_rectangle(
    19.0,
    282.0,
    199.0,
    326.0,
    fill="#323232",
    outline="", tags="Start")

StopRectangle = canvas.create_rectangle(
    225.0,
    284.0,
    405.0,
    328.0,
    fill="#323232",
    outline="", tags="Stop")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    122.0,
    168.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    326.0,
    168.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    212.0,
    48.0,
    image=image_image_3
)

canvas.create_text(
    14.0,
    6.0,
    anchor="nw",
    text="Intervals",
    fill="#F3F3F3",
    font=("SourceSansPro Regular", 14 * -1)
)

canvas.create_text(
    162.0,
    16.0,
    anchor="nw",
    text="Burst",
    fill="#F3F3F3",
    font=("SourceSansPro Regular", 10 * -1)
)

canvas.create_text(
    295.0,
    16.0,
    anchor="nw",
    text="Hold",
    fill="#F3F3F3",
    font=("SourceSansPro Regular", 10 * -1)
)

canvas.create_text(
    14.0,
    88.0,
    anchor="nw",
    text="Options",
    fill="#F3F3F3",
    font=("SourceSansPro Regular", 14 * -1)
)

canvas.create_text(
    34.0,
    128.0,
    anchor="nw",
    text="Key:",
    fill="#F3F3F3",
    font=("SourceSansPro Regular", 14 * -1)
)

canvas.create_text(
    34.0,
    176.0,
    anchor="nw",
    text="Burst amount:",
    fill="#F3F3F3",
    font=("SourceSansPro Regular", 14 * -1)
)

canvas.create_text(
    261.0,
    120.0,
    anchor="nw",
    text="Start:",
    fill="#F3F3F3",
    font=("SourceSansPro Regular", 14 * -1)
)

canvas.create_text(
    262.0,
    157.0,
    anchor="nw",
    text="Stop:",
    fill="#F3F3F3",
    font=("SourceSansPro Regular", 14 * -1)
)

canvas.create_text(
    243.0,
    88.0,
    anchor="nw",
    text="Key Settings",
    fill="#F3F3F3",
    font=("SourceSansPro Regular", 14 * -1)
)

canvas.create_text(
    20.0,
    284.0,
    anchor="nw",
    text="Start",
    fill="#F3F3F3",
    font=("SourceSansPro Regular", 36 * -1), tags="Start"
)

canvas.create_text(
    226.0,
    284.0,
    anchor="nw",
    text="Stop",
    fill="#F3F3F3",
    font=("SourceSansPro Regular", 36 * -1), tags="Stop"
)

import tkinter as tinka
strVar = tinka.StringVar() 

#Duration 
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png")
)
entry_bg_1 = canvas.create_image(
    56.5,
    51.0,
    image=entry_image_1
)
DurationText = Entry(
    bd=0,
    font=("SourceSansPro Regular", 13 * -1),
    bg="#1F1F1F",
    fg="#F3F3F3",
    highlightthickness=0
)
DurationText.insert(0, "100")
DurationText.place(
    x=29.0,
    y=29.0,
    width=55.0,
    height=42.0
)

#DurationType
# entry_image_2 = PhotoImage(
#     file=relative_to_assets("entry_2.png"))
# entry_bg_2 = canvas.create_image(
#     112.0,
#     51.0,
#     image=entry_image_2
# )
# entry_2 = Entry(
#     bd=0,
#     bg="#1F1F1F",
#     fg="#000716",
#     highlightthickness=0
# )

keepvalue = strVar.get()

DurationType = ttk.Combobox(window, textvariable = keepvalue, state="readonly", background='#1F1F1F') 
DurationType['values'] = TimeTypes
DurationType.current(0) 

DurationType.place(
    x=95.0,
    y=29.0,
    width=40.0,
    height=42.0
)

#BurstDuration
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    189.5,
    51.0,
    image=entry_image_3
)
BurstDurationText = Entry(
    bd=0,
    font=("SourceSansPro Regular", 13 * -1),
    bg="#1F1F1F",
    fg="#F3F3F3",
    highlightthickness=0
)
BurstDurationText.place(
    x=162.0,
    y=29.0,
    width=55.0,
    height=42.0
)

#BurstType
entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    245.0,
    51.0,
    image=entry_image_8
)
BurstDurationType = ttk.Combobox(window, textvariable = keepvalue, state="readonly", background='#1F1F1F') 
BurstDurationType['values'] = TimeTypes
BurstDurationType.current(0) 

BurstDurationType.place(
    x=228.0,
    y=29.0,
    width=40.0,
    height=42.0
)

#HoldDuration
HoldDurationText = Entry(
    bd=0,
    font=("SourceSansPro Regular", 13 * -1),
    bg="#1F1F1F",
    fg="#F3F3F3",
    highlightthickness=0
)
HoldDurationText.place(
    x=295.0,
    y=29.0,
    width=55.0,
    height=42.0
)

HoldType = ttk.Combobox(window, textvariable = keepvalue, state="readonly", background='#1F1F1F') 
HoldType['values'] = TimeTypes + ("until stopped",)
HoldType.current(0) 

HoldType.place(
    x=361.0,
    y=29.0,
    width=40.0,
    height=42.0
)

#Key
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    171.5,
    142.0,
    image=entry_image_4
)
# entry_4 = Entry(
#     bd=0,
#     font=("SourceSansPro Regular", 13 * -1),
#     bg="#1F1F1F",
#     fg="#F3F3F3",
#     highlightthickness=0
# )


KeyTarget = ttk.Combobox(window, textvariable = keepvalue, state="readonly", background='#1F1F1F') 
KeyTarget['values'] = Keys
KeyTarget.current(0) 

KeyTarget.place(
    x=144.0,
    y=127.0,
    width=55.0,
    height=28.0
)

#Burst amount
entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    171.5,
    187.0,
    image=entry_image_5
)
BurstAmount = Entry(
    bd=0,
    font=("SourceSansPro Regular", 13 * -1),
    bg="#1F1F1F",
    fg="#F3F3F3",
    highlightthickness=0
)
BurstAmount.insert(0, "1")
BurstAmount.place(
    x=144.0,
    y=172.0,
    width=55.0,
    height=28.0
)

#StartKey
entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    356.5,
    131.0,
    image=entry_image_6
)
# entry_6 = Entry(
#     bd=0,
#     font=("SourceSansPro Regular", 13 * -1),
#     bg="#1F1F1F",
#     fg="#F3F3F3",
#     highlightthickness=0
# )

StartKey = ttk.Combobox(window, textvariable = keepvalue, state="readonly", background='#1F1F1F') 
StartKey['values'] = PressableKeys
StartKey.current(0) 

StartKey.place(
    x=329.0,
    y=116.0,
    width=55.0,
    height=28.0
)

#StopKey
entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    357.5,
    171.0,
    image=entry_image_7
)
# entry_7 = Entry(
#     bd=0,
#     font=("SourceSansPro Regular", 13 * -1),
#     bg="#1F1F1F",
#     fg="#F3F3F3",
#     highlightthickness=0
# )

StopKey = ttk.Combobox(window, textvariable = keepvalue, state="readonly", background='#1F1F1F') 
StopKey['values'] = ("None",) + PressableKeys
StopKey.current(0) 

StopKey.place(
    x=330.0,
    y=156.0,
    width=55.0,
    height=28.0
)

from PIL import ImageTk, Image

window.iconphoto(False, ImageTk.PhotoImage(file=OUTPUT_PATH / Path(r"C:\Users\Windows\OneDrive\Desktop\Projects\Macro\AutoClicker\build\AutoSpam.ico")))
window.attributes('-topmost', True)
window.title('Super cool auto exe')
window.resizable(False, False)

KeyListener = None

Running = True
BurstDuration = None

Enabled = False
Holding = True

def PressKey(Key):
	if Key == "Left click":
		pydirectinput.leftClick()
	elif Key == "Right click":
		pydirectinput.rightClick()
	elif Key == "Middle click":
		pydirectinput.middleClick()
	else:
		pydirectinput.press(Key)

def PressDown(Key):
	if Key == "Left click":
		pydirectinput.mouseDown(button="left")
	elif Key == "Right click":
		pydirectinput.mouseDown(button="right")
	elif Key == "Middle click":
		pydirectinput.mouseDown(button="middle")
	else:
		pydirectinput.keyDown(Key)

def PressUp(Key):
	if Key == "Left click":
		pydirectinput.mouseUp(button="left")
	elif Key == "Right click":
		pydirectinput.mouseUp(button="right")
	elif Key == "Middle click":
		pydirectinput.mouseUp(button="middle")
	else:
		pydirectinput.keyUp(Key)
 
def ForceEnable(Args = None):
	global Enabled
	Enabled = True

def ForceDisable(Args = None):
	global Enabled, Holding

	threading.Thread(target=PressUp, args=(KeyTarget.get(),)).start()
	Enabled = False
	Holding = False

def KeyPressed(Pressed: str):
	global Enabled

	Pressed = str(Pressed)
	Pressed = (len(Pressed) == 3 and Pressed[1]) or Pressed
	Pressed = Pressed.replace("Key.", "")
	Pressed = Pressed.replace("_", "")

	if StopKey.get() == Pressed and Enabled:
		ForceDisable()
	elif StartKey.get() == Pressed and not Enabled:
		ForceEnable()

def KeyReleased(Pressed):
	global Enabled

	Pressed = str(Pressed)
	Pressed = (len(Pressed) == 3 and Pressed[1]) or Pressed
	Pressed = Pressed.replace("Key.", "")
	Pressed = Pressed.replace("_", "")

	if StartKey.get() == Pressed and StopKey.get() == "None":
		ForceDisable()

def ListenKeyPress():
	global KeyListener
	with Listener(on_press=KeyPressed, on_release=KeyReleased) as listener:
		KeyListener = listener
		listener.join()

def StringToNumber(String):
	try:
		return float(String)
	except: pass

def GetMultiplier(Type):
	if Type == "ms":
		return 0.001
	elif Type == "s":
		return 1
	elif Type == "m":
		return 60
	elif Type == "h":
		return 60 * 60

def StartListen():
	global Running, Holding

	while True:
		if not Running:
			break

		if not Enabled: 
			time.sleep(0.1)
			continue
		
		KeyAmount = StringToNumber(BurstAmount.get()) or 1
		Duration = (StringToNumber(DurationText.get()) or 1) * GetMultiplier(DurationType.get())
		BurstDuration = StringToNumber(BurstDurationText.get())
		HoldDuration = StringToNumber(HoldDurationText.get())
		ChosenHoldType = HoldType.get()

		if HoldDuration:
			HoldDuration *= GetMultiplier(DurationType.get())

		if ChosenHoldType == "until stopped":
			HoldDuration = True

		if BurstDuration:
			BurstDuration *= GetMultiplier(BurstDurationType.get())

		for i in range(int(KeyAmount)):
			print(HoldDuration)
			if not HoldDuration:
				threading.Thread(target=PressKey, args=(KeyTarget.get(),)).start()
			elif HoldDuration == True and not Holding:
				threading.Thread(target=PressDown, args=(KeyTarget.get(),)).start()
				Holding = True
			else:
				threading.Thread(target=PressDown, args=(KeyTarget.get(),)).start()
				time.sleep(HoldDuration)
				threading.Thread(target=PressUp, args=(KeyTarget.get(),)).start()
			
			if BurstDuration:
				time.sleep(BurstDuration)
		
		time.sleep(Duration)

threading.Thread(target=ListenKeyPress).start()
threading.Thread(target=StartListen).start()

canvas.tag_bind("Start","<Button-1>", ForceEnable)
canvas.tag_bind("Stop","<Button-1>", ForceDisable)

window.mainloop()
Running = False
KeyListener.stop()
