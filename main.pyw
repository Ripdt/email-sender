from pystray import Menu, MenuItem, Icon
from PIL import Image
# from email import message

import os
import settings

img = Image.open("icons/gmail.png")
emailInformation = settings.readSettings()

def onClicked(icon, item):
    print('hello world')

def onExitClicked(icon, item):
    icon.stop()

def onSettingsClicked(icon, item):
    os.system("start /wait cmd /c settings.py changeSettings")
    emailInformation = settings.readSettings()

icon = Icon("ripdt-email-sender", img, menu=Menu(
    MenuItem("teste", onClicked),
    MenuItem("configurações", onSettingsClicked),
    MenuItem("sair", onExitClicked)
))

icon.run()

