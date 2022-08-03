#!/usr/bin/python3

import pyautogui as aut
from pynput import mouse

aut.FAILSAFE = False
screenWidth, screenHeight = aut.size()
b9 = False
b8 = False


def on_click(x,y,button,pressed):
    global b9, b8
    b9 = pressed if button == mouse.Button.button9 else b9
    b8 = pressed if button == mouse.Button.button8 else b8
    if b9 and b8: 
        aut.moveTo(screenWidth/2, screenHeight/2)



with mouse.Listener(on_click=on_click) as listener:
    listener.join()

