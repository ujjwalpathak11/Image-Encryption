import  PIL as pillow
from PIL import Image 
import math
MAX_COLOR_VALUE = 256
MAX_BIT_VALUE = 8
n = 4
inhide = Image.open("inhide2.jpg")
tohide = Image.open("tohide2.jpg")
pix_tohide = tohide.load()
pixel_map = inhide.load()
w,h=inhide.size
def remove_n_least_significant_bits(value, n):
    value = value >> n 
    return value << n
hidden= []
for i in range(w):
    for j in range(h):
        r,g,b = tohide.getpixel((i,j))
        r = r >> MAX_BIT_VALUE - n     #get n msb of to hide img by right shift
        g = g >> MAX_BIT_VALUE - n
        b = b >> MAX_BIT_VALUE - n

        r1,g1,b1 = inhide.getpixel((i,j))
        r1 = remove_n_least_significant_bits(r1, n)
        g1 = remove_n_least_significant_bits(g1, n)
        b1 = remove_n_least_significant_bits(b1, n)

        pixel_map[i, j] = (r + r1, g1 + g,b + b1)
inhide.save("hidden2.png")
