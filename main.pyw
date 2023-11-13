from pystray import Menu, MenuItem, Icon
from PIL import Image

import os
import settings

img = Image.open("icons/gmail.png")
emailInformation = settings.readSettings()

def onSendClicked(icon, item):
    os.system("start /wait cmd /c send.py sendEmail " + emailInformation.__str__())

def onExitClicked(icon, item):
    icon.stop()

def onSettingsClicked(icon, item):
    os.system("start /wait cmd /c settings.py changeSettings")
    emailInformation = settings.readSettings()

icon = Icon("ripdt-email-sender", img, menu=Menu(
    MenuItem("enviar e-mail", onSendClicked),
    MenuItem("configurações", onSettingsClicked),
    MenuItem("sair", onExitClicked)
))

icon.run()

