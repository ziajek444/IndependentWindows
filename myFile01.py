from pystray import MenuItem as item
import pystray
from PIL import Image

def action():
    pass

image = Image.open("obrazik.jpg")
menu = (item('Options', action), item('Exit', action))
icon = pystray.Icon("Really?", image, "NazwaProgramu", menu)
icon.run()
