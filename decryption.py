from PIL import Image 
import math
hidden = Image.open("hidden2.png")
pixel_map = hidden.load()
w,h=hidden.size
MAX_COLOR_VALUE = 256
MAX_BIT_VALUE = 8
n = 4
def get_n_least_significant_bits(value, n):
    value = value << MAX_BIT_VALUE - n
    value = value % MAX_COLOR_VALUE 
    return value
     
for i in range(w):
    for j in range(h):
        r,g,b = hidden.getpixel((i,j))
        r= get_n_least_significant_bits(r, n)
        g= get_n_least_significant_bits(g, n)
        b= get_n_least_significant_bits(b, n)

        pixel_map[i, j] = (r, g, b)
hidden.save("unlock.jpg")  
