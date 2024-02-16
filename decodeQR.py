from pyzbar.pyzbar import decode
from PIL import Image

decodeQR = decode(Image.open('instagram.png'))
